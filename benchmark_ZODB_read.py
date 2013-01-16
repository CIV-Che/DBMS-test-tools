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


# setup ZODB storage
dbpath      = 'testdb.fs'
storage     = FileStorage.FileStorage(dbpath)
db          = DB(storage)
connection  = db.open()
dbroot      = connection.root()

f = open('zodb.read.1111110.00.txt', 'w')
#begin tests
t = time.time()

for i in xrange(10):
    postt = dbroot[i]
    post = (postt[0],postt[1],postt[2],0)
    for post2 in postt[3]:
        post = (post2[0],post2[1],post2[2],postt[0])
        for post3 in post2[3]:
            post = (post3[0],post3[1],post3[2],postt[0],post2[0])
            for post4 in post3[3]:
                post = (post4[0],post4[1],post4[2],postt[0],post2[0],post3[0])
                for post5 in post4[3]:
                    post = (post5[0],post5[1],post5[2],postt[0],post2[0],post3[0],post4[0])
                    for post6 in post5[3]:
                        post = (post6[0],post6[1],post6[2],postt[0],post2[0],post3[0],post4[0],post5[0])

f.write("%s\n" % (time.time() - t))

f.close()
# closing ZODB database
connection.close()
db.close()

