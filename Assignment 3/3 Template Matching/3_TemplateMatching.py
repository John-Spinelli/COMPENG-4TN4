import numpy as np
import cv2
from matplotlib import pyplot as plt
import math

##### MY WAY #####
def heat_map(img, template):

    # Modify template and image
    template = cv2.bitwise_not(template)
    t_height, t_width = template.shape
    
    edges = cv2.Canny(img,100,200)
    height, width = img.shape
    
    temp_avg = template.mean()
    heatmap = np.zeros((height,width))

    # Normalized Cross Correlation
    for row in range(t_height // 2, height - (t_height//2) - 1):
        for col in range(t_width // 2, width - (t_width//2) - 1):

            # Take slice of image
            slice = edges[row-t_height//2:row+t_height//2+1,col-t_width//2: col+t_width//2]
            slice_avg = slice.mean()

            # Equation:  sum( X * Y ) / sqrt( sum(X^2) * sum(Y^2) )
            #             ^^^ A ^^^            ^^B         ^^^ C 
            
            A = ((template-temp_avg)*(slice-slice_avg)).sum()
            B = ((template-temp_avg)**2).sum()
            C = ((slice-slice_avg)**2).sum()

            # Calculate heat value
            heatmap[row,col] = A / np.sqrt(B*C)
            
    # Tidy Up
    heatmap[np.isnan(heatmap)] = 0
    return heatmap
    
##### matchTemplate Method ######
def tempMatch(img, template):
    edges = cv2.Canny(img,100,200)
    template = cv2.bitwise_not(template)
    result = cv2.matchTemplate(edges,template,cv2.TM_CCOEFF_NORMED)
    return result

# Quick scaled dimensions
def scaleFunc(img, factor):
    width = int(img.shape[1] * factor)
    height = int(img.shape[0] * factor)
    return (width, height)

# Read images
image = cv2.imread("messi.jpg")
img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('original', img)
template = cv2.imread('circle.bmp',0)
cv2.imshow('template',template)


# Heat Mapping original size
res1 = heat_map(img, template)
res2 = tempMatch(img, template)
plt.imshow(res1,cmap = 'gray')
plt.show()
plt.imshow(res2,cmap = 'gray')
plt.show()


##### Scaled Image, match w/ unknown size#####
given_col = cv2.resize(image, scaleFunc(image,2))
given = cv2.cvtColor(given_col, cv2.COLOR_BGR2GRAY)
template = cv2.imread('circle.bmp',0)
template = cv2.Canny(template,50,200)

t_h, t_w = template.shape[0:2]

match = None
# Resize and compare template
for scale in np.linspace(0.25, 1.0, 20)[::-1]:
    smaller = cv2.resize(given, scaleFunc(given,scale))
    up_ratio = given.shape[1] / float(smaller.shape[1])

    # Resized image must be bigger than template
    if t_h > smaller.shape[0] or t_w > smaller.shape[1]:
        break

    # Match template, get location of max correlation
    edges = cv2.Canny(smaller, 50,200)
    result = cv2.matchTemplate(edges, template, cv2.TM_CCOEFF)
    (_, correl, _, correl_loc) = cv2.minMaxLoc(result)

    # New match?
    if match is None or correl > match[0]:
        match = (correl, correl_loc, up_ratio)

_, location, up_ratio = match

# New heatmap with scaled template
template = cv2.imread('circle.bmp',0)
template = cv2.resize(template, scaleFunc(template,up_ratio))
res3 = tempMatch(given, template)
plt.imshow(res3, cmap = 'gray')
plt.show()

# Upscale the coordinate for the matched template
x_min = int(location[0]*up_ratio)
y_min = int(location[1]*up_ratio)
x_max = int((location[0]+t_w)*up_ratio)
y_max = int((location[1]+t_h)*up_ratio)

# Plot bounding box for estimated position
cv2.rectangle(given_col, (x_min,y_min), (x_max,y_max), (0,0,255), 2)
cv2.imshow("Detected Image",given_col)
cv2.imwrite("scaled_detected_image.png",given_col)

cv2.waitKey(0)
cv2.destroyAllWindows()
