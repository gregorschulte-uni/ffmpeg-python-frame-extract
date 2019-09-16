# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 10:53:49 2019

@author: bzesg01
"""

import subprocess
from glob import glob
import os

#ffmpeg = 'F:\\Downloads\\ffmpeg-20190812-9fdc7f1-win64-static\\bin\\ffmpeg.exe'

os.chdir('C:\\test\\')  

for file in glob('**/*.MP4'):
    filename = os.path.abspath(file)
    mutename = os.path.abspath(file)[:-4]+'_m.mp4'
    print (filename)
    print (mutename)
    p = subprocess.run(["F:\\Downloads\\ffmpeg-20190812-9fdc7f1-win64-static\\bin\\ffmpeg.exe", "-i", filename, "-an", "-vcodec copy", mutename])
    print(p)
