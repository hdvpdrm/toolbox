# system-tools
place to store py scripts, solving different  system tasks. 

# Make it Flat
This script was written for 30 minutes and its meaning to be is to prepare directory<br>
for another script. However, currently i found new better solution, but i will use it anyway.<br>
you run this script from the top of some directory and then it destroys every subdir, moving files<br>
to the top, where script was invoked.<br>

# Sort directory
This script is dedicated to sort directory by chosen extensions.<br>
Example:
```sortdir audio=.flac,.wav,.mp3 arcs=.zip,.rar docs=.docx, .docx,.pdf```

Also it has optional argument ```-wd```. It can be places anywhere.<br>
So it forces script to walk through whole directory tree, not only current working directory.<br>

So this utility takes different number of arguments, where left is name of directory and right values<br>
are extension, that will be moved into mentioned directories. Directories are created from current working directory.<br>

# FRD(find and rename duplicates)
Purpose of this script is obvious, but it was written to avoid problems, that may occur when you use directory sorting<br>
script, because there may be files with the same names, but placed in different directories, so some files will not be moved.<br>
To avoid this problem simply use this tiny script.

# CGI(create gitignore)
This script is used to create .gitignore file.<br>
Example:
```cgi -f .sln .txt .user .filter -d Release .git```
After` ```-f``` mark you pass file extensions to add to gitignore and<br>
after ```-d``` mark you pass directories to ignore.<br>

To walk through whole directory of project, you should use ```-wd``` option.<br>

# SRM(safe rm)
This script rewrites files n times(default value is 5) and then removes it. There will be ability to recover it, but its content will be noise.<br>
Example:<br>
```srm kitten.png 100```<br>
```srm kitten.png```<br>

