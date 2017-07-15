import numpy as np
import cv2
def loadvideo(Numframe,filename):
    i=0
    while (i<Numframe):
        cap=cv2.VideoCapture(filename)
        cap.read()
        i+=1
    t,frame=cap.read()
    cv2.imshow('a',frame)
    return frame
