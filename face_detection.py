import cv2

face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    print(ret)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_rectangle = face_detection.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rectangle:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow('Face Detection Video', frame)

    if cv2.waitKey(3) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

