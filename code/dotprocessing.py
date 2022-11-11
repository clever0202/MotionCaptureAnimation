import cv2
import numpy as np
#load image
img = cv2.imread('resources/composite/composite0.tif')

#apply median blur, 15 means it's smoothing image 15x15 pixels
blur = cv2.medianBlur(img,15)

#convert to hsv
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

#color definition
red_lower = np.array([10,0,0])
red_upper = np.array([180,255,255])

#red color mask (sort of thresholding, actually segmentation)
mask = cv2.inRange(hsv, red_lower, red_upper)

connectivity = 4  
# Perform the operation
output = cv2.connectedComponentsWithStats(mask, connectivity, cv2.CV_32S)
# Get the results

num_labels = output[0]-1

centroids = output[3][1:]
#print results
print ('number of dots, should be 4:',num_labels )
print ('array of dot center coordinates:',centroids)