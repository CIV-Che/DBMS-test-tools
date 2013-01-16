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
from pymongo import ASCENDING, DESCENDING
import time

# setup MongoDB storage
connection = Connection("mongodb://localhost",safe=False,auto_start_request=True)
connection.drop_database("posts") # remove old database
db=connection.posts
db.posts.create_index([('parent', DESCENDING)])


f = open('mongo.ins.1111110.00.txt', 'w')
#begin tests
t = time.time()

for i1 in xrange(10):
    id1 = time.time()
    db.posts.insert({'date':id1,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':0})
    for i2 in xrange(10):
        id2 = time.time()
        db.posts.insert({'date':id2,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':id1})
        for i3 in xrange(10):
            id3 = time.time()
            db.posts.insert({'date':id3,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':id2})
            for i4 in xrange(10):
                id4 = time.time()
                db.posts.insert({'date':id4,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':id3})
                for i5 in xrange(10):
                    id5 = time.time()
                    db.posts.insert({'date':id5,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':id4})
                    for i6 in xrange(10):
                        id6 = time.time()
                        db.posts.insert({'date':id6,'name':'John Doe','post':'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','parent':id5})

    f.write("%s\n" % (time.time() - t))

f.close()
# closing Mongo database
connection.close()
