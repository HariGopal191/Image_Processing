import cv2
import numpy as np
'''img = cv2.imread('L-Drago.jpg',1)
cv2.imshow('Ryuga',img)
cv2.waitKey(0)'''
'''
img = cv2.imread('L-Drago.jpg',0)
cv2.imshow('Ryuga',img)
cv2.waitKey(0)'''

img = cv2.imread('cap.jpg',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k== 27:
        cv2.destroyAllWindows()
elif k==ord('s'):
        cv2.imwrite('gray.jpg',img)
        cv2.destroyAllWindows()
