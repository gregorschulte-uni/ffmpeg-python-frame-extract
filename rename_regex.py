from glob2 import glob
import os

files = glob('E:\\**\\**\\*.MP4', recursive = True)
files.sort()

for f in files:
    onedelimiter = os.path.basename(f).replace('_','.')
    number = str(onedelimiter.split('.')[1]).zfill(2) 
    newname = os.path.dirname(f)+'\\'+os.path.basename(f).split('.')[0]+'.'+number+'_'+os.path.basename(f).split('_', 1)[1]
    print(os.path.basename(newname))
    os.rename(os.path.abspath(f),newname)
print(len(files))