import cv2
import mediapipe as mp
import numpy as np
import time
import v_mouse

pTime=0

while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame)
    cTime =time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime