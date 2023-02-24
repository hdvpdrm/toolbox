import os
import sys
import shutil

def get_args(arg_type):
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
    else:
        print("{} directory already exists!".format(a[0]))
        args.pop(id)
    id = id+ 1

#find required files
sorted_paths = {}
for a in args:
    n = a[0]
    file_types = a[1]
    sorted_paths[n] = []
    
    for root, dirs, files in os.walk(os.getcwd()):
        for f in files:
            _, ext = os.path.splitext(f)
            if ext != "" and ext in file_types:
                sorted_paths[n].append(os.path.join(root,f))


#move found to their required places
for k in sorted_paths.keys():
    dest = os.getcwd()+"/"+k
    for p in sorted_paths[k]:
        try:
            shutil.move(p,dest)
        except Exeception as err:
            print("{}".format(err))
                
