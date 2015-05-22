import vim
import bibtexparser
from operator import itemgetter
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

def customizations(record):
    record = homogeneize_latex_encoding(record)
    record = convert_to_unicode(record)
    record = author(record)
    record = editor_split(record)
    return record

def editor_split(record):
    """
    Split editor field into a list of "Name, Surname".

    :param record: the record.
    :type record: dict
    :returns: dict -- the modified record.

    """
    if "editor" in record:
        if record["editor"]:
            record["editor"] = getnames([i.strip() for i in record["editor"].replace('\n', ' ').split(" and ")])
        else:
            del record["editor"]
    return record

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

def decrap(incoming):
    out = incoming.replace("~", " ").replace("\\emph{", "").replace("}", "").replace("{", "")
    return out

def populate_list():
    with open('/Users/msprevak/Dropbox/msprevak/Library/texmf/bibtex/bib/mds-bib/refs.bib') as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        bib_database = bibtexparser.load(bibtex_file, parser=parser)
        entries = sorted(bib_database.entries, key=itemgetter('id'))

    for e in entries:
        desc = str()
        # add the author or editor
        if 'author' in e:
            desc += add_names(e['author'], 5)
        elif 'editor' in e:
            desc += add_names(e['editor'], 5)
            desc += ' (Ed.)'
        # add the year
        if 'year' in e:
            desc += ' (%s)' % e['year']
        # add the title
        if 'title' in e:
            if 'type' in e and e['type'] == 'book':
                desc += " '" + decrap(e['title']) + "'"
            else:
                desc += " '" + decrap(e['title']) + "'"
        if 'type' in e:
            if e['type'] == 'article':
                if 'journal' in e:
                    desc += ", " + decrap(e['journal'])
                    if 'volume' in e:
                        desc += ', ' + e['volume']
                    if 'pages' in e:
                        desc += ', pp. ' + e['pages']
            elif e['type'] == 'incollection' or e['type'] == 'inproceedings':
                    if 'editor' in e or 'booktitle' in e:
                        desc += ' in'
                    if 'editor' in e:
                        desc += " %s (Ed.)" % add_names(e['editor'], 4)
                    if 'booktitle' in e:
                        desc += " '" + decrap(e['booktitle']) + "'"
            elif e['type'] == 'book':
                if 'publisher' in e:
                    desc += ", " + decrap(e['publisher'])
            elif e['type'] == 'mastersthesis' or e['type'] == 'phdthesis':
                if 'school' in e:
                    desc += ", " + decrap(e['school'])
            elif e['type'] == 'unpublished':
                desc += ', unpublished manuscript'
            desc += " [" + e['type'] + "]"
        if 'id' in e:
            k = e['id']
        desc = desc.replace("'", "''").replace("\\", "")
        vim.command("call add(l:candidates,['%s','%s'])" % (k, desc))
