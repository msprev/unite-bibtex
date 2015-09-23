import bibtex
import cache
import error

def candidates(cache_dir, bib_files):
    """
    :cache_dir: directory where cache files kept
    :bib_files: list of bib files to read
    :returns: data structure that Unite wants for its list of candidates
    """
    # 1. Sanity check:
    # if bib_files incorrectly set to string, add single bib file to list
    if type(bib_files) is str:
        bib_files = [bib_files]
    # 2. Gather the candidates into unite_keyvals and use cache
    # format of unite_keyvals:
    #   { bibtex-key: text-in-unite-list }
    unite_keyvals = dict()
    for bib in bib_files:
        unite_keyvals.update(bibtex.parse(bib))
        # cache = cache.Cache(bib, cache_dir)
        # try:
        #     cache.read()
        # except (error.NoCache, error.OutdatedCache):
        #     cache.unite_keyvals = bibtex.parse(bib)
        #     cache.write()
        # unite_keyvals.update(cache.unite_keyvals)
    # 3. Create Unite data structure
    # sort items based on bibtex key, case-insensitive
    gathered = [{'action__text': '@' + bibtex_key, 'word': text}
                for bibtex_key, text in
                sorted(unite_keyvals.viewitems(), key=lambda x: x[0].lower())]
    return gathered
