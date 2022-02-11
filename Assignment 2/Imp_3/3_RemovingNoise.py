import numpy as np
import cv2

img = cv2.imread('img3.png')

median = cv2.medianBlur(img,3)
cv2.imshow('median',median)
cv2.imwrite('median_filter.png', median)

low = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('low pass',low)
cv2.imwrite('lowpass_filter.png', low)
