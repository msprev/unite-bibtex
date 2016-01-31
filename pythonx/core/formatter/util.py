def get(e, key, default):
    """
    return e.get(key, default)
    if bibtex version of key not found, use biblatex version
    """
    BIBLATEX = {'year': 'date',
                'journal': 'journaltitle',
                'address': 'location'}
    if key not in BIBLATEX:
        return e.get(key, default)
    else:
        return e.get(key, e.get(BIBLATEX[key], default))


def author_or_editor(e, max_num):
    """
    return string flattened list of either authors or editors
    - authors returned in preference to editors
    - if neither found, then '=no author=' is returned
    :e: bibtex entry
    :max_num: maximum number of names to include, other marked by 'et al'
    :returns: string with authors or editors
    """
    authors = get(e, 'author', None)
    editors = get(e, 'editor', None)
    if authors:
        return flatten_list(authors, max_num)
    elif editors:
        return flatten_list(editors, max_num)
    else:
        return '=no author='

def author(e, max_num):
    """
    return string flattened list of authors
    - if not found, then '=no author=' is returned
    :e: bibtex entry
    :max_num: maximum number of names to include, other marked by 'et al'
    :returns: string with authors
    """
    authors = get(e, 'author', ['=no author='])
    return flatten_list(authors, max_num)


def editor(e, max_num):
    """
    return string flattened list of editors
    - if not found, then '=no author=' is returned
    :e: bibtex entry
    :max_num: maximum number of names to include, other marked by 'et al'
    :returns: string with editors
    """
    editors = get(e, 'editor', ['=no editor='])
    return flatten_list(editors, max_num)

def flatten_list(names, max_num):
    """
    flattens a list of authors or editors and caps it a max number
    :names: list of names
    :num: maximum number of names to include, others marked by 'et al.'
    :returns: string of flattened list
    """
    # sanity check: empty list returns empty string
    if len(names) == 0:
        return ''
    # add first author
    text = names[0]
    # add next authors
    for i in range(1, min(max_num, len(names))):
            text += ' and ' + names[i]
    # add truncated authors
    if len(names) > max_num:
        text += ' et al.'
    return text

def remove_latex_crap(incoming):
    """
    remove funny latex characters and text from incoming string
    - uses list of subs for find and replace
    :returns: string with characters removed
    """
    subs = [('~', ' '),
            ('\\emph{', ''),
            ('}', ''),
            ('{', ''),
            ('\\', ''),
            ('--', '-')]
    text = incoming
    for s in subs:
        text = text.replace(s[0], s[1])
    return text

