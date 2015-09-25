import os
import bibtexparser
# import format.apalike
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

def parse(filename):
    entries = list()
    unite_keyvals = dict()
    with open(filename) as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        entries = bibtexparser.load(bibtex_file, parser=parser).entries
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
            desc += " '" + decrap(e['title']) + "'"
        # now, the per-type stuff...
        if e['ENTRYTYPE'] == 'article':
            if 'journal' in e:
                desc += ", " + decrap(e['journal'])
                if 'volume' in e:
                    desc += ', ' + e['volume']
                if 'pages' in e:
                    desc += ', pp. ' + e['pages']
        elif e['ENTRYTYPE'] == 'incollection' or e['ENTRYTYPE'] == 'inproceedings':
            if 'crossref' in e:
                ps = [x for x in entries if x['ID'] == e['crossref']]
                if ps:
                    p = ps[0]
                    if 'editor' in p or 'booktitle' in p:
                        desc += ' in'
                    if 'editor' in p:
                        desc += " %s (Ed.)" % add_names(p['editor'], 4)
                    if 'booktitle' in p:
                        desc += " '" + decrap(p['booktitle']) + "'"
            else:
                if 'editor' in e or 'booktitle' in e:
                    desc += ' in'
                if 'editor' in e:
                    desc += " %s (Ed.)" % add_names(e['editor'], 4)
                if 'booktitle' in e:
                    desc += " '" + decrap(e['booktitle']) + "'"
        elif e['ENTRYTYPE'] == 'book':
            if 'address' in e:
                desc += ", " + decrap(e['address'])
            if 'publisher' in e:
                desc += ": " + decrap(e['publisher'])
        elif e['ENTRYTYPE'] == 'mastersthesis' or e['ENTRYTYPE'] == 'phdthesis':
            if 'school' in e:
                desc += ", " + decrap(e['school'])
        elif e['ENTRYTYPE'] == 'unpublished':
            desc += ', unpublished manuscript'
        if 'ID' in e:
            desc += ' ' + "@" + e['ID']
        desc += " [" + e['ENTRYTYPE'] + "]"
        if 'ID' in e:
            k = unicode(e['ID'])
        desc = desc.replace("\\", "").replace("--", "-")
        unite_keyvals[k] = desc
    return unite_keyvals

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

