#!/usr/bin/python

from __future__ import print_function

hostname = '41.89.56.131'
username = 'root'
password = ''
database = 'default'

# Simple routine to run a query on a database and print the results:
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT fname, lname FROM employee" )

    for firstname, lastname in cur.fetchall() :
        print( firstname, lastname )


print( "Using psycopg2:" )
import psycopg2
myConnection = psycopg2.connect( host=hostname, user=username, password=password )
print(myConnection)
doQuery( myConnection )
myConnection.close()
