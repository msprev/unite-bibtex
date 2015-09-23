class NoCache(Exception):
    """ no cache file found """
    pass

class OutdatedCache(Exception):
    """ cache is out of date """
    pass
