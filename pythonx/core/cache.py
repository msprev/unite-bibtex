class cache(object):

    """Docstring for cache. """

    def __init__(self, bib_file, cache_dir):
        """@todo: to be defined1. """
        self.unite_keyvals = dict()
        self.timestamp = None
        self.bib_file = bib_file
        self.cache_filename = str() # create it here

    def read():
        """@todo: Docstring for read.

        :filename: @todo
        :returns: @todo

        """
        pass

    def write(unite_keyvals):
        """@todo: Docstring for write.

        :filename: @todo
        :returns: @todo

        """
        pass

    def get_timestamp(filename):
        """@todo: Docstring for get_timestamp.

        :filename: @todo
        :returns: @todo

        """
        pass

def update_current_timestamp():
    time_stamp = os.path.getmtime(vim.eval('g:unite_bibtex_bib_file'))
    vim.command('let l:current_timestamp = %s' % time_stamp)

