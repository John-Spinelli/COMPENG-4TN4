import cv2

orig_img = cv2.imread('Headshot.jpg', 1)

img = (orig_img * 0.5).astype('uint8')

# print channel 1 (green) for pixels in this range
print(img[3:15, 5:10, 1])

cv2.imshow('Output', img)
