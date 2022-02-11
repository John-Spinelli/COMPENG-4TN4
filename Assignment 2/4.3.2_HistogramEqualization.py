import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
img = cv2.imread('img4.png')
cv2.imshow('image',img)

img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
#cv2.imshow('image2',img)

# Original Histograms
L = img[:,:,0]
hist_L = cv2.calcHist([L],[0],None,[256],[0,256])

# Use CLAHE
clahe = cv2.createCLAHE(clipLimit = 5)
L2 = clahe.apply(L)

hist_L2 = cv2.calcHist([L2],[0],None,[256],[0,256])

# Update Image
img[:,:,0] = L2
#cv2.imshow('equalized image',img)

img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
cv2.imshow('converted image',img)
cv2.imwrite('Equalized_Mushroom_L_CLAHE.png',img)

# Plot Histograms
f, arr = plt.subplots(1,2)
arr[0].plot(hist_L, color='r', label="L")
arr[1].plot(hist_L2, color='b', label="L2")
f.set_figheight(4)
f.set_figwidth(12)
plt.show()

