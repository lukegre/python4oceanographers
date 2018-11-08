Python for earth scientists
===========
<p style="color:#aaa">An introduction to working with data in python for scientists</p>

- [Basic Info](#basic-info)
- [What you need to join](#what-you-need-to-join)
- [What will you learn?](what-will-you-learn?)
- [Daily Breakdown](#daily-breakdown)


### tl;dr
```
WHAT:  Python - numpy, scipy, matplotlib, pandas, xarray
WHEN:  11 - 13 December 2018
WHERE: CSIR, Rosebank
WHO:   Beginners with sound knowledge of lists, tuple, for loop, if statement
COST:  R150 per day
HOW:   On your own laptop with Luke and Tommy teaching interactively
```

---

### Basic Info
The course will be run by [Luke Gregor](https://github.com/luke-gregor) and Tommy Ryan-Keogh and will be hosted at the CSIR.

Anyone can join but we are limited to 20 spaces - so first come first serve.

Note that the course will also cost R150 per day. Note that the days build on each other so I recommend that you only skip days if you've done the course before and you want a refresher. This can be paid to Luke in person *(a brother's gotta eat)* - details to follow.

### What you need to join
- A laptop with the Anaconda distribution of Python installed (https://www.anaconda.com/download/)
- A sound understanding of basic python: **Part 1**  at https://python101.pythonlibrary.org/index.html. You will quickly fall behind if you don't understand:
    - types: `str, int, float, list, tuple, dict`
    - for loops
    - if statements
    - import packages
- Know how to have packages installed with `conda` in the command line
    - `conda install pandas scikit-learn netCDF4 xarray`

### What will you learn?
We will cover the tools you need to work with data in python to create plots like this (and many more):

<img src="download.png" style="width:33%; float:left">
<img src="_SVR_trainTest_2Dhist_wchl.png" style="width:66%; float:left">

However, you will not walk away as ninja. This takes time and practice. The course serves as a crash course to working with and plotting data. We will go over example problems, but it will help if you come with your own data so you can learn on the fly.

---

## Daily breakdown
#### DAY 1 (numpy)
Core Python recap, `numpy` and `matplotlib`
- recap core Python
- importing data
- working with data - indexing, slicing, etc.
- plotting lines and scatter

#### DAY 2 (pandas)
`pandas` will change your life (if you work with time series or any other table data).
- importing data
- time series resampling
- plotting recap with pandas
- linear regression with `sklearn`
- groupby (for the advanced)

#### DAY 3 (xarray)
`xarray` is a netCDF tool and probably saved me four months in my PhD
- importing netCDF
- temporal resampling
- calculating climatologies
- plotting maps with cartopy
