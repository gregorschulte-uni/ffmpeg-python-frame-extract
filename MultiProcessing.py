from multiprocessing import Pool
import multiprocessing
import os
import shutil 

from glob import glob

filelist = glob("C:\\csv\\input\\*.csv", recursive=True)

def f(x):
    print(x)
    cp = shutil.copy(x,os.path.dirname(os.path.dirname(os.path.abspath(x))))
    return cp

if __name__ == '__main__':
    with Pool(multiprocessing.cpu_count()) as p:
        p.map(f, filelist)
        
    os.system("pause")    