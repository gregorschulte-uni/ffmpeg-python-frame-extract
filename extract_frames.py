import cv2
import os
from glob import glob


os.chdir('C:\\test\\')                   # Manually setting working directory, add open folder dialog later

framecounter    = 0                      # number of frames in video
frameshift      = 0                      # number of frames to skip at the beginning of a video

temppath        = "empty"                # initialize temporary path string
tempfile        = "empty"                # initialize temporary file string

multiplier      = 0                      # initzalize multiplier, ie seconds * fps
restframes      = 0                      # initialize frames left in video

seconds         = 40                     # set interval in seconds

for file in glob('**/*.mp4'):
   
    vidcap          = cv2.VideoCapture(file)
    success,image   = vidcap.read()
    
    fps             = vidcap.get(cv2.CAP_PROP_FPS)                  # Gets the framerate of the current video
    frames          = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)          # Gets the number of frames in the current video
    multiplier      = round(fps * seconds)                          # nth frame to write   
    
    
    if os.path.dirname(file) == temppath: 
        print ("altes  Verzeichis")
        if os.path.abspath(file) == tempfile:
            print("same File")

        else:
            print("new File")
            frameshift =  multiplier - restframes
        
    else:
            print("neues Verzeichnis")
            frameshift      = 0
            framecounter    = 0
            restframes      = 0
    
    
    
    print("\n##################################",
          "\nFilename:\t\t\t", os.path.abspath(file),
          "\nFrames in current video:\t",frames,         # print current video file information
          "\nFPS:\t\t\t\t", fps, 
          "\nInterval:\t\t\t", seconds,"s" , 
          "\nMultiplier:\t\t\t", multiplier ,
          "\nFrames left from last video:\t",restframes,
          "\nFrames to skip:\t\t\t", frameshift,
          "\n########################################\n")

    
    while success:
        frameId = int(round(vidcap.get(1)))             # get current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
        position = frameId + restframes                 # calculate position correct for time left in previous file 
        
        success, image = vidcap.read()
    
        if (position) % multiplier == 0:
            framecounter += 1
            filename = os.path.abspath(file).replace('.mp4','') +"_"+ str(frameId).zfill(8) + "_"+str(framecounter).zfill(8)+".jpg"
            print (filename)
            cv2.imwrite(filename, image)                # write frame to image
            


    restframes = (frames - frameshift) % multiplier     # calculate frames left in video     
 
    temppath = os.path.dirname(file)                    # fill temporary path variable
    tempfile = os.path.abspath(file)                    # fill temporary filename variable
    
    vidcap.release()
    
    
print ("Complete")