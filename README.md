# VolumeHandControl
This project allows you to control the volume of your computer by using hand gestures. It utilizes computer vision and hand tracking techniques to detect and track hand movements, and adjusts the system volume based on the gestures detected.

# Requirements
Make sure you have the following dependencies installed:

Python 3.x
OpenCV
Mediapipe
Pycaw

You can install the required packages using the following command:

    pip install opencv-python mediapipe pycaw

# Usage
1. Import the necessary libraries:

          import cv2
          import numpy as np
          import HandTrackingModule as htm
          from ctypes import cast, POINTER
          from comtypes import CLSCTX_ALL
          from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
          import math as m

2. Set up the audio device and volume control:

		devices = AudioUtilities.GetSpeakers()
		interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
		volume = cast(interface, POINTER(IAudioEndpointVolume))
		volumeRange = volume.GetVolumeRange()

		minVol = volumeRange[0]
		maxVol = volumeRange[1]

3. Set up the video capture and hand tracking module:

        cap = cv2.VideoCapture(0)
        detector = htm.handDetector()

4. Start the main loop to process video frames:

         while True:
           success, img = cap.read()
           detector.findHands(img)
           position_list = detector.HandPositions(img)

              Detect hand gestures and adjust volume
              if len(position_list) != 0:
                  x1 = position_list[4][1]
                  y1 = position_list[4][2]
                  x2 = position_list[8][1]
                  y2 = position_list[8][2]

              cv2.circle(img, (x1, y1), 15, (255, 0, 0), cv2.FILLED)
              cv2.circle(img, (x2, y2), 15, (255, 0, 0), cv2.FILLED)
              cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 4)

              length = m.hypot(x2 - x1, y2 - y1)
              print(length)

              # Hand range: 30 - 325
              # Volume range: minVol - maxVol

              vol = np.interp(length, [30, 325], [minVol, maxVol])
              volume.SetMasterVolumeLevel(vol, None)
              print(vol)

              cv2.imshow("Image", img)
              cv2.waitKey(1)

5.Run the script and adjust the volume by moving your hand closer or farther apart.
