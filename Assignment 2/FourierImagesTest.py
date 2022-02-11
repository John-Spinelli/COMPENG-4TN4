import cv2
import numpy as np
from matplotlib import pyplot as plt
import cmath

img_name = 'target.png'
# Read and display original images in grayscale
img = cv2.imread(img_name)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow(img_name,gray_img)

# Fourier transform images
gray_fourier = np.fft.fft2(gray_img)
shifted_gf = np.fft.fftshift(gray_fourier)



plt.imshow(np.log(abs(shifted_gf)), cmap='gray')
plt.show()

#plt.show()
