# -*- coding: utf-8 -*-
from pykinect2 import PyKinectV2
from pykinect2 import PyKinectRuntime
import numpy as np
import cv2

from imageai.Detection import ObjectDetection
import os

if __name__ == "__main__":
    print("Start.")

    execution_path = os.getcwd()

    detector = ObjectDetection()
    # detector.setModelTypeAsYOLOv3()
    # detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
    detector.loadModel()

    kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

    shape = (424, 512)
    midpoint = (kinect.color_frame_desc.Width // 2, kinect.color_frame_desc.Height // 2)
    while True:
        frame = kinect.get_last_color_frame()

        frame = np.reshape(frame, (1080, 1920, -1)).astype(np.uint8)
        frame = cv2.resize(frame, dsize=(1920//6, 1080//6), interpolation=cv2.INTER_CUBIC)

        #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if False:
            detections = detector.detectObjectsFromImage(input_image=frame,
                                                         input_type="array",
                                                         output_type="array",
                                                         minimum_percentage_probability=10)
            for box in detections[1]:
                cv2.rectangle(frame, box['box_points'],
                              (0, 0, 250), 2)
                print(box)
                print("\n\n\n\n\n\n\n")
        # frame = np.reshape(frame, shape)
        # frame = np.uint8(frame.clip(1, 4000) / 16.)?????????????????
        # frame = cv2.bilateralFilter(frame, 9, 150, 75)
        # cv2.rectangle(frame, (midpoint[0]-15, midpoint[1]-15), (midpoint[0]+15, midpoint[1]+15), (32000, 32000, 32000), 2)
        # color = frame[midpoint]
        #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
