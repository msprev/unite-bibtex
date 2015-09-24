import base64
import json
import os
import time

SLEEP_TIME = 0.1

class Cache(object):
    """
    Cache data on disk.
    Will cache data in some source file transformed by some arbitrary function.
    Methods for reading, writing and updating cache.
    """

    def __init__(self, source, cache_dir):
        """
        Setting initialised cache
        :source: source file data to cache
        :cache_dir: directory in which to place cache file
        """
        # sanity check 1: source file exists
        if not os.path.isfile(source):
            raise MissingSource
        # sanity check 2: cache directory exists
        if not os.path.exists(cache_dir):
            raise MissingCacheDir
        # blank cache has no timestamp and empty data
        self.timestamp = None
        self.data = dict()
        # set up names of cache and lock file
        self.source_path = os.path.abspath(source)
        cache_name = base64.urlsafe_b64encode(self.source_path) + '.cache'
        lock_name = base64.urlsafe_b64encode(self.source_path) + '.lock'
        cache_path = os.path.abspath(cache_dir)
        self.cache_path = os.path.join(cache_path, cache_name)
        self.lock_path = os.path.join(cache_path, lock_name)

    def read(self):
        """
        Read data in cache file, and update self.data
        Raises NoCache if cache file does not exist
        Raises OutdatedCache if cache file modified date != that of source file
        """

        if not os.path.isfile(self.cache_path):
            raise NoCache
        while self.islocked():
            time.sleep(SLEEP_TIME)
        # lock!
        self.lock()
        # read the cache
        try:
            with open(self.cache_path, 'r') as fp:
                on_disk = json.load(fp)
                self.timestamp = on_disk[0]
                self.data = on_disk[1]
        # alway sunlock!
        finally:
            self.unlock()
        # check if cache is out of date
        if self.timestamp != os.path.getmtime(self.source_path):
            raise OutdatedCache

    def update(self, update_fun):
        """
        Freshen the cache
        Read source data and store transform of it by arbitrary function
        :update_fun: function to apply to source file data
        """
        self.data = update_fun(self.source_path)
        self.timestamp = os.path.getmtime(self.source_path)

    def write(self):
        """
        Write data to cache file
        """
        # sanity check 1: don't write an unfilled cache
        if not self.timestamp:
            raise WriteUnfilledCache
        while self.islocked():
            time.sleep(SLEEP_TIME)
        # lock!
        self.lock()
        # write the cache
        try:
            with open(self.cache_path, 'w') as fp:
                json.dump([self.timestamp, self.data], fp)
                fp.flush()
        # always unlock!
        finally:
            self.unlock()

    def lock(self):
        """
        lock cache file from read/writes of other processes
        """
        if self.islocked():
            raise AttemptedLockingLocked
        open(self.lock_path, 'a').close()

    def unlock(self):
        """
        unlock cache file to read/writes of other processes
        """
        if not self.islocked():
            raise AttemptedUnlockingUnlocked
        os.remove(self.lock_path)

    def islocked(self):
        """
        test if cache file is lock
        :returns: True if locked, otherwise False
        """
        if os.path.isfile(self.lock_path):
            return True
        return False

# Exceptions raised by cache

class NoCache(Exception):
    """ no cache file found """
    pass

class OutdatedCache(Exception):
    """ cache is out of date """
    pass

class MissingSource(Exception):
    """ source file cannot be found """
    pass

class MissingCacheDir(Exception):
    """ cache dictory cannot be found """
    pass

class AttemptedLockingLocked(Exception):
    """ attempt to lock an already locked cache """
    pass

class AttemptedUnlockingUnlocked(Exception):
    """ attempt to unlock an already unlocked cache """
    pass

class WriteUnfilledCache(Exception):
    """ attempt to write an unfilled cache """
    pass



