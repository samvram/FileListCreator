# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 21:14:12 2018

@author: samvr
"""

import os

filepath = os.getcwd()

files = os.listdir(filepath)

print(files)

with open(os.path.join(filepath,'list_of_files.txt'),'w') as f:
    for file in files:
        f.write(file+'\n')

        