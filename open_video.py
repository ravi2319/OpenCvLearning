import cv2

cap = cv2.VideoCapture('myvideo.mkv')

if cap.isOpened() == False:
    print('Error! Check Path')

while cap.isOpened() == True:

    ret, frame = cap.read()

    if ret == True:

        cv2.imshow('Frame', frame)

    if cv2.waitKey(15) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()