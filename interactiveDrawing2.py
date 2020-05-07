import cv2

def draw_circle(event, x, y, flags, param):

    global center, clicked

    if event == cv2.EVENT_LBUTTONDOWN:
        center = (x,y)
        clicked = False

    if event == cv2.EVENT_LBUTTONUP:
        clicked = True

center = (0,0)
clicked = False

cap = cv2.VideoCapture(0)

cv2.namedWindow('Testing')

cv2.setMouseCallback('Testing', draw_circle)

while True:

    ret, frame = cap.read()

    if clicked:

        cv2.circle(frame, center=center, radius=50, color=(255,0,255), thickness=3)

    cv2.imshow('Testing', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()