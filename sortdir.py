#!/usr/bin/python3

import os
import sys
import shutil

work_with_cwd = True
def get_args(arg_type):
    if arg_type == "-wd":#whole directory tree
        global work_with_cdw
        work_with_cwd = False
    if "=" in arg_type:
        name, args = arg_type.split("=")
        args = args.split(",") if "," in args else args
        return (name,args)
    else:
        return []

args = list(map(get_args,sys.argv[1:]))

#create directories, mentioned in arguments
id = 0
for a in args:
    if not os.path.exists(a[0]):
        os.makedirs(a[0])
    id = id+ 1



def process_file(fl,ext):
    if ext != "" and ext in file_types:
        sorted_paths[n].append(fl) 
def walk_through_all_dirs(sorted_paths):
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            _, ext = os.path.splitext(f)
            process_file(os.path.join(root,f),ext)

def walk_through_curr_dir(sorted_paths):
    for fl in os.listdir(os.getcwd()):
        _, ext = os.path.splitext(fl)
        process_file(fl,ext)
#find required files
sorted_paths = {}
for a in args:
    n = a[0]
    file_types = a[1]
    sorted_paths[n] = []

    if not work_with_cwd:
        walk_through_all_dirs(sorted_paths)
    else:
        walk_through_curr_dir(sorted_paths)



#move found to their required places
for k in sorted_paths.keys():
    dest = os.getcwd()+"/"+k
    for p in sorted_paths[k]:
        try:
            shutil.move(p,dest)
        except Exception as err:
            print("{}".format(err))
                
