import cv2
from glob import glob
import os

os.chdir('C:\\test\\')

print ("Current Working Dir: ", os.getcwd(), "\n\n")

framecounter = 0
frameshift = 0

temppath = "empty"
tempfile = "empty"

multiplier = 0
restframes = 0

for file in glob('**/*.mp4'):
    
    
    print("Current file: " , os.path.abspath(file))
    
    
    
    vidcap = cv2.VideoCapture(file)
    
    success,image = vidcap.read()
    
    seconds = 40
    
    fps = vidcap.get(cv2.CAP_PROP_FPS) # Gets the frames per second
    
    frames = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)
    
    multiplier = fps * seconds
    
    
    print("Frames:\t\t",frames, 
          "\nFPS:\t\t", fps, 
          "\nInterval:\t", seconds,"s" , 
          "\nMultiplier:\t", multiplier , 
          "\nFrames left:\t", restframes )
    
    
    
    if os.path.dirname(file) == temppath: 
        print ("altes  Verzeichis")
        if os.path.abspath(file) == tempfile:
            print("same File")
        else:
            print("new File")
            frameshift = frameshift + restframes
        
    else:
            frameshift = 0
            print("neues Verzeichnis")
            framecounter = 0

    

    
    print ("\n\n start writing frames \n\n ")
    while success:
        frameId = int(round(vidcap.get(1)))  #current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
        position = frameId + frameshift
        success, image = vidcap.read()
    
        if (position) % multiplier == 0:
            framecounter += 1
            filename = os.path.abspath(file).replace('.mp4','') +"_"+ str(frameId).zfill(8) + "_"+str(framecounter).zfill(8)+".jpg"
            print (filename)
            cv2.imwrite(filename, image)
            


    print ("\n\n finished wrinting frames \n\n")
    restframes = (frames - frameshift) % multiplier
    #frameshift = multiplier - restframes
 
    temppath = os.path.dirname(file)
    tempfile = os.path.abspath(file)
    vidcap.release()
    
    
print ("Complete")