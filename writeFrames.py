import numpy as np
import cv2
import os
import glob


cap = cv2.VideoCapture("night-day.mp4")
input_frames = int(cap.get(7))
print (input_frames)
count = 0

path = 'train/'
i = 0
path = path  + str(i)
os.mkdir(path)

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:

        if count == 90:
            i += 1
            path = 'train/' + str(i)
            os.mkdir(path)
            count = 0

        if count == 80:
            path = 'val/' + str(i)
            os.mkdir(path)
        
            
        # write all frames to /images folder
        cv2.imwrite(path + '/%d.jpg'%count, frame)
        count += 1

        # cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

