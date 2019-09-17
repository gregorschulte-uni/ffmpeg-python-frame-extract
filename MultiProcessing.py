from multiprocessing import Pool
import multiprocessing
import os
#import shutil 
import subprocess

import datetime

from glob2 import glob

import struct 

if (struct.calcsize('P')*8== 64):
    print('64 bit system recognized')
    ffmpegpath = 'C:\\ffmpeg\\ffmpeg64\\bin\\ffmpeg.exe'
    print(ffmpegpath)
else: 
    print('64 bit system recognized')
    ffmpegpath = 'C:\\ffmpeg\\ffmpeg32\\bin\\ffmpeg.exe'
    print(ffmpegpath)
    
parameters = ' -loglevel panic -an -vcodec copy -y '
    

filelist = glob('C:\\test\\videos01\\**\\*.mp4', recursive=True)

def convert_and_delete(file):
    filename = str(os.path.abspath(file))
    mutename = str(os.path.abspath(file)[:-4]+'_m'+os.path.splitext(file)[1])
    p_string = ffmpegpath + ' -i ' + filename + parameters + mutename
    print(datetime.datetime.now().time().strftime('%H:%M:%S'), filename)    
    subprocess.call(p_string, shell = True)
    os.remove(file) 

#def f(x):
#    print(x)
#    cp = shutil.copy(x,os.path.dirname(os.path.dirname(os.path.abspath(x))))
#    return cp




if __name__ == '__main__':
    

    
    with Pool(multiprocessing.cpu_count()) as p:
        p.map(convert_and_delete, filelist)
        
    os.system("pause")    
    
