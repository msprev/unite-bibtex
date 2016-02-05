import bibtexparser
import formatter.apalike
from bibtexparser.bparser import BibTexParser
from bibtexparser.customization import *

# logging configuration for bibtexparser to stderr
import logging
import logging.config

logger = logging.getLogger(__name__)

logging.config.dictConfig({
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s %(funcName)s:%(lineno)d: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'formatter': 'standard',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'WARNING',
            'formatter': 'standard',
            'propagate': True
        }
    }
})
# end logging configuration


def parse(filename):
    """
    parse bibtex file and return dictionary of key values as result
    uses a formatter to create Unite text for each entry
    :returns: dicionary
        - key of dictionary item is BibTeX entry key
        - val of dictionary item is text for Unite to display for that entry
        all text in the dictionary, including keys, is unicode
    """
    # 1. parse the file
    entries = list()
    with open(filename) as bibtex_file:
        parser = BibTexParser()
        parser.customization = customizations
        entries = bibtexparser.load(bibtex_file, parser=parser).entries
    # 2. build the Unite text for each entry
    unite_keyvals = dict()
    for e in entries:
        f = getattr(formatter.apalike, e['ENTRYTYPE'], formatter.apalike.default)
        unite_keyvals[unicode(e['ID'])] = f(e)
    return unite_keyvals

def customizations(record):
    """
    custom transformation applied during parsing
    """
    record = convert_to_unicode(record)
    # Split author field from separated by 'and' into a list of "Name, Surname".
    record = author(record)
    # Split editor field from separated by 'and' into a list of "Name, Surname".
    record = editor_split(record)
    return record

def editor_split(record):
    """
    custom transformation
    - split editor field into a list of "Name, Surname"
    :record: dict -- the record
    :returns: dict -- the modified record
    """
    if "editor" in record:
        if record["editor"]:
            record["editor"] = getnames([i.strip() for i in record["editor"].replace('\n', ' ').split(" and ")])
        else:
            del record["editor"]
    return record


