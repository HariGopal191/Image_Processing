import cv2

face_csc = cv2.CascadeClassifier('/home/harigopal/opencv/data/haarcascades/haarcascade_smile.xml')
#cam = cv2.VideoCapture(1)

while(True):
    #tf, img = cam.read()    
    img = cv2.imread("men.jpg")
       
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.imread("")
    
    faces = face_csc.detectMultiScale(gray, 20.3, 4)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 5)
        
    cv2.imshow('img', img)
    key = cv2.waitKey(1)
    if key == 27:
        cv2.destroyallWindows()

#cam.release()
cv2.destroyAllWindows()
