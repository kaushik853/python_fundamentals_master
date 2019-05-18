'''
Write a script that searches a folder (and all its subfolders) on your computer and compiles a list of all of
all .jpg files (with the complete path of the files).

If you are feeling bold, create a list for each kind of file extension you find in the folder.

Start with a small folder to make it easy to check if your program is working correctly. Then sub out the
folder name with a bigger folder. This program should work for any specified folder on your computer.


'''

# import fnmatch
# import os
# import re
#
# def findfiles(which, where='.'):
#     '''Returns list of filenames from `where` path matched by 'which'
#        shell pattern. Matching is case-insensitive.'''
#
#     # TODO: recursive param with walk() filtering
#     rule = re.compile(fnmatch.translate(which), re.IGNORECASE)
#     return [name for name in os.listdir(where) if rule.match(name)]
# print(findfiles('*.jpg', '/Users/xxxyyy/Downloads'))

import glob
from pathlib import Path
cfiles = Path('/Users/xxxyyy/Downloads').glob("**/*.jpg")
for files in cfiles:
    print(files)
dfiles = Path('/Users/xxxyyy/Downloads').glob("**/*.JPG")
for file in dfiles:
    print(file)

config_files = glob.glob('/Users/palkau/Downloads/**/*.jpg', recursive=True)
for c_file in config_files:
    print(c_file)

import os
for (root, dirs, file_1) in os.walk('/Users/xxxyyy/Downloads', topdown=True):
    print(root)
    print(dirs)
    print(file_1)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

import os
file_type = []
for (root, dirs, file_1) in os.walk('/Users/xxxyyy/Downloads', topdown=True):
    for file in file_1:
        file_2 = file.split(".")[-1]
        if file_2 not in file_type:
            file_type.append(file_2)
print(file_type)
