def author(e):
    """@todo: Docstring for author.

    :e: @todo
    :returns: @todo

    """
    x = str()
    if 'author' in e:
        desc += add_names(e['author'], 5)
    return x


def add_names(names, max_num):
    out = str()
    for i in range(0, min(max_num, len(names))):
        if i == 0:
            out += decrap(names[i])
        else:
            out += ' and ' + decrap(names[i])
    if len(names) > max_num:
        out += ' et al.'
    return out

