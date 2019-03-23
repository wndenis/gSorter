import numpy as np
import cv2
import os

dir_path = os.getcwd()

for filename in os.listdir(dir_path):
    # If the images are not .JPG images, change the line below to match the image type.
    if filename.endswith(".jpg"):
        image = cv2.imread(filename)
        height, width, channels = image.shape
        dx = int(width * 0.28)
        dy = int(height * 0.28)
        #y 15, x 15
        crop_img = image[dy:height - dy, dx:width - dx]
        #cv2.imshow("cropped", crop_img)
        resized = cv2.resize(crop_img,None,fx=0.22, fy=0.22, interpolation=cv2.INTER_AREA)
        cv2.imwrite(filename, resized)
    cv2.waitKey(0)