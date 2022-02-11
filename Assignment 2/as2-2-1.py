import cv2
import numpy as np
import matplotlib.pyplot as plt


#read files in as grayscale images
messi_color = cv2.imread('messi.jpg')
ronaldo_color = cv2.imread('ronaldo.jpg')

messi = cv2.cvtColor(messi_color, cv2.COLOR_BGR2GRAY)
ronaldo = cv2.cvtColor(ronaldo_color, cv2.COLOR_BGR2GRAY)

height, width = messi.shape[:2]

new_messi = np.zeros((height,width))
new_ronaldo = np.zeros((height,width))

#convert images into the fourier domain
messi_f = np.fft.fft2(messi)
#shift zero frequency components to the center of spectrum
messi_f_shift = np.fft.fftshift(messi_f)

#same process for ronaldo image
ronaldo_f = np.fft.fft2(ronaldo)
ronaldo_f_shift = np.fft.fftshift(ronaldo_f)

#combine the magnitude and phase
new_messi = abs(ronaldo_f_shift) * np.exp(1j*np.angle(messi_f_shift))
new_ronaldo = abs(messi_f_shift) * np.exp(1j*np.angle(ronaldo_f_shift))

#shift the components back to original place

#compute inverse discrete fourier transform
new_messi = np.fft.ifftshift(new_messi)
new_messi = np.fft.ifft2(new_messi).real

new_ronaldo = np.fft.ifftshift(new_ronaldo)
new_ronaldo = np.fft.ifft2(new_ronaldo).real

cv2.imshow("Ronaldo",new_ronaldo)
cv2.waitKey(10000)

cv2.imshow("Messi",new_messi)
cv2.waitKey(10000)