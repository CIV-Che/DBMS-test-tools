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
from   ZODB import FileStorage, DB
from BTrees.OOBTree import OOBTree
from persistent.list import PersistentList
import transaction


# remove old databases
if os.path.exists('posts.fs'):
    [os.remove(i) for i in glob.glob('posts.fs*')]

# setup ZODB storage
storage     = FileStorage.FileStorage('posts.fs')
db          = DB(storage)
connection  = db.open()
db_root     = connection.root()
c_commit    = transaction.commit


f = open('_zodb.ins.btree.t.txt', 'w')
#begin tests
t = time.time()
cnt = 0

db_root['posts'] = OOBTree({0:PersistentList()})
for i1 in xrange(1):
    id1 = time.time()
    db_root['posts'][0].append((id1,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
    c_commit()
    cnt = cnt + 1
    db_root['posts'][id1] = PersistentList()
    for i2 in xrange(10):
        id2 = time.time()
        db_root['posts'][id1].append((id2,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
        c_commit()
        cnt = cnt + 1
        db_root['posts'][id2] = PersistentList()
        for i3 in xrange(10):
            id3 = time.time()
            db_root['posts'][id2].append((id3,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
            c_commit()
            cnt = cnt + 1
            db_root['posts'][id3] = PersistentList()
            for i4 in xrange(10):
                id4 = time.time()
                db_root['posts'][id3].append((id4,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
                c_commit()
                cnt = cnt + 1
                db_root['posts'][id4] = PersistentList()
                for i5 in xrange(10):
                    id5 = time.time()
                    db_root['posts'][id4].append((id5,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
                    c_commit()
                    cnt = cnt + 1
                    db_root['posts'][id5] = PersistentList()
                    for i6 in xrange(10):
                        id6 = time.time()
                        db_root['posts'][id5].append((id6,'John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))
                        c_commit()
                        cnt = cnt + 1

    f.write("%s\n\n" % (time.time() - t))

f.write("rows: %s\n" % cnt)

t = time.time()
db.pack()
f.write("\n\nPackZODB time: %s" % (time.time() - t))
f.write("\n\nZODB size(pack/unpack): %s/%s\n\n" % (os.path.getsize('posts.fs'),os.path.getsize('posts.fs.old')))
f.close()
# closing ZODB database
connection.close()
db.close()
storage.close()
