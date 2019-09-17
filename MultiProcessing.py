from multiprocessing import Pool
import multiprocessing
import os
import shutil 

from glob import glob

import struct 


if (struct.calcsize('P')*8== 64):
    print('64 bit system recognized')
    ffmpegpath = 'C:\\ffmpeg64\\bin\\ffmpeg.exe'
else: 
    print('64 bit system recognized')
    ffmpegpath = 'C:\\ffmpeg32\\bin\\ffmpeg.exe'
    
parameters = ' -an -vcodec copy '



    

filelist = glob("C:\\test\\input\\*.mp4", recursive=True)

#def f(x):
#    print(x)
#    cp = shutil.copy(x,os.path.dirname(os.path.dirname(os.path.abspath(x))))
#    return cp


def convert_and_delete(file):
    filename = str(os.path.abspath(file))
    mutename = str(os.path.abspath(file)[:-4]+'_m'+os.path.splitext(file)[1])
    p_string = ffmpegpath + ' -i ' + filename + parameters + mutename
    print(p_string)    
    #c = subprocess.call(p_string)
    #os.remove(file) 

if __name__ == '__main__':
    with Pool(multiprocessing.cpu_count()) as p:
        p.map(f, filelist)
        
    os.system("pause")    