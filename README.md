# toolbox
python scripts collection to solve different system tasks. 

## Files


### Make it Flat
Destroy directory tree and move all files to top directory.<br>

### Sort directory
This script is dedicated to sort directory by chosen extensions.<br>
Example:
```sortdir audio=.flac,.wav,.mp3 arcs=.zip,.rar docs=.docx, .docx,.pdf```

Also it has optional argument ```-wd```. It can be places anywhere.<br>
So it forces script to walk through whole directory tree, not only current working directory.<br>

So this utility takes different number of arguments, where left is name of directory and right values<br>
are extension, that will be moved into mentioned directories. Directories are created from current working directory.<br>

### FRD(find and rename duplicates)
Purpose of this script is obvious, but it was written to avoid problems, that may occur when you use directory sorting<br>
script, because there may be files with the same names, but placed in different directories, so some files will not be moved.<br>
To avoid this problem simply use this tiny script.



## SQL

### GTCN
Script retrieves names of each column of specified table from sqlite3 table.<br>
Usage example: ```python gtcn.py places.sqlite table1 [table2 ... tableN]```

### Foxhist
This script shows visiting frequency of each page from history.<br>
Basic usage:```python foxhist.py root```<br>
To define minimal visiting counter pass cap parameter:<br>
Example:```python foxhist.py root cap=n```<br>
Also you can specify location of database file:<br>
Example:```python foxhist.py root db=place```

Also you can compute frequence char-by-char, omitting root argument. It means, if some url is different from<br>
another one in terms of strings, then they are different urls. It doesn't matter they have the same hostname.<br>