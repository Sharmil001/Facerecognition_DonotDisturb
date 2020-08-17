import numpy as np
import cv2
import sys
import serial
import time
import pyautogui

# Used for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Open webcam
cap = cv2.VideoCapture(0)
count = 0


while(True):
    # Capture frame-by-frame
    ret, img = cap.read()
    # Changing the size of the window
    cv2.resizeWindow('img', 500, 500)
    #cv2.line(img,(500,250),(0,250),(0,255,0),1)
    #cv2.line(img,(250,0),(250,500),(0,255,0),1)
    #cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    #convert from BGR to GRAY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1, 5)

    #Draw rectangle on the face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        arr = {y:y+h, x:x+w}
        print (arr)

        """print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))"""
        
         #Calculate center
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2

        print (xx)
        print (yy)

        center = (xx,yy)

        print("Center of Rectangle is :", center)
        #data = "X{0:.0f}Y{1:.0f}Z".format(xx, yy)
        #print ("output = '" +data+ "'")
        #arduino.write(data.encode())


    cv2.imshow('img',img)
    
    # For runing this code in your system add your coordinates here change the range
    # of the xx and yy in both the cases
    if xx>=290 and xx<=320 and yy>=240 and yy<=255 and count==1  :#callibrate it
        pyautogui.press('space')
        count=0

    elif xx>=350 and xx<=365 and yy>=220 and yy<=235 and count==0:#calibrate it
        pyautogui.press('space')
        count=1



    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
