import os
import re

def walker(rootdir, pattern = re.compile('.*?')):
    ls_filename = []
    ls_subdirs = []
    for subdirs, dirs, files in os.walk(rootdir):
        for file in files:
            if pattern.match(file):
                ls_filename.append(file)
                ls_subdirs.append(subdirs)
    return zip(ls_filename, ls_subdirs)