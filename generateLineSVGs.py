# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:24:20 2019

@author: bzesg01
"""

from glob import glob
import os


filelist = glob("E:\Stareso2019-Copy\lines\*.jpg", recursive=True)


for f in filelist:
    prefix = os.path.basename(f)[:3]
    
    print(prefix)
    
    #add writing svg files with jpg filenames
    