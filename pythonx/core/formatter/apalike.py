import util

def default(e):
    # get the data
    author = util.author_or_editor(e, 5)
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
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
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
    journal = util.get(e, 'journal', '=no journal=')
    volume = util.get(e, 'volume', None)
    pages = util.get(e, 'pages', None)
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
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
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
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
    school = util.get(e, 'school', '=no school=')
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
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
    publisher = util.get(e, 'publisher', None)
    address = util.get(e, 'address', None)
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
    year = util.get(e, 'year', 'no year')
    title = util.get(e, 'title', '=no title=')
    publisher = util.get(e, 'publisher', None)
    address = util.get(e, 'address', None)
    editor = util.editor(e, 3)
    pages = util.get(e, 'pages', None)
    booktitle = util.get(e, 'booktitle', '=no booktitle=')
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

def inproceedings(e):
    return incollection(e)
    
def inbook(e):
    return incollection(e)


