import cv2
import numpy as np
import HandTrackingModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math as m

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()

minVol = volumeRange[0]
maxVol = volumeRange[1]

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

        #getting the length between the tip of our thumb and index finger
        length = m.hypot(x2-x1, y2 - y1)

        #hand range 35 - 325
        #vol range -74 - 0
        vol = np.interp(length, [30, 325], [minVol, maxVol])
        volume.SetMasterVolumeLevel(vol, None)

    cv2.imshow("Image", img)
    cv2.waitKey(1)