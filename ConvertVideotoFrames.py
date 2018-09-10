import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture("record.mp4")

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not frame is None:
        # Saves image of the current frame in jpg file
        name = str(currentFrame) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)
    else:
        break

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
cv2.destroyAllWindows()