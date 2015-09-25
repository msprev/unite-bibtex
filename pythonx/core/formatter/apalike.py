import util

def default(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += "'%s'" % title
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def article(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    journal = e.get('journal', '=no journal=')
    volume = e.get('volume', None)
    pages = e.get('pages', None)
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += "'%s'" % title
    text += ', '
    text += '%s' % journal
    if volume:
        text += ', '
        text += volume
    if pages:
        text += ', '
        text += 'pp. ' + pages
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def unpublished(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += "'%s'" % title
    text += ', '
    text += 'unpublished manuscript'
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def phdthesis(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    school = e.get('school', '=no school=')
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += "'%s'" % title
    text += ', '
    text += school
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def mastersthesis(e):
    return phdthesis(e)

def book(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    publisher = e.get('publisher', None)
    address = e.get('address', None)
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += '%s' % title
    if address or publisher:
        text += ', '
        if address:
            text += address
            text += ': '
        if publisher:
            text += publisher
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def incollection(e):
    # get the data
    author = util.author(e, 5)
    year = e.get('year', 'no year')
    title = e.get('title', '=no title=')
    publisher = e.get('publisher', None)
    address = e.get('address', None)
    editor = util.editor(e, 3)
    booktitle = e.get('booktitle', '=no booktitle=')
    bibtex_key = unicode(e['ID'])
    bibtex_type = e['ENTRYTYPE']
    # build the string
    text = str()
    text += author
    text += ' '
    text += '(%s)' % year
    text += ' '
    text += '%s' % title
    if editor != '=no editor=' or booktitle != '=no booktitle=':
        text += ' in'
        if editor != '=no editor=':
            text += ' '
            text += editor
            text += ' '
            if len(e['editor']) == 1:
                text += '(Ed.)'
            else:
                text += '(Eds.)'
        text += ' '
        text += booktitle
    if address or publisher:
        text += ', '
        if address:
            text += address
            text += ': '
        if publisher:
            text += publisher
    text += ' '
    text += '@' + bibtex_key
    text += ' '
    text += '[%s]' % bibtex_type
    # remove latex markup crap
    text = util.remove_latex_crap(text)
    return text

def inproceedings(e):
    return incollection(e)

