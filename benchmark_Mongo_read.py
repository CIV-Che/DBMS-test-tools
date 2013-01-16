#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""
This script for measure work timings (benchmarking)
any number of CMS backends (data storage) as
MySQL (5.5.28), MongoDB, ZODB (3.9.7).
"""

__author__ = 'Cheltsov Ivan (civ@ploha.ru)'
__copyright__ = 'Copyright 2012, Cheltsov Ivan'
__version__ = '0.1.0'
__license__ = 'LGPL'


from pymongo import Connection
import time

# setup MongoDB storage
connection = Connection("mongodb://localhost",safe=False,auto_start_request=True)
db=connection.posts


f = open('mongo.read.1111110.00.txt', 'w')
#begin tests
t = time.time()

for post1 in db.posts.find({'parent':0}):
    post = post1.values()
    for post2 in db.posts.find({'parent':post1['parent']}):
        post = post2.values()
        for post3 in db.posts.find({'parent':post2['parent']}):
            post = post3.values()
            for post4 in db.posts.find({'parent':post3['parent']}):
                post = post4.values()
                for post5 in db.posts.find({'parent':post4['parent']}):
                    post = post5.values()
                    for post6 in db.posts.find({'parent':post5['parent']}):
                        post = post6.values()

f.write("%s\n" % (time.time() - t))

f.close()
# closing Mongo database
connection.close()
