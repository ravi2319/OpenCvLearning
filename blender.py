<<<<<<< HEAD
from __future__ import print_function
import cv2

alpha = 0.5

print('''Simple Linear Blender
----------------------
*Enter alpha [0.0-1.0]: ''')
input_alpha = float(input().strip())

if 0 <= alpha <= 1:
    alpha = input_alpha

src1 = cv2.imread('images\LinuxLogo.jpg')
src2 = cv2.imread('images\WindowsLogo.jpg')

if src1 is None:
    print("Error Loading Image1")

elif src2 is None:
    print("Error loading Image2")

#blend images

beta = (1.0 - alpha)

dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)

cv2.imshow('dst', dst)
cv2.waitKey(0)

=======
from __future__ import print_function
import cv2

alpha = 0.5

print('''Simple Linear Blender
----------------------
*Enter alpha [0.0-1.0]: ''')
input_alpha = float(input().strip())

if 0 <= alpha <= 1:
    alpha = input_alpha

src1 = cv2.imread('images\LinuxLogo.jpg')
src2 = cv2.imread('images\WindowsLogo.jpg')

if src1 is None:
    print("Error Loading Image1")

elif src2 is None:
    print("Error loading Image2")

#blend images

beta = (1.0 - alpha)

dst = cv2.addWeighted(src1, alpha, src2, beta, 0.0)

cv2.imshow('dst', dst)
cv2.waitKey(0)

>>>>>>> 9e0d3764d29205fcc0158b5fbb79f489e1e33a24
cv2.destroyAllWindows()