#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import sys
import cv2
import pyzbar.pyzbar as pyzbar

# try:
cap = cv2.VideoCapture("http://192.168.1.223/mjpg/video.mjpg")

if not cap.isOpened():
    sys.exit()
#     pass

print("Start While Loop")
cc = 0
while(True):
    ret, frame = cap.read()
    decObj = pyzbar.decode(frame)
    for obj in decObj:
        print("Data {}".format(cc), obj.data.decode())
        cc += 1
    # cv2.imshow('Frame', frame)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break

cap.release()
cv2.destroyAllWindows()
