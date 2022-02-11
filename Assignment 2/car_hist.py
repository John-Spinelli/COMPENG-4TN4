import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
img = cv2.imread('car.png')
img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('car',img)
img2 = cv2.imread('carc.png')
img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
cv2.imshow('carc',img2)

# Original Histograms
hist_1 = cv2.calcHist(img,[0],None,[256],[0,256])
hist_2 = cv2.calcHist(img2,[0],None,[256],[0,256])

# Plot histograms
f, arr = plt.subplots(1,2)
arr[0].plot(hist_1, color='r', label="r")

arr[1].plot(hist_2, color='r', label="r2")
plt.show()


