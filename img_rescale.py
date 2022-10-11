# import the modules

import cv2
import numpy as mp

# img = cv2.imread('Photos/test.jpg')
# cv2.imshow('testing image', img)
def rescaleFram(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
capture = cv2.VideoCapture('Videos/test_video.mp4')
while True:
    isTure, frame = capture.read()
    
    frame_resized = rescaleFram(frame)
    flipped_image = cv2.flip(frame_resized,0)

    cv2.imshow('Video', frame)
    cv2.imshow('video resized', flipped_image)

    if cv2.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv2.destroyAllWindows()