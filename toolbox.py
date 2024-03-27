import os
import sys
import tomllib
import argparse
import subprocess

def gtd():
    return os.path.abspath(os.path.dirname(__file__))
def get_all_dirs():
    not_magic = lambda x: x not in ("__init__.py","__main__.py")
    not_tilde = lambda x: not x.endswith("~")#it is very annoying shit from emacs
    return (x for x in os.listdir(gtd()) if x.startswith("_") and not_magic(x) and not_tilde(x))
def get_scripts():
    '''returns dict, where key is category(browser,files,sql,e.t.c) and value is generator of related scripts docs'''
    get_scripts = lambda d: (d+"/"+x for x in os.listdir(gtd()+"/"+d) if x.endswith(".toml"))

    scripts = {}
    for d in get_all_dirs():
        scripts[d] = get_scripts(d)
    return scripts

def associate_script_by_dir():
    d = {}
    for dir in get_all_dirs():
        for script in (x for x in os.listdir(gtd()+"/"+dir) if x.endswith(".py")):
            d[script] = dir
    return d

def read_single_script_info(script_path):
    with open(gtd()+"/"+script_path,"rb") as f:
        info =  tomllib.load(f)
        return (info["script"],dict([x for x in info.items() if "script" not in x]))
    
def read_scripts_annotations():
    scripts  = {}
    for category, gen in get_scripts().items():
        for script in gen:
            script_name, otherdata = read_single_script_info(script)
            scripts[script_name] = otherdata
    return scripts

def parse_args():
    parser = argparse.ArgumentParser(prog="toolbox",description="script to manage/invoke different system script of this package")
    parser.add_argument("-l","--list"   , help="list all available scripts",action="count")
    parser.add_argument("-i","--inspect", help="read detailed information about provided script")
    parser.add_argument("-e","--execute", help="execute existing script",nargs="*", type=str)
    return  parser.parse_args()

def does_script_exist(script,scripts):
    return script in scripts

def show_all_scripts(annotations,arg):
    keys    = [key for key in annotations.keys()]
    max_len = max(len(k) for k in keys)
    pd = lambda a,b,diff:print(a," "+" "*diff," --- ",b,sep="")
    for k in keys:
        diff = max_len - len(k)
        desc = annotations[k]["desc"]
        pd(k,desc,diff)


def inspect(annotations,arg):
    if not does_script_exist(arg,annotations.keys()):
        print("toolbox: error: script doesn't exist :{}".format(arg))
        sys.exit(1)

    for i, pair in enumerate(annotations[arg]["examples"]):
        example, annot = pair
        print("#{} - {}".format(i,example))
        print(annot+"\n")
        
def execute(annotations,arg):
    arg[0] = arg[0]+".py"
    scripts = associate_script_by_dir()
    dir = scripts[arg[0]]
    arg[0] = gtd()+"/"+dir+"/"+arg[0]
    try:
        subprocess.run(arg)
    except Exception as e:
        print("toolbox error: failed to execute subprocess!")
        print(str(e))
    
        
            
def invoke(annotations):
    commands = {
        "list":show_all_scripts,
        "inspect":inspect,
        "execute":execute
        }
    
    args = vars(parse_args())
    for key, val in args.items():
        if val is not None:
            commands[key](annotations, val)
    


