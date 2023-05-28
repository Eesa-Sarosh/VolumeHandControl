import cv2
import numpy as np
import HandTrackingModule as htm
import math as m
import screen_brightness_control as sbc

# set the brightness to 100%
# sbc.set_brightness(50)
# # set the brightness to 100% for the primary monitor
# sbc.get_brightness(50, display=0)
# show the current brightness for each detected monitor

cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    detector.findHands(img)
    position_list = detector.HandPositions(img)

    if len(position_list) != 0:
        x1 = position_list[4][1]
        y1 = position_list[4][2]
        x2 = position_list[8][1]
        y2 = position_list[8][2]
        cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 4)

        # getting the length between the tip of our thumb and index finger
        length = m.hypot(x2-x1, y2 - y1)

        bright = np.interp(length, [30, 325], [0, 100])
        sbc.set_brightness(bright)

    cv2.imshow("Image", img)
    cv2.waitKey(1)