#!/usr/bin/python3

#srm - safe rm or safe removing script
#since deleted files can be recovered, this script rewrites file
#with noise and then delete it with standard tool of current OS

import sys
import secrets
import os

if len(sys.argv) < 2:
    print("not enough arguments!")
    print("example:python srm.py file_to_erase optional_rewriting_times_number")
    exit(-1)

try:
    #get all required data - file to fill with random noise and then erase, number that shows how much time script should write noise
    with open(sys.argv[1],"rb") as f:
        bytes = f.read()
        bytes_len = len(bytes)
    
    rewriting_times_number = 5 if len(sys.argv) < 3 else int(sys.argv[2]) # default value is 5
    for _ in range(0,rewriting_times_number):
        with open(sys.argv[1],"wb") as f:
            f.write(secrets.token_bytes(bytes_len))
except Exception as e:
    print("unable to open {}".format(sys.argv[1]))
    print(str(e))

#erase file that can't be recovered
if os.name == 'nt':
    os.system("erase /f /q {}".format(sys.argv[1]))
elif os.name == "posix":
    os.system("rm -rf {}".format(sys.argv[1]))
else:
    print("sorry! script can't recognize your OS!")
