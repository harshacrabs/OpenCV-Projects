import cv2

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

while True:
    success, frame = cap.read()
    if not success:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_frame, 1.1, 4) # (image, scaleFactor, minNeighbors)

    for (x,y,w,h) in faces:
        cv2.rectangle(gray_frame, (x,y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow('Video', gray_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()