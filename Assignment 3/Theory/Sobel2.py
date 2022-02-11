import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

G = [[0,0,0,0,0,0,0,0],
     [0,127,127,127,0,0,0,0],
     [0,0,127,127,127,0,0,0],
     [0,0,0,80,80,80,0,0],
     [0,0,0,0,127,127,127,0],
     [0,0,0,0,0,127,127,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

magnitude = [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

angle = [[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]


# Loop through, perform edge detection
for row in range(1,7):
    print('0\\angle0&')
    for col in range(1,7):
        dx = 0
        dy = 0
        # Constant Col
        dx += G[row-1][col+1] - G[row-1][col-1]
        dx += (G[row][col+1] - G[row][col-1])*2
        dx += G[row+1][col+1] - G[row+1][col-1]
        # Constant Row
        dy += G[row-1][col-1] - G[row+1][col-1]
        dy += (G[row-1][col] - G[row+1][col])*2
        dy += G[row-1][col+1] - G[row+1][col+1]
                
        magnitude[row][col] = round(math.sqrt(dx**2+dy**2),1)        
        angle[row][col] = round(math.atan2(dy,dx)*180/math.pi,1)
        if angle[row][col] < 0:
            angle[row][col] += 360

        # Print out magnitude and angle, formatted for latex
        print(str(magnitude[row][col])+'\\angle'+str( round(angle[row][col]))+'&')
    # Zero Padding        
    print('0\\angle0\\\\')    
    print()

### Non maximum supression     
sup=[[0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0],
     [0,0,0,0,0,0,0,0]]

for i in range(1,7):
    for j in range(1,7):
        
        q = 255
        r = 255       
        #  ---
        if (0 <= angle[i][j] < 22.5) or (337.5 <= angle[i][j] <= 360) or (180-22.5 <= angle[i][j] < 180+22.5):
            q = magnitude[i][ j+1]
            r = magnitude[i][ j-1]
        #  ///
        elif (22.5 <= angle[i][j] < 67.5) or (225-22.5 <=angle[i][j] < 225+22.5):
            q = magnitude[i+1][ j-1]
            r = magnitude[i-1][ j+1]
        #  |||
        elif (67.5 <= angle[i][j] < 112.5) or (270-22.5 <=angle[i][j] < 270+22.5):
            q = magnitude[i+1][ j]
            r = magnitude[i-1][ j]
        #  \\\
        elif (112.5 <= angle[i][j] < 157.5) or (315-22.5 <=angle[i][j] < 315+22.5):
            q = magnitude[i-1][ j-1]
            r = magnitude[i+1][ j+1]
        else:
            print('ERROR ERROR ERROR ERROR ERROR')

        if (magnitude[i][j] >= q) and (magnitude[i][j] >= r):
            sup[i][j] = magnitude[i][j]
            
        else:
            sup[i][j] = 0

### Normalize Values, 0-255
max = 0
for i in range(1,7):
    for j in range(1,7):
        if sup[i][j] > max:
            max = sup[i][j]

for i in range(1,7):
    for j in range(1,7):
        sup[i][j] = int((sup[i][j] / max) * 255) 

print('===================')
print('supression')


# printout for latex 
for i in range(1,7):
    print('0&',end='')        # Zero Pad
    for j in range(1,7):
        print(str(sup[i][j])+'&',end='')
    print('0\\\\')     # Zero Pad
    print()


# Hysteresis Thresholding
for i in range(1,7):
    for j in range(1,7):
        if sup[i][j] >= 120:  # Strong
            sup[i][j] = 1
        elif sup[i][j] > 20:  # Weak
            sup[i][j] = 'W'
        else:                 # Non Relevant
            sup[i][j] = 0

for i in range(1,7):
    for j in range(1,7):
        if sup[i][j] == 'W':
            if (sup[i-1][j-1]+sup[i-1][j]+sup[i-1][j+1]+sup[i][j-1]+ \
                    sup[i][j+1]+sup[i+1][j-1]+sup[i+1][j]+sup[i+1][j+1]) > 0:
                sup[i][j] = 1
            else:
                sup[i][j] = 0

print('===================')
print('hysteresis')
# printout for latex 
for i in range(1,7):
    print('0&',end='')        # Zero Pad
    for j in range(1,7):
        print(str(sup[i][j])+'&',end='')
    print('0\\\\')     # Zero Pad
    print()

'''            
array = np.array(sup)
plt.imshow(array, cmap='gray')
plt.show()
'''
