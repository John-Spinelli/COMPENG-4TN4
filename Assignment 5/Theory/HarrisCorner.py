import cv2
import numpy as np
from matplotlib import pyplot as plt
import array_to_latex as a2l

img = [[0,0,0,0,0],
       [0,255,255,255,0],
       [0,255,255,255,0],
       [0,255,255,255,0],
       [0,0,0,0,0]]

image = np.array(img)

latex = a2l.to_ltx(image, frmt = '{:1.0f}', arraytype='array',print_out=True)

