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
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
    # detector.setModelTypeAsTinyYOLOv3()
    # detector.setModelPath(os.path.join(execution_path, "yolo-tiny.h5"))
    detector.loadModel()
    custom_objects = detector.CustomObjects(person=True, umbrella=True, car=True, cup=True, fork=True, knife=True, bottle=True, cell_phone=True)

    kinect = PyKinectRuntime.PyKinectRuntime(PyKinectV2.FrameSourceTypes_Color)

    shape = (424, 512)
    midpoint = (kinect.color_frame_desc.Width // 2, kinect.color_frame_desc.Height // 2)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    while True:
        frame = kinect.get_last_color_frame()
        frame = frame.reshape((1080, 1920, -1)).astype(np.uint8)
        # frame = np.reshape(frame, (1080, 1920, -1))#.astype(np.uint8)
        frame = cv2.resize(frame, (0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_CUBIC)

        # frame = cv2.resize(frame, dsize=(1920//4, 1080//4), interpolation=cv2.INTER_CUBIC)

        #gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if True:
            detections = detector.detectCustomObjectsFromImage(input_image=frame,
                                                         input_type="array",
                                                         output_type="array",
                                                         minimum_percentage_probability=70,
                                                         custom_objects=custom_objects)
            for box in detections[1]:
                b = box['box_points']
                cv2.rectangle(frame, b,
                              (0, 0, 250), 2)
                label = "{} {:.2f}".format(box['name'], box['percentage_probability'])
                cv2.putText(frame, label, (b[0], b[1] - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

                # print(box)
                # print("\n\n\n\n\n\n\n")
        # frame = np.reshape(frame, shape)
        # frame = np.uint8(frame.clip(1, 4000) / 16.)?????????????????
        # frame = cv2.bilateralFilter(frame, 9, 150, 75)
        # cv2.rectangle(frame, (midpoint[0]-15, midpoint[1]-15), (midpoint[0]+15, midpoint[1]+15), (32000, 32000, 32000), 2)
        # color = frame[midpoint]
        #frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

        cv2.imshow("output", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
