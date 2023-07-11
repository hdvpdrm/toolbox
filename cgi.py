import sys
import os

files_to_ignore, dirs_to_ignore = [], []
check_files, check_dirs = False, False
check_only_this_directory = True

#process args and sort them by categories
for arg in sys.argv[1:]:
    if "-" in arg:
        if "-f" == arg:
            check_files = True
            check_dirs = False
        elif "-d" == arg:
            check_files = False
            check_dirs = True
        elif "-wd" == arg:
            check_only_this_directory = False#script will iterate over all directory tree
        else:
            print("unknown argument {}".format(arg))
            exit(-1)
        continue#skip this special argument to check next ones

    if check_files:
        files_to_ignore.append(arg)
    if check_dirs:
        dirs_to_ignore.append(arg)

#if there are empty files and dirs, then break script running
if not check_files and not check_dirs:
    print("you didn't specified file types and directories to ignore!")
    print("example: cgi -f .sln .txt -d Release")
    exit(-1)

def process_file(f):
    _, ext = os.path.splitext(f)
    with open(".gitignore","a") as f:
        if ext in files_to_ignore:
            f.write("*{}\n".format(ext))
def process_dir(d):
    with open(".gitignore","a") as f:
        if d in dirs_to_ignore:
            f.write("{}/\n".format(d))
        
if not check_only_this_directory:
    for _, dirs, files in os.walk(os.getcwd()):
        for f in files:
            process_file(f)
        for d in dirs:
            process_dir(d)
else:
    for f in os.listdir(os.getcwd()):
        if os.path.isfile(f):
            process_file(f)
        else:
            process_dir(f)
            

system("echo .gitignore >> .gitignore")
