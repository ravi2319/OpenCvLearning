import cv2

img = cv2.imread('abc.png')
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('image',grey)
cv2.waitKey()