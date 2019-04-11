import numpy as np
import cv2
import os
import glob


cap = cv2.VideoCapture("night-day.mp4")

count = 0

path = 'night-day/'

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        # write all frames to /images folder
        cv2.imwrite(path + 'frame%d.jpg'%count, frame)
        count += 1

        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

