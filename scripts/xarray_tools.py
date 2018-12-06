from __future__ import print_function
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt


print("    xarray tools: xr.DataArray.map()")

@xr.register_dataarray_accessor('map')
class CartopyMap(object):
    """
    Plot the given 2D array on a cartopy axes (assuming that Lat and Lon exist)
    The default projection is PlateCarree, but can be:
        cartopy.crs.<ProjectionName>()

    If the projection is Stereographic the plot will be round unless
    the keyword arguement `round` is set False.

    If you would like to create a figure with multiple subplots
    you can pass an axes object to the function with keyword argument `ax,
    BUT then you need to specify the projection when you create the axes:
        plt.axes([x0, y0, w, h], projection=cartopy.crs.<ProjectionName>())

    Additional keywords can be given to the function as you would to
    the xr.DataArray.plot function. The only difference is that `robust`
    is set to True by default.

    The function returns a GeoAxes object to which features can be added with:
        ax.add_feature(feature.<FeatureName>, **kwargs)
    By default, LAND and COASTLINE are added, but can be removed by
    setting default_features=False

    Written by Luke Gregor
    """
    def __init__(self, xarray_obj):
        self._obj = xarray_obj

    def __call__(self, ax=None, proj=None, round=True, default_features=True, **kwargs):
        return self._cartopy(ax=ax, proj=proj, round=round, default_features=default_features, **kwargs)

    def _cartopy(self, ax=None, proj=None, round=True, default_features=True, **kwargs):
        import matplotlib.path as mpath
        import matplotlib.pyplot as plt
        from cartopy import feature
        from cartopy import crs

        xda = self._obj
        assert xda.ndim == 2, 'The array must be two dimensional'

        if ax is None:
            tighten = True
            proj = crs.PlateCarree() if proj is None else proj
            fig, ax = plt.subplots(
                1, 1, figsize=[11, 4], dpi=100,
                subplot_kw={'projection': proj})
        else:
            tighten = False

        stereo_maps = (crs.Stereographic,
                       crs.NorthPolarStereo,
                       crs.SouthPolarStereo)
        if isinstance(proj, stereo_maps) & round:
            theta = np.linspace(0, 2 * np.pi, 100)
            center, radius = [0.5, 0.5], 0.5
            verts = np.vstack([np.sin(theta), np.cos(theta)]).T
            circle = mpath.Path(verts * radius + center)

            ax.set_boundary(circle, transform=ax.transAxes)

        if default_features:
            ax.add_feature(feature.LAND, color='#CCCCCC', zorder=4)
            ax.add_feature(feature.COASTLINE, lw=0.5, zorder=4)

        if 'robust' not in kwargs:
            kwargs['robust'] = True
        if ('cbar_kwargs' not in kwargs) & kwargs.get('add_colorbar', True):
            kwargs['cbar_kwargs'] = {'pad': 0.02}

        axm = xda.plot(ax=ax, transform=crs.PlateCarree(), **kwargs)
        if kwargs.get('add_colorbar', True):
            ax.colorbar = axm.colorbar
        if tighten:
            fig.tight_layout()

        return ax

