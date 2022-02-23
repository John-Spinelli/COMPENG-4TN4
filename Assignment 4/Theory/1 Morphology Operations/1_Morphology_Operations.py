import cv2
import numpy as np
from matplotlib import pyplot as plt
import array_to_latex as a2l

img = [[0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,1,1,1,1,1,1,1,0,0],
     [0,0,0,0,1,1,1,1,1,1,0,0],
     [0,0,0,0,0,1,1,1,1,1,0,0],
     [0,0,0,0,0,0,1,1,1,1,0,0],
     [0,0,1,0,0,0,0,1,1,1,0,0],
     [0,0,0,1,0,0,0,0,1,1,0,0],
     [0,0,0,0,1,0,0,0,0,1,0,0],
     [0,0,0,0,0,1,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0,0,0,0,0]]

ero = [[0,1,0],
       [0,1,1],
       [0,1,0]]

dil = [[1,0,0],
       [0,1,0],
       [0,0,1]]

open = [[1,1,1],
        [1,1,1],
        [1,1,1]]

height = len(img)
width = len(img[0])

ero_res = np.zeros((height, width))
dil_res = np.zeros((height, width))
close_1 = np.zeros((height, width))
close_2 = np.zeros((height, width))

# Display Original
image = np.array(img)
plt.imshow(image,cmap='gray')
plt.show()

# Erosion
for row in range(1,height-1):
    for col in range(1,width-1):
        top = img[row-1][col]
        mid = img[row][col]
        bot = img[row+1][col]
        right = img[row][col+1]
        if top and mid and bot and right:
            ero_res[row,col] = 1

f, arr = plt.subplots(1,2)
arr[0].imshow(image, cmap='gray')
arr[1].imshow(ero_res, cmap='gray')
plt.show()
print('EROSION')
latex = a2l.to_ltx(ero_res, frmt = '{:1.0f}', arraytype='array',print_out=True)

# Dilation
for row in range(1,height-1):
    for col in range(1,width-1):
        top = img[row-1][col-1]
        mid = img[row][col]
        bot = img[row+1][col+1]
        if top or mid or bot:
            dil_res[row,col] = 1

f, arr = plt.subplots(1,2)
arr[0].imshow(image, cmap='gray')
arr[1].imshow(dil_res, cmap='gray')
plt.show()
print('DILATION')
latex = a2l.to_ltx(dil_res, frmt = '{:1.0f}', arraytype='array',print_out=True)


###### OPENING #######
        
# Erosion
for row in range(1,height-1):
    for col in range(1,width-1):

        # Check all pixels in structuring element
        pix_val = 1
        for i in range(-1,2):
            for j in range(-1,2):
                if img[row+i][col+j] == 0:
                    pix_val = 0
                    break
        close_1[row,col] = pix_val

# Dilation
for row in range(1,height-1):
    for col in range(1,width-1):

        # Check all pixels in structuring element
        pix_val = 0
        for i in range(-1,2):
            for j in range(-1,2):
                if close_1[row+i,col+j] == 1:
                    pix_val = 1
                    break
        close_2[row,col] = pix_val

# Display Intermediate Results
f, arr = plt.subplots(1,2)
arr[0].imshow(image, cmap='gray')
arr[1].imshow(close_1, cmap='gray')
plt.show()
print('OPEN1')
latex = a2l.to_ltx(close_1, frmt = '{:1.0f}', arraytype='array',print_out=True)


# Display Results of Closing
f, arr = plt.subplots(1,2)
arr[0].imshow(image, cmap='gray')
arr[1].imshow(close_2, cmap='gray')
plt.show()
print('OPEN2')
latex = a2l.to_ltx(close_2, frmt = '{:1.0f}', arraytype='array',print_out=True)





            
