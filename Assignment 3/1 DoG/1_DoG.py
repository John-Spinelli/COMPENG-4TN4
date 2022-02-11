import cv2
import numpy as np

plate = cv2.imread('lp.jpg')
#Change the scale for testing different sizes of image
#plate = cv2.resize(plate, (int(plate.shape[1]*.1),int(plate.shape[0]*.1)))

# Produce list of different kernal sizes
blurs = []
blurs.append(cv2.GaussianBlur(plate,(3,3),0))
blurs.append(cv2.GaussianBlur(plate,(5,5),0))
blurs.append(cv2.GaussianBlur(plate,(7,7),0))
blurs.append(cv2.GaussianBlur(plate,(9,9),0))
blurs.append(cv2.GaussianBlur(plate,(11,11),0))
blurs.append(cv2.GaussianBlur(plate,(13,13),0))
blurs.append(cv2.GaussianBlur(plate,(15,15),0))
blurs.append(cv2.GaussianBlur(plate,(17,17),0))
blurs.append(cv2.GaussianBlur(plate,(19,19),0))

# Run loop to test different kernal sizes
'''
for i in range(8):
    for j in range(i+1,9):
        print(i,j)
        diff = cv2.subtract(blurs[j], blurs[i])
        cv2.imshow(str(i)+' minus '+str(j),diff)
'''
# Just edges
edges = cv2.subtract(blurs[2],blurs[0])*7
edges = cv2.cvtColor(edges, cv2.COLOR_BGR2GRAY)
cv2.imshow('edgessss',edges)
cv2.imwrite('just_edges.png',edges)

# 19x19 vs 3x3 was the best result
filtered = cv2.subtract(blurs[8],blurs[0])
cv2.imshow("best",filtered)
cv2.imwrite('filtered_plate.png',filtered)
grayscale  = cv2.cvtColor(filtered,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',grayscale)
cv2.imwrite('grayscale.png',grayscale)
norm = grayscale*3
cv2.imshow('norm',norm)
cv2.imwrite('norm.png',norm)

'''
# Adjusting thresholds
gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,140,220)
cv2.imshow("cannya",edges)
edges = cv2.Canny(gray,140,240)
cv2.imshow("cannyb",edges)
edges = cv2.Canny(gray,140,260)
cv2.imshow("cannyc",edges)
'''

gray2 = cv2.cvtColor(blurs[0],cv2.COLOR_BGR2GRAY)
'''
# Adjusting threshold, with preprocessing
edges2 = cv2.Canny(gray2,140,220)
cv2.imshow("canny2a",edges2)
edges2 = cv2.Canny(gray2,140,240)
cv2.imshow("canny2b",edges2)
'''
# Display best thresholding w preprocessing
edges2 = cv2.Canny(gray2,140,260)
cv2.imshow("canny2c",edges2)
cv2.imwrite("canny_op.png", edges2)
