# -*- coding: utf-8 -*-
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

if __name__ == "__main__":
    print("Start.")
    kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Infrared)

    while True:
        #blank_image = np.zeros((kinect.color_frame_desc.Width, kinect.color_frame_desc.Height,3), np.uint8)#kinect.get_last_color_frame()
        frame = kinect.get_last_infrared_frame()
        f8 = np.uint8(frame.clip(1, 4000) / 16.)
        frame8bit = np.dstack((f8, f8, f8))
        frame = frame8bit.tolist()
        print(frame[0][:60])
        print()

        #.reshape((kinect.infrared_frame_desc.Width, kinect.infrared_frame_desc.Height))
        #frame = np.array_split(frame8bit, kinect.infrared_frame_desc.Width)
        #cv2.imshow('frame', frame8bit)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
