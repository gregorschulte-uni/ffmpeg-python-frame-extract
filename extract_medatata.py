import cv2
import os
from glob import glob

os.chdir('C:\\test\\')          # Manually setting working directory, add open folder dialog later

log = open("log.txt","w")

for file in sorted(glob('**/*.mp4')):
   
    vidcap          = cv2.VideoCapture(file)
    success,image   = vidcap.read()
    fps             = vidcap.get(cv2.CAP_PROP_FPS)                  # Gets the framerate of the current video
    frames          = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)          # Gets the number of frames in the current video
    height          = vidcap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    width           = vidcap.get(cv2.CAP_PROP_FRAME_WIDTH)
    
    logstring = str(os.path.basename(file)) + ";" + str(round(height)).zfill(4) + ";" + str(round(width)).zfill(4) + ";" + str(round(frames)).zfill(10) + ";" + str(fps).zfill(6) +"\r"
    
    print(logstring)    
    log.write(logstring)
    
    vidcap.release()

log.close()    
