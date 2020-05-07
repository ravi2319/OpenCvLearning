<<<<<<< HEAD
import cv2

img = cv2.imread('abc.png')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',grey)
=======
import cv2

img = cv2.imread('abc.png')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',grey)
>>>>>>> 9e0d3764d29205fcc0158b5fbb79f489e1e33a24
cv2.waitKey()