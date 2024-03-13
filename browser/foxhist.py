#!/usr/bin/python3
#foxhist: script computes statistic for firefox browser
#Usage example 1: python foxhist.py       -- shows result based on different urls
#Usage example 2: python foxhist.py root  -- shows result based on matched root urls.
#Usage example 3: python foxhist.py cap=2 db=~/.mozilla/firefox/somestrangepath/places.sqlite - Show pages with visiting count above 2
import sqlite3
import sys
import os
from operator import itemgetter
from math import floor
from urllib.parse import urlparse

def get_max_url_len(result):
    urls = [a[0] for a in result if a[0] is not None]
    return max(len(x) for x in urls)
def parse_args():
    if len(sys.argv) == 1:
        return None
    
    args    = sys.argv[1:]
    cap     = None
    db_path = None
    count_root_url = False
    
    for a in args:
        if a == 'root':
            count_root_url = True
            continue
        elif '=' not in a:
            print("foxhist error: '{}' is incorrect argument".format(a))
            sys.exit(1)

        left, right = a.split('=')
        if left == 'cap':
            cap = int(right)
        elif left == 'db':
            db_path = right
        else:
            print("foxhist error: '{}' is incorrect argument".format(left))
            sys.exit(1)
    return db_path, cap, count_root_url

def count_roots(result):
    urls = {}
    for url, _ in result:
        name = urlparse(url).hostname
        if name not in urls.keys():
            urls[name]  = 1
        else:
            urls[name] += 1

    return [(url, count) for url, count in urls.items()]

root = os.path.expanduser("~")
db_path = "{}/.mozilla/firefox/fv1ycf68.default-release/places.sqlite".format(root)
cap = 1
count_root_url = False

parsed = parse_args()
if parsed is not None:
    db_path = db_path if parsed[0] is None else parsed[0]
    cap = cap if parsed[1] is None else parsed[1]
    count_root_url = count_root_url if parsed[2] is None else parsed[2]
try:
    conn   = sqlite3.connect(db_path)
    cursor = conn.execute("SELECT url, visit_count FROM moz_places")
    result = cursor.fetchall()
    total_elements_n = len(result)
    
    result = result if not count_root_url else count_roots(result)
    result = list(filter(lambda a: a[1] > cap,result))
    result = sorted(result,key=lambda x:x[1],reverse=True)
    
    max_len = get_max_url_len(result)

    print("elements shown:",len(result))
    print("total elements:",total_elements_n)
    for el in result:
        #pass empty vals
        if el[0] is None:
            continue
        
        diff = max_len-len(el[0])
        percentage = (el[1]/total_elements_n)*100
        print(el[0]," "*diff, " --- ",el[1]," ---  ",floor(percentage),"%",sep="")
except sqlite3.OperationalError as e:
    print("foxhist error: unable to open {}".format(db_path))
    sys.exit(1)


