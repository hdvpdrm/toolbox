#!/usr/bin/python3
#gtcn.py - Get Table Column Name
#This script is created to open database and view column names for each passed table.
#It depends on file core util to check whether passed file is sqlite3 database or not.
import sqlite3
import sys
from functools import reduce
from subprocess import PIPE, run

#script takes database and list of tables.
if len(sys.argv) <= 2:
    print("gtcm usage: python gtcm.py database.sqlite table1 [table2 ... tableN]")
    sys.exit(1)


def get_column_names(table,conn):
    try:
        cursor = conn.execute("SELECT * FROM {}".format(table))
        names = [desc[0] for desc in cursor.description]
        return reduce(lambda a,b:a+" "+b,names)
    except Exception as e:
        print("gtcm error: unable to reach '{}' table".format(table))
        return ""

command = ["file", sys.argv[1]]
try:
    result = run(command, stdout=PIPE, universal_newlines=True)
except FileNotFoundError as e:
    print("gtcm error: unable to run 'file' command")
    sys.exit(1)

if result.returncode == 0:
    result = result.stdout.split()[:4]
    if result[1] == 'SQLite' and result[3] == 'database,':
        conn = sqlite3.connect(sys.argv[1])
        for table_name in sys.argv[2:]:
            result = get_column_names(table_name,conn)
            if result != "": print(table_name,":",result)
    else:
        print("gtcm error: {} is not sqlite3 database".format(sys.argv[1]))
else:
    print("gtcm error: file's return code is {}".format(result.returncode))
    sys.exit(1)



