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
#import ZODB
from   ZODB import FileStorage, DB
from BTrees.OOBTree import OOBTree


# setup ZODB storage
storage     = FileStorage.FileStorage('posts.fs')
db          = DB(storage)
connection  = db.open()
db_root     = connection.root()
#c_commit    = connection.transaction_manager.commit


f = open('_zodb.read.btree.t.txt', 'w')
#begin tests
t = time.time()
cnt = 0

for p1 in db_root['posts'][0]:
    post = p1
    cnt = cnt + 1
    for p2 in db_root['posts'][p1[0]]:
        post = p2
        cnt = cnt + 1
        for p3 in db_root['posts'][p2[0]]:
            post = p3
            cnt = cnt + 1
            for p4 in db_root['posts'][p3[0]]:
                post = p4
                cnt = cnt + 1
                for p5 in db_root['posts'][p4[0]]:
                    post = p5
                    cnt = cnt + 1
                    for p6 in db_root['posts'][p5[0]]:
                        post = p6
                        cnt = cnt + 1

f.write("%s\n\n" % (time.time() - t))
f.write("rows:%s\n\n" % cnt)


f.close()
# closing ZODB database
connection.close()
db.close()
storage.close()
