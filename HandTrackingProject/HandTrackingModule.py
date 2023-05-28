import cv2
import mediapipe as mp

class handDetector():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(min_detection_confidence=0.7)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
               self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)

    def HandPositions(self, img):
        lmList = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                 for id, lm in enumerate(handLms.landmark):
                    height = img.shape[0]
                    width = img.shape[1]
                    cx = int(lm.x * width)
                    cy = int(lm.y * height)
                    lmList.append([id, cx, cy])
        return lmList
