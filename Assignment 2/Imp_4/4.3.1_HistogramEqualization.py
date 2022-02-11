import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read Image
img = cv2.imread('img4.png')
cv2.imshow('image',img)

# Original Histograms
b, g, r = img[:,:,0], img[:,:,1], img[:,:,2]
hist_b = cv2.calcHist([b],[0],None,[256],[0,256])
hist_g = cv2.calcHist([g],[0],None,[256],[0,256])
hist_r = cv2.calcHist([r],[0],None,[256],[0,256])

# Use CLAHE
clahe = cv2.createCLAHE(clipLimit = 5)
b2 = clahe.apply(b)
g2 = clahe.apply(g)
r2 = clahe.apply(r)
hist_b2 = cv2.calcHist([b2],[0],None,[256],[0,256])
hist_g2 = cv2.calcHist([g2],[0],None,[256],[0,256])
hist_r2 = cv2.calcHist([r2],[0],None,[256],[0,256])

# Display Result
img[:,:,0], img[:,:,1], img[:,:,2] = b2, g2, r2
cv2.imshow('equalized image',img)
cv2.imwrite('Equalized_Mushroom_CLAHE.png',img)

# Plot histograms
f, arr = plt.subplots(1,2)
arr[0].plot(hist_r, color='r', label="r")
arr[1].plot(hist_r2, color='r', label="r2")
f.set_figheight(4)
f.set_figwidth(12)
plt.show()

f, arr = plt.subplots(1,2)
arr[0].plot(hist_g, color='g', label="g")
arr[1].plot(hist_b2, color='g', label="g2")
f.set_figheight(4)
f.set_figwidth(12)
plt.show()

f, arr = plt.subplots(1,2)
arr[0].plot(hist_b, color='b', label="b")
arr[1].plot(hist_g2, color='b', label="b2")
f.set_figheight(4)
f.set_figwidth(12)
plt.show()


