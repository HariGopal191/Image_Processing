import numpy as np
import cv2
from matplotlib import pyplot as plt
face_csc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_csc = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture('AIW.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([30,150,50])
    upper_red = np.array([255,255,180])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    faces = face_csc.detectMultiScale(frame,1.3,5)
    #cv2.imshow('Original',frame)
    
    edges = cv2.Canny(frame,100,200)
    
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_csc.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #cv2.imshow('some',res)
    cv2.imshow('face/color',np.hstack([frame,res]))
    cv2.imshow('edges',edges)
   #plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


