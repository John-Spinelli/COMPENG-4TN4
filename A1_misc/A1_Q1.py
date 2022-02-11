''' Johnathan Spinelli, A1_Q1 '''
import cv2

orig_img = cv2.imread('img1.png', 1)

angle = int(input("Enter angle: 0, 90, 180, 270   "))

if (angle == 0):
    cv2.imshow('output',orig_img)
    cv2.imwrite("0_degrees.jpg",orig_img)
elif (angle == 90):
    image = cv2.rotate(orig_img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imshow('output',image)
    cv2.imwrite("90_degrees.jpg",image)
elif (angle == 180):
    image = cv2.rotate(orig_img, cv2.ROTATE_180)
    cv2.imshow('output',image)
    cv2.imwrite("180_degrees.jpg",image)
else :
    image = cv2.rotate(orig_img, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imshow('output',image)
    cv2.imwrite("270_degrees.jpg",image)


