from glob import glob
import os

files  = glob('E:\\Stareso2019-Copy\\lines\\*.jpg')

f = open('E:\\Stareso2019-Copy\\lines\\template\\template.svg','r')
filedata = f.read()
f.close()

for file in files:
    
    prefix = os.path.splitext(os.path.basename(file))[0]
    
    newdata = filedata.replace("000.jpg", os.path.basename(file))
    newdata = newdata.replace("000.png", prefix+".png")    
    
    outname = "E:\\Stareso2019-Copy\\lines\\"+prefix+".svg"

    f = open(outname,'w')
    f.write(newdata)
    f.close()
    print(prefix)
    
print("\nDone, created "+ str(len(files)) +" files.")