''' Johnathan Spinelli, A1_Q2 '''
import cv2
import numpy as np

orig_img = cv2.imread('img1.png', 1)
# Hardcoded value, can prompt user for input instead
gamma = 1.5
inv = 1.0/gamma

# Method 1 
table = np.array([((i / 255.0) ** inv) * 255
		for i in np.arange(0, 256)]).astype("uint8")

out_img = cv2.LUT(orig_img, table)

# Method 2
out2 = (((orig_img / 255) ** (inv)) * 255).astype('uint8')

cv2.imshow('Original', orig_img)
cv2.imshow('Method1',out_img)
cv2.imwrite('img1_gamma.png',out_img)
cv2.imshow('Method2', out2)


