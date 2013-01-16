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


import MySQLdb
import time

# setup MySQL storage
db=MySQLdb.connect(host="localhost", user="user", passwd="password", charset='utf8', db="test")
cursor = db.cursor()
# remove old database
cursor.execute("DROP DATABASE test")
cursor.execute("CREATE DATABASE test")
db=MySQLdb.connect(host="localhost", user="user", passwd="password", charset='utf8', db="test")
cursor = db.cursor()

cursor.execute("CREATE TABLE post(id varchar(17), name varchar(64), post text, parent varchar(17));")
cursor.execute("CREATE INDEX parent on post(parent);")

f = open('mysql.ins.1111110.00.txt', 'w')
#begin tests
t = time.time()

for i1 in xrange(1):
    id1 = time.time()
    cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id1,0))
    db.commit()
    for i2 in xrange(10):
        id2 = time.time()
        cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id2,id1))
        db.commit()
        for i3 in xrange(10):
            id3 = time.time()
            cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id3,id2))
            db.commit()
            for i4 in xrange(10):
          id4 = time.time()
    		cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id4,id3))
	        db.commit()
                for i5 in xrange(10):
		    id5 = time.time()
		    cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id5,id4))
		    db.commit()
                    for i6 in xrange(10):
			id6 = time.time()
			cursor.execute("INSERT INTO post VALUES ('%010.6f','John Doe','Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.','%010.6f');" % (id6,id5))
			db.commit()

    f.write("%s\n" % (time.time() - t))

f.close()
# closing MySQL database
db.close()

