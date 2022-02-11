import cv2
import numpy as np
from matplotlib import pyplot as plt
import cmath

# Read and display original images in grayscale
img = cv2.imread('messi.jpg')
img2 = cv2.imread('ronaldo.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('Messi',gray_img)
cv2.imshow('Ronaldo',gray_img2)

# Fourier transform images
gray_fourier = np.fft.fft2(gray_img)
shifted_gf = np.fft.fftshift(gray_fourier)

gray_fourier2 = np.fft.fft2(gray_img2)
shifted_gf2 = np.fft.fftshift(gray_fourier2)

plt.imshow(np.log(abs(shifted_gf)), cmap='gray')
#plt.show()
plt.imshow(np.angle(shifted_gf), cmap = 'gray')
#plt.show()

# Create Low Pass
rows, cols  = gray_img.shape
crow, ccol = int(rows / 2), int(cols / 2)

LP = np.zeros((rows,cols), np.uint8)
r = 30
center = [crow, ccol]
x, y = np.ogrid[:rows, :cols]
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
LP[mask_area] = 1

# Create High Pass
HP = np.ones((rows, cols), np.uint8)
mask_area = (x - center[0]) ** 2 + (y - center[1]) ** 2 <= r*r
HP[mask_area] = 0

plt.imshow(LP, cmap = 'gray')
plt.show()
cv2.imwrite
plt.imshow(HP, cmap = 'gray')
plt.show()

# Apply filters to TF images
LP_mes = LP*shifted_gf
HP_ron = HP*shifted_gf2

plt.imshow(np.log(abs(LP_mes)), cmap = 'gray')
plt.show()
plt.imshow(np.log(abs(HP_ron)), cmap = 'gray')
plt.show()

# Switch magnitudes/phases of TF images
mes_ron = abs(shifted_gf) * np.exp(1j*np.angle(shifted_gf2))
ron_mes = abs(shifted_gf2) * np.exp(1j*np.angle(shifted_gf))

# Transform Images back
LP_mes = np.fft.ifftshift(LP_mes)
LP_mes_final = np.fft.ifft2(LP_mes).real
HP_ron = np.fft.ifftshift(HP_ron)
HP_ron_final = np.fft.ifft2(HP_ron).real

blended_img = cv2.addWeighted(LP_mes_final,0.5,HP_ron_final,0.5,0)

mes_ron = np.fft.ifftshift(mes_ron)
mes_ron_final = np.fft.ifft2(mes_ron).real
ron_mes = np.fft.ifftshift(ron_mes)
ron_mes_final = np.fft.ifft2(ron_mes).real

# Plot and save Images
plt.imshow(LP_mes_final, cmap = 'gray')
plt.show()
plt.imshow(HP_ron_final, cmap = 'gray')
plt.show()
plt.imshow(blended_img, cmap = 'gray')
plt.show()

# Scale down blended for a smaller version
scale = 60
width = int(blended_img.shape[1] * scale / 100)
height = int(blended_img.shape[0] * scale / 100)
dim = width, height
smaller_blend = cv2.resize(blended_img, dim, interpolation = cv2.INTER_AREA)

# Continue plotting
plt.imshow(smaller_blend, cmap = 'gray')
plt.show()
plt.imshow(mes_ron_final, cmap = 'gray')
plt.show()
plt.imshow(ron_mes_final, cmap = 'gray')
plt.show()
