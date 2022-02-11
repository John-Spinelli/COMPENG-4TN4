''' Johnathan Spinelli, A1_Q3 '''
import cv2
import time
from matplotlib import pyplot as plt
import numpy as np

'''
# Capturing webcam image
cam = cv2.VideoCapture(0)
time.sleep(1)
result, image = cam.read()
time.sleep(1)
result, image = cam.read()
cv2.imwrite('webcam.jpg',image)
'''

# Reading in the image I previously captured
image = cv2.imread('webcam.jpg', 1)
result = 1

if result:
    cv2.imshow("Picture", image)
    #cam.release()

    # Create Histogram
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv],[0],None,[256],[0,256])
    plt.plot(hist, color='k')

    # Threshold acquired from examining histogram
    upper_thresh = 37                        
    lower = np.array([0, 0, 0])
    upper = np.array([upper_thresh,255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    cv2.imshow('mask',mask)
    cv2.imwrite('mask.jpg',mask)

    # Show the resulting image, write it out
    final = cv2.bitwise_and(image,image,mask = mask)
    cv2.imshow('final',final)
    cv2.imwrite('skin_detection.jpg',final)

    # Display histogram at end, blocking menu
    plt.show()

else:
    print("something didnt work")
    cam.release()

cv2.waitKey(0)
cv2.destroyAllWindows()
