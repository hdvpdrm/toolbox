#!/usr/bin/python3
#ChangeCase - script changes case to lower/upper for specified files in directory
import os
import sys


os.chdir(os.getcwd()) #move to directory where script is invoked

#chc takes at least 1 file and option
if len(sys.argv) < 2:
    print("chc error: not enough arguments! see toolbox -i chc for help!")
    sys.exit(-1)

key = [x for x in sys.argv if x.startswith("!")]
files = [x for x in sys.argv[1:] if not x.startswith("!")]

#there should be a key
if len(key) != 1: 
    print("chc error: incorrect arguments! see toolbox -i chc for help!")
    sys.exit(-1)
    
key = key[0]
if key not in ("!lower","!upper"):
    print("chc error: {} is incorrect key!".format(key))
    sys.exit(-1)

def rename(x):
    if key == "!lower":
        return x.lower()
    return x.upper()

for f in files:
    if os.path.exists(f):
        renamed = function(f)
        os.rename(f,rename(f))
    else:
        print("chc warning: {} doesn't exist!".format(f))
