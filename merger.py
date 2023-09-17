#merger.py
#This script is dedicated to match 2 directories and find files with the same names
#if they are the same, script asks user should they be merged and if user is agree
#then script merges two files


import os
import sys
import hashlib
import itertools

def get_all_files(dir):
    '''get all files in directory tree'''
    files = list()
    for root, _, f in os.walk(dir):
        files = files + list(map(lambda n:(root,n),f))
    return files

def match_same_files(dir1,dir2):
    '''return iter with matched file'''
    return ((name1,name2) for name1, name2 in itertools.product(dir1,dir2) if name1[1] == name2[1])

#check arguments
if len(sys.argv) != 3 and len(sys.argv) != 4:
    print("incorrect number of arguments!")
    print("example: merger dir1 dir2")
    print("example: merger dir1 dir2 wd")

dir1, dir2 = sys.argv[1],sys.argv[2]
whole_directory_tree = False

if len(sys.argv) == 4:
    if sys.argv[3] == "wd":
        whole_directory = True
    else:
        print("unknown argument {} script won't walk through whole directory!".format(sys.argv[3]))

dir1_elements, dir2_elements = None, None

if whole_directory_tree:
    dir1_elements = get_all_files(dir1)
    dir2_elements = get_all_files(dir2)
else:
    dir1_elements = os.listdir(dir1)
    dir1_elements = list(map(lambda f:(dir1,f),dir1_elements))
    
    dir2_elements = os.listdir(dir2)
    dir2_elements = list(map(lambda f:(dir2,f),dir2_elements))


def get_input(prompt):
    answer = input(prompt+"(Y/n):")
    if answer == "Y":
        return True
    elif answer == "n":
        return False
    else:
        get_input(prompt)

#rewrite files if user wants to do it
for f in match_same_files(dir1_elements,dir2_elements):
    left, right = f
    left_path = left[0]+"/"+left[1]
    right_path = right[0]+"/"+right[1]

    if get_input("do you want to rewrite {} with {}?".format(right_path,left_path)):
        with open(left_path,"rb") as left_file:
            with open(right_path,"wb") as right_file:
                right_file.write(left_file.read())


