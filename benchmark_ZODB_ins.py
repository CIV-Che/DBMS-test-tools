#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
This script for measure work timings (benchmarking)
any number of CMS backends (data storage) as
MySQL, MongoDB, ZODB (3.9.7).
"""

__author__ = 'Cheltsov Ivan (civ@ploha.ru)'
__copyright__ = 'Copyright 2012, Cheltsov Ivan'
__version__ = '0.1.0'
__license__ = 'LGPL'


import time, os, glob
import ZODB
from   ZODB import FileStorage, DB
from   persistent.list import PersistentList


# remove old databases
if os.path.exists('testdb.fs'):
    [os.remove(i) for i in glob.glob('testdb.fs*')]

# setup ZODB storage
dbpath      = 'testdb.fs'
storage     = FileStorage.FileStorage(dbpath)
db          = DB(storage)
connection  = db.open()
dbroot      = connection.root()
c_commit    = connection.transaction_manager.commit

f = open('zodb.ins.1111110.00.txt', 'w')
#begin tests
t = time.time()

for i1 in xrange(10):
    comment = PersistentList()
    post = PersistentList(['John Doe',time.time(),
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        comment])
    dbroot[i1] = post
    c_commit()
    for i2 in xrange(10):
        comment = PersistentList()
        post = PersistentList(['John Doe',time.time(),
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            comment])
        dbroot[i1][3].append(post)
        c_commit()
        for i3 in xrange(10):
            comment = PersistentList()
            post = PersistentList(['John Doe',time.time(),
                'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                comment])
            dbroot[i1][3][i2][3].append(post)
            c_commit()
            for i4 in xrange(10):
                comment = PersistentList()
                post = PersistentList(['John Doe',time.time(),
                    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                    comment])
                dbroot[i1][3][i2][3][i3][3].append(post)
                c_commit()
                for i5 in xrange(10):
                    comment = PersistentList()
                    post = PersistentList(['John Doe',time.time(),
                        'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                        comment])
                    dbroot[i1][3][i2][3][i3][3][i4][3].append(post)
                    c_commit()
                    for i6 in xrange(10):
                        comment = PersistentList()
                        post = PersistentList(['John Doe',time.time(),
                            'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
                            comment])
                        dbroot[i1][3][i2][3][i3][3][i4][3][i5][3].append(post)
                        c_commit()

    f.write("%s\n" % (time.time() - t))

t = time.time()
db.pack()
f.write("\n\nPackZODB time: %s" % (time.time() - t))
f.close()
# closing ZODB database
connection.close()
db.close()

