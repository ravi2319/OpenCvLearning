import cv2
import numpy as np
from builtins import input


img = cv2.imread('images\WindowsLogo.jpg')
new_img = np.zeros(img.shape, img.dtype)

alpha = 1.0
beta = 0

print('Basic Linear Transitions')
print('------------------------')
try:
    alpha = float(input("Enter the alpha value [1.0-3.0]: "))
    beta = int(input('Enter the beta value [0-100]: '))
except ValueError:
    print('Error not a number')

for y in range(img.shape[0]):
    for x in range(img.shape[1]):
        for z in range(img.shape[2]):
            new_img[y,x,z] = np.clip(alpha*img[y,x,z] + beta, 0, 255)

## Or instead of lines 27 to 30 use
#new_img = cv2.convertScaleAbs(alpha=alpha,beta=beta)

cv2.imshow('Original Image', img)
cv2.imshow('New Image', new_img)

cv2.waitKey()