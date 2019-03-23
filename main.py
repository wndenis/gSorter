# -*- coding: utf-8 -*-
from pykinect2 import PyKinectV2
from pykinect2.PyKinectV2 import *
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2
import ctypes

if __name__ == "__main__":
    print("Start.")
    kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Infrared)

    while True:
        frame = kinect.get_last_infrared_frame()
        #frame = frame.astype(np.uint8)
        frame = np.reshape(frame, (424, 512))
        f8 = np.uint8(frame.clip(1, 4000) / 16.)
        frame = np.dstack((f8, f8, f8))
        #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        # frame = cv2.bilateralFilter(frame, 9, 150, 75)

        # continue

        # frame = kinect.get_last_infrared_frame()
        # f8 = np.uint8(frame.clip(1, 4000) / 16.)
        # frame = np.dstack((f8, f8, f8))
        # # frame = np.array(frame)
        # frame = frame.reshape(kinect.color_frame_desc.Width // 3, kinect.color_frame_desc.Height // 3)

        print(frame)
        print()

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
