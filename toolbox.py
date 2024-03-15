import os
import sys
import tomllib
import argparse


def get_scripts():
    '''returns dict, where key is category(browser,files,sql,e.t.c) and value is generator of related scripts docs'''
    all_script_dirs = (x for x in os.listdir() if x.startswith("_"))
    get_scripts = lambda d: (d+"/"+x for x in os.listdir(d) if x.endswith(".toml"))

    scripts = {}
    for d in all_script_dirs:
        scripts[d] = get_scripts(d)
    return scripts


def read_single_script_info(script_path):
    with open(script_path,"rb") as f:
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
    parser.add_argument("-e","--execute", help="execute existing script",nargs="*")
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

        examples_list = annotations[k]["examples"]
        for i, pair in enumerate(examples_list):
            example, annot = pair
            print(" "*5 +"#{}".format(i)+" "+example)
            print(" "*5+annot+"\n")
            
            
            
        
        
        
    
    
def execute(annotations):
    commands = {
        "list":show_all_scripts
        }
    
    args = vars(parse_args())
    for key, val in args.items():
        if val is not None:
            commands[key](annotations, val)
    

annotations = read_scripts_annotations()
execute(annotations)
