import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read image, make gray copy
img = cv2.imread('3.png')
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur and canny for contour detection
img_blur = cv2.GaussianBlur(img_g, (3,3), 0)
img_c = cv2.Canny(img_blur, 200, 250)

# Get contours
all_contours = img.copy()
contours, hierarchy = cv2.findContours(img_c,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
cv2.drawContours(all_contours, contours, contourIdx=-1, color=(0,255,0), thickness=2, lineType = cv2.LINE_AA)
cv2.imshow('All Contours', all_contours)
cv2.imwrite('all_contours.png', all_contours)

# Detected parameters
max_p = None
max_cont = None

for cont in contours:
    # First contour
    if max_p == None:        
        max_p = cv2.arcLength(cont, True)
        max_cont = cont
        
    elif cv2.arcLength(cont,True) > max_p:
        # Longer contour than before
        max_p = cv2.arcLength(cont, True)
        max_cont = cont

        # If first fully enclosed rectangle, stop
        epsilon = 0.1*cv2.arcLength(cont, True)
        approx = cv2.approxPolyDP(cont, epsilon, True)
        if len(approx) >= 4:
            break

# If contour detected:                  
if max_cont.any():
    # Display contour on image
    good_contour = img.copy()
    cv2.drawContours(good_contour, [max_cont], contourIdx=-1, color=(0,255,0), thickness=2, lineType = cv2.LINE_AA)
    cv2.imshow('Good Contour', good_contour)
    cv2.imwrite('good_contour.png', good_contour)

    # Create a mask, extract the image with mask
    mask = np.zeros(img_g.shape, np.uint8)
    cv2.drawContours(mask,[max_cont],0,255,-1,)
    cv2.imshow('mask',mask)
    extracted = cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('Extracted License',extracted)
    cv2.imwrite('extracted_license.png',extracted)

else:
    print("No contours found, sorry :(")

cv2.waitKey(0)
cv2.destroyAllWindows()
