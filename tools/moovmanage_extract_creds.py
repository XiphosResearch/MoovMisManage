#!/usr/bin/python2
# Coding: utf-9
# Version: 20150215.1
# Author: Darren Martyn
import sqlite3
import sys

# interesting shit that is in all the db's I parsed...
creds = {'Admin Password': 'password',
         'SNMP Community String': 'snmp_ro_community', 
         'Datacard APN': 'datacard_apn', 
         'Datacard Username': 'datacard_username', 
         'Datacard Password': 'datacard_password',
         'Datacard2 APN': 'datacard2_apn', 
         'Datacard2 Username': 'datacard2_username', 
         'Datacard2 Password': 'datacard2_password'}

def main(args):
    # this is all a hideous hack... Because death to sqlite3
    if len(args) != 2:
        sys.exit("%s settings.db" %(args[0])) 
    print "\x1b[1;36m{+}\x1b[0m\x1b[1;35m Parsing Database...\x1b[0m"
    try:
        con = sqlite3.connect(args[1])
        c = con.cursor()
        c.execute("SELECT * from setting")
    except Exception, e:
        print "\x1b[1;31m{!}\x1b[0m\x1b[1;31m Error hit! Printing trace...\x1b[0m"
        print e
        sys.exit(0)
    for cred in creds:
        c.execute("SELECT * from setting")
        for row in c.fetchall():
            if str(row[0]) == str(creds[cred]):
                print "\x1b[1;34m{*}\x1b[0m\x1b[1;31m %s:\x1b[0m \x1b[1;32m%s\x1b[0m" %(cred, row[1])
    print "\x1b[1;36m{+}\x1b[0m\x1b[1;35m Parsing Complete!\x1b[0m"

if __name__ == "__main__":
    main(args=sys.argv)
