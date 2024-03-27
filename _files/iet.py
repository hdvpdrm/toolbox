#!/usr/bin/python3
#IgnoreEmacsTilde files(something like blabla.h~ blabla.c~)

from os import listdir, getcwd
from os.path import isfile, join

onlyfiles = [f for f in listdir(getcwd()) if isfile(join(getcwd(), f))]


try:
    with open(".gitignore","a") as ig:
        for f in onlyfiles:
            if f.endswith("~"): ig.write(f+"\n")
except Exception as e:
    print("failed to open .gitignore:",str(e))
