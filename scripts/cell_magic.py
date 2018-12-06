from IPython.core.magic import register_line_magic

print("    cell magic: %less_n <fname>")

@register_line_magic
def less_n(arg_s):
    from IPython.core import page
    """Show a file through the pager.

    Files ending in .py are syntax-highlighted."""
    if not arg_s:
        raise UsageError('Missing filename.')

    fid = open(arg_s, 'r')
    cont = 'SHOWING FIRST 200 LINES OF FILE WITH LINE NUMBERS (NOT PART OF FILE)\n'
    cont += '=' * 68 + '\n\n'
    for i, line in enumerate(fid):
        line = line.replace('\t', ' '*4)
        cont += '{: >3d}  {}'.format(i, line[:100] + '...\n' if len(line) > 100 else line)
        if i == 200:
            break

    page.page(cont)
