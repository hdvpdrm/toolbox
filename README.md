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

So this utility takes different number of arguments, where left is name of directory and right values<br>
are extension, that will be moved into mentioned directories. Directories are created from current working directory.<br>
