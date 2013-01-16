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

f = open('mysql.read.1111110.00.txt', 'w')
#begin tests
t = time.time()

cursor.execute("SELECT * FROM post WHERE parent='%010.6f'" % 0)
posts1 = cursor.fetchall()
for post1 in posts1:
    post = post1
    cursor.execute("SELECT * FROM post WHERE parent='%s'" % post1[0])
    posts2 = cursor.fetchall()
    for post2 in posts2:
        post = post2
        cursor.execute("SELECT * FROM post WHERE parent='%s'" % post2[0])
        posts3 = cursor.fetchall()
        for post3 in posts3:
            post = post3
            cursor.execute("SELECT * FROM post WHERE parent='%s'" % post3[0])
            posts4 = cursor.fetchall()
            for post4 in posts4:
                post = post4
                cursor.execute("SELECT * FROM post WHERE parent='%s'" % post4[0])
                posts5 = cursor.fetchall()
                for post5 in posts5:
                    post = post5
                    cursor.execute("SELECT * FROM post WHERE parent='%s'" % post5[0])
                    posts6 = cursor.fetchall()
                    for post6 in posts6:
                        post = post6

f.write("%s\n" % (time.time() - t))

f.close()
# closing MySQL database
db.close()

