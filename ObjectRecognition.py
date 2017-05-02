# !/usr/bin/env python

# Importing modules
import numpy as np
import cv2
import random
#from video import create_capture
from common import clock, draw_str

help_message = '''
===============================================================================
===================== CONTROLLED OBJECT RECOGNITION ===========================
===============================================================================

We recognize the following :
1. Face 
2. Eye
3. Smile
4. Animal Face (cat)
5. Wall Clock
6. Number Plate
'''

choice_message = '''
Choose an input feed :
0. Webcam
1. Video file
2. Exit
'''

# Function for detecting face
def detect_face_eye(img, cascade):
    
    rects = cascade.detectMultiScale(img, scaleFactor=1.25, minNeighbors=4, \
                            minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Function for detecting cat face
def detect_cat(img, cascade):
    
    rects = cascade.detectMultiScale(img, scaleFactor=1.09, minNeighbors=35, \
                            minSize=(99,99), flags = cv2.CASCADE_SCALE_IMAGE)   
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Function for detecting smile
def detect_smile(img, cascade):
    
    rects = cascade.detectMultiScale(img, scaleFactor=1.23, minNeighbors=60, \
                            minSize=(30, 30), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Function for detecting number plate
def detect_numberplate(img, cascade):
    
    rects = cascade.detectMultiScale(img, scaleFactor=1.08, minNeighbors=15, \
                            minSize=(3, 3), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Function for detecting wall clock
def detect_wc(img, cascade):
    
    rects = cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=10, \
                            minSize=(5, 5), flags = cv2.CASCADE_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    rects[:,2:] += rects[:,:2]
    return rects

# Function to draw rectangle around the detected object
def draw_rects(img, rects, color, obj):
    
    for x1, y1, x2, y2 in rects:
        
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
        draw_str(img, (x1, y1-10), ' # %s' %obj) # Name of the detected object
        
# Main function      
if __name__ == '__main__':
    import sys
    print help_message
 
    cascade = cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\haarcascade_frontalface_alt.xml")
    nested  = cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\haarcascade_eye.xml")
    cat= cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\haarcascade_frontalcatface.xml")
    smile = cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\haarcascade_mcs_mouth.xml")
    numberplate = cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\haarcascade_russian_plate_number.xml")
    wc = cv2.CascadeClassifier("E:\SOFTWARES\opencv\sources\data\haarcascades\wc.xml")

    while(1):
        print choice_message
        choice = input ("Enter a choice ")
        
        if choice==0:
            cam = cv2.VideoCapture(0)
            break
        
        elif choice==1:
            vid = raw_input("Enter a filename ")
            cam = cv2.VideoCapture(vid)
            #cam = cv2.VideoCapture(sys.argv[1])
            break
        
        elif choice==2:
            quit()
            
        else:
            print "\ninvalid choice"
    
    u=v=w=x=y=0
    
    if not cam.isOpened():
        print 'camera not opened'
        
    while (cam.isOpened()):
        ret, img = cam.read()                                       # Reading from the webcam
        
        if ret:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)            # Convert to grayscale
            gray = cv2.equalizeHist(gray)                           # Histogram equalization (Adjusting brightness)
            
            rects = detect_face_eye(gray, cascade)
            if rects == [] or v==11:
                v=0
            else:
                v=v+1
                
            if v==10:
                checkname = "face"
                vi = vis.copy()              
                filename =checkname+str(random.randrange(100, 1000, 2))+".bmp"
                cv2.imwrite(filename,vi) # writes image test.bmp to disk

                
            rect_cat = detect_cat(gray, cat)
            if rect_cat == [] or u==11:
                u=0
            else:
                u=u+1
            if u==10:
                checkname = "cat"
                vi = vis.copy()              
                filename =checkname+str(random.randrange(100, 1000, 2))+".bmp"
                cv2.imwrite(filename,vi) # writes image test.bmp to disk
                
                
            rect_smile = detect_smile(gray, smile)
            if rect_smile == [] or w==6:
                w=0
            else:
                w=w+1
            if w==5:
                checkname = "smile"
                vi = vis.copy()              
                filename =checkname+str(random.randrange(100, 1000, 2))+".bmp"
                cv2.imwrite(filename,vi) # writes image test.bmp to disk

                
            rect_wc = detect_wc(gray, wc)
            if rect_wc == [] or x==11:
                x=0
            else:
                x=x+1
            if x==10:
                checkname = "wallclock"
                vi = vis.copy()              
                filename =checkname+str(random.randrange(100, 1000, 2))+".bmp"
                cv2.imwrite(filename,vi) # writes image test.bmp to disk

                
            rect_numberplate = detect_numberplate(gray, numberplate)
            if rect_numberplate == [] or y==11:
                y=0
            else:
                y=y+1
            if y==10:
                checkname = "numberplate"
                vi = vis.copy()              
                filename =checkname+str(random.randrange(100, 1000, 2))+".bmp"
                cv2.imwrite(filename,vi) # writes image test.bmp to disk
                
            
            vis = img.copy()                                            # Copy of the original image
            draw_rects(vis, rects, (255, 0, 255), "Face")
            draw_rects(vis, rect_cat, (255, 0, 0), "Cat")
            draw_rects(vis, rect_smile, (255, 255, 0), "smile")
            draw_rects(vis, rect_wc, (255, 255, 0), "WallClock")
            draw_rects(vis, rect_numberplate, (255, 255, 255), "NumberPlate")

            if not nested.empty():
                for x1, y1, x2, y2 in rects:
                    roi = gray[y1:y2, x1:x2]
                    vis_roi = vis[y1:y2, x1:x2]
                    subrects = detect_face_eye(roi.copy(), nested)
                    draw_rects(vis_roi, subrects, (0, 255, 0), "Eye")
            
            cv2.imshow('CONTROLLED OBJECT RECOGNITION', vis)    # Displaying the window 'CONTROLLED OBJECT RECOGNITION'
            
            if 0xFF & cv2.waitKey(5) == 27:
                cam.release()                                     # Closing the webcam             
                break
                
        elif not ret:
            continue
        
        else:
            cam.release()                                        # Closing the webcam
                                              
cv2.destroyAllWindows()                                         # Destroying the window
