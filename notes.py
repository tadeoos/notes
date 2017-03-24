#!/Users/Tadeo/anaconda/bin/python

import os
import sys

file, note_text = '.notes/'+sys.argv[1], ' '.join(sys.argv[2:])+'\n'

os.makedirs('.notes', exist_ok=True)

with open(file,"a+") as f:
    f.write(note_text)