# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:15:58 2019

@author: bzesg01
"""

from glob import glob
import shutil
import os.path

os.chdir("E:\\Stareso2019-Copy\\output\\")

filelist = glob("E:\Stareso2019-Copy\stills\set05_2019.06.17_cohort10\**.*", recursive=True)
counter = 0 
for f,g  in zip(filelist,filelist[1:]):
    
    if (os.path.basename(f)[:3]==os.path.basename(g)[:3]):
        counter +=1
    else:
        counter = 0
        
    print(f)
    prefix = os.path.basename(f)[:3]
    try:
        os.mkdir(prefix)
    except OSError:
        print("error")
    else:
        print("done")
    try:
        os.mkdir(prefix+"\\10s")
    except:
        pass
    else:
        pass
    try: 
        os.mkdir(prefix+"\\60s")
    except:
        pass
    else:
        pass
        
    print(prefix)
    print(counter)
    if (counter % 6 == 0):
        shutil.copy(f,prefix+"\\60s\\")
    shutil.copy(f,prefix+"\\10s\\")