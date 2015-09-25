#!/usr/bin/env python
""" bibwatch: watch for changes to bibtex files and update Unite bibtex cache

Author    : Mark Sprevak <mark.sprevak@ed.ac.uk>
Copyright : Copyright 2015, Mark Sprevak
License   : BSD3
"""
import argparse
import bibtex
import cache
import datetime
import os
import sys
import time

VERSION = "0.1"
SLEEP_TIME = 1

DESCRIPTION = '''
bibwatch: watch for changes to BibTeX files and update their Unite BibTeX cache
'''

EPILOG = '''
Copyright (C) 2015 Mark Sprevak
Web:  http://sites.google.com/site/msprevak
This is free software; see the source for copying conditions. There is no
warranty, not even for merchantability or fitness for a particular purpose.
'''

def main():
    # initialise dictionaries
    c = dict()
    mtime_last = dict()
    mtime_cur = dict()
    # read command line arguments
    cli_args = parse_cli()
    bib_files = cli_args['input']
    cache_dir = cli_args['cache']
    if not bib_files:
        print('No BibTeX files listed on command line to monitor')
        exit(1)
    if not cache_dir:
        print('No cache directory specified on command line')
        exit(2)
    # check if cache is up to date
    for b in bib_files:
        print('monitoring: "%s"' % b)
        c[b] = cache.Cache(b, cache_dir)
        mtime_last[b] = 0
        try:
            c[b].read()
            mtime_last[b] = c[b].timestamp
        except (cache.NoCache, cache.OutdatedCache):
            mtime_last[b] = 0
    print('cache directory: "%s"' % cache_dir)
    print('(press Control+C to stop monitoring)')
    # monitor for changes
    try:
        while True:
            for b in bib_files:
                mtime_cur[b] = os.path.getmtime(b)
                if mtime_cur[b] != mtime_last[b]:
                    update(c[b])
                mtime_last[b] = mtime_cur[b]
                time.sleep(SLEEP_TIME)
    except KeyboardInterrupt:
        print('\nStopped')

def update(c):
    today = datetime.date.today().isoformat()
    now = datetime.datetime.now().time().isoformat()
    print(today + ' ' + now)
    print('    updating cache for "%s"' % c.source_path)
    start_time = time.time()
    c.update(bibtex.parse)
    c.write()
    elapsed_time = time.time() - start_time
    time_report = 'time taken: %s (%f seconds)' % (str(datetime.timedelta(seconds=elapsed_time)), elapsed_time)
    print('    written "%s"' % c.cache_path)
    print('-- done (%s)' % time_report)

def parse_cli():
    p = argparse.ArgumentParser(
        description=DESCRIPTION,
        epilog=EPILOG,
        formatter_class=argparse.RawTextHelpFormatter,
        add_help=False)
    p.add_argument('input', nargs='*',
                   help="BibTeX files to monitor for changes")
    p.add_argument("-h", "--help", '---help', '---h',
                   action="help",
                   help="show this help message and exit")
    p.add_argument('-v', '--version', '---version', '---v',
                   action='version',
                   version=('%(prog)s ' + VERSION))
    p.add_argument("--cache", '-c',
                    help='cache directory to write cached files')
    known_raw, unknown = p.parse_known_args()
    known = vars(known_raw)
    return known

if __name__ == '__main__':
    main()

