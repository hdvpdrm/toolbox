import os
import itertools
import sys

def check_root(root):
    '''check if we should avoid directory'''
    for a in sys.argv[1:]:
        if a in root:
            return False
    return True
def get_new_name(name,counter):
    '''get new name to rename'''
    if "." in name:
        s = name.split(".")
        return "{}{}.{}/".format(s[0],counter,s[1])
    else:
        return name+str(counter)

saved =[]
duplicate_counter = 0
for root, dirs, files in os.walk(os.getcwd()):
    for filename in files:
        if filename in saved and check_root(root):
            a = root+"/"+filename
            b = root+"/"+get_new_name(filename,duplicate_counter
            os.rename(a,b))
            print("{} -> {}".format(a,b))
            duplicate_counter = duplicate_counter + 1
        else:
            saved.append(filename)
