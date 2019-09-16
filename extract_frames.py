import cv2
import os
import subprocess
from glob import glob



os.chdir('C:\\test\\')          # Manually setting working directory, add open folder dialog later

seconds         = 10                     # set interval in seconds

framecounter    = 0                      # number of frames in video
frameshift      = 0                      # number of frames to skip at the beginning of a video
multiplier      = 0                      # initzalize multiplier, ie seconds * fps
restframes      = 0                      # initialize frames left in video
temppath        = "empty"                # initialize temporary path string

for file in glob('**/*.MP4'):
    print(subprocess.getoutput(['F:\\Downloads\\ffmpeg-20190812-9fdc7f1-win64-static\\bin\\ffmpeg.exe', '-i', file, '-an' , '-vcodec', 'copy', 'C:\\test\\muted.mp4']))

    
    vidcap          = cv2.VideoCapture(file)
    success,image   = vidcap.read()
    codec           = vidcap.get(cv2.CAP_PROP_FOURCC)
    fps             = vidcap.get(cv2.CAP_PROP_FPS)                  # Gets the framerate of the current video
    frames          = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)          # Gets the number of frames in the current video
    multiplier      = round(fps * seconds)                          # nth frame to write   
            
    if os.path.dirname(file) != temppath:                           # Test: is it still the same path?
        frameshift      = 0
        framecounter    = 0
        restframes      = 0                          
        print ("\ndifferent folder, resetting counter variables\n")
    
    print("\n##################################################",
          "\nfilename:\t\t\t", os.path.abspath(file),
          "\nframes in current video:\t",round(frames),             # print current video file information
          "\nfps:\t\t\t\t", fps, 
          "\ninterval:\t\t\t", seconds,"s" , 
          "\nmultiplier:\t\t\t", multiplier ,
          "\nframes left from last video:\t",round(restframes),
          "\nframes to skip:\t\t\t", round(frameshift),
          "\ncodec: ", codec,
          "\n##################################################\n")
    
    while success:
        frameId = int(round(vidcap.get(1)))                         # get current frame number, rounded b/c sometimes you get frame intervals which aren't integers...this adds a little imprecision but is likely good enough
        position = round(frameId + restframes)                             # calculate position correct for time left in previous file 
        
        success,image = vidcap.read()
        print(frameId)
        if (position-1) % multiplier == 0:
            framecounter += 1
            filename = os.path.abspath(file).replace('.MP4','') +"_"+ str(frameId).zfill(8) + "_"+str(framecounter).zfill(8)+".jpg"
            print (filename)
            cv2.imwrite(filename, image)                            # write frame to image

    restframes = (frames - frameshift) % multiplier                 # calculate number of frames left in current video   
    frameshift =  multiplier - restframes                           # calculate number of frames to skip in next video
 
    temppath = os.path.dirname(file)                                # fill temporary path variable
    
    vidcap.release()
    
print ("\nextraction complete.")