import numpy as np
import cv2
vid=cv2.VideoCapture(0)
instant=vid.read()
#print(instant)
avg=np.float32(sum(instant)/len(instant))
file=cv2.CascadeClassifier("/home/harigopal/opencv/data/haarcascades/haarcascade_upperbody.xml")
obj=0
while(1):
    _,frame=vid.read()
    #print(frame)
    cv2.accumulateWeighted(frame, avg, 0.1)
    background=cv2.convertScaleAbs(avg)
    diff=cv2.absdiff(frame, background)
    cv2.imshow("input", frame)
    bodies=file.detectMultiScale(frame)
    for body in bodies:
        cv2.rectangle(frame, (body[0], body[1]), (body[0]+body[2], body[0]+body[3]), (255,0,0), 3)
    cv2.imshow("Upper Body", frame)
    if cv2.waitKey(5)==27:
        break
vid.release()
cv2.destroyAllWindows()
