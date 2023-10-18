#!/usr/bin/python3

#MAKEITFLAT##
#############
#This script is dedicated to convert nested directory system(or it can be called dir tree)
#into the primitive linear structure of files in the top directory where this scripted
#was invoked.
import os
import functools
import shutil

#get all dirs
dirs = list(filter(os.path.isdir,os.listdir(os.getcwd())))

_files = []
def get_files(directory):
    global _files
    
    for root,dirs, files in os.walk(directory):
        #iterate over current dir
        for filename in files:
            if filename in _files:
                break
            _files.append(os.path.join(root,filename))

    return list(set(_files))

# unite all files data and move to the top directory
files = functools.reduce(lambda a,b:a+b, list(map(get_files,dirs)))


duplicate_counter = 0 #two subdirectories can have two files with the same names
for f in files:
    #do all only if file exists
    if os.path.exists(f):
        head, tail = os.path.split(f)
        file_path = os.path.join(os.getcwd(),tail)#place where file will be placed

        #so if there are already the same file,then rename it
        if(os.path.exists(file_path)):
            new_name = os.path.join(head,str(duplicate_counter)+tail)
            os.rename(os.path.join(head,tail),new_name)
            duplicate_counter = duplicate_counter + 1
            shutil.move(new_name,os.getcwd())
        else:
            shutil.move(f,os.getcwd())

#delete empty directories
for d in dirs:
    shutil.rmtree(d)
