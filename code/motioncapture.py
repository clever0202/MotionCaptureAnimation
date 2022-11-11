import sys
import os
import cv2
import numpy as np
import random
from matplotlib import pyplot as plt
from IPython.display import clear_output
# %matplotlib inline

# Setup for object tracking

if not os.path.isdir(os.path.join(os.getcwd(), 'resources/frames')):
    os.mkdir("resources/frames")
else:
    print('frames already exists')

if not os.path.isdir(os.path.join(os.getcwd(), 'resources/composite')):
    os.mkdir("resources/composite")
else:
    print('composite already exists')
    
framenumber = 0
framectr = 0
omovie = cv2.VideoCapture('resources/Opt1-MarionetteMovements.mov')
frame_height = omovie.get(cv2.CAP_PROP_FRAME_HEIGHT)
frame_width = omovie.get(cv2.CAP_PROP_FRAME_WIDTH)

# Extract the frames from original video
# while(1):
#     ret, frame = omovie.read()
#     if not ret:
#         break
#     print('Extracting: %d' % framenumber)
#     clear_output(wait=True)
#     cv2.imwrite('resources/frames/%d.tif' % framenumber, frame)
#     framenumber += 1
# omovie.release()

framenumber = 950
#Going through each frame to find values with R higher than threshold
framectr = framenumber - 1
process_frame = 0

foreground = 250 # Foreground Threshold for Segmentation
# Store the coordinates found by intensity thresholding
coordListX = list()
coordListY = list()

while process_frame <= framectr:
    oframe = cv2.imread('resources/frames/%d.tif' % process_frame)
    print('Processing frame: %d, overall progress: %.2f %%' % (process_frame, process_frame/framectr*100))
    clear_output(wait=True)
    
    # Change frame to grey scale
    gframe = oframe.copy() # Grey scaled frame

    # Load the saved frames sequentially
    height = None
    width = None
    for y in range(gframe.shape[1]):
        for x in range(gframe.shape[0]):
            # Convert to gray scale
            if oframe[x][y][2] >= 200 and oframe[x][y][0] < 150 and oframe[x][y][1] < 150 :
                gframe[x][y][2] = 255
            else:
                for i in range(3):
                        gframe[x][y][i] = 0

    # Get the initial state (object coordinates  
#     oframe = cv2.line(oframe, (coord[1], coord[0]), (gcoord[1], gcoord[0]), (0, 0, 255), 2)

    count = 0
    for y in range(gframe.shape[1]):
        for x in range(gframe.shape[0]):
            if(gframe[x][y][0] == 255):
                count += 1

    ####################################### END ################################################
    cv2.imwrite('resources/composite/composite%d.tif' % process_frame, gframe)
    if cv2.waitKey(30) & 0xff == ord('q'):
        break
    process_frame += 1