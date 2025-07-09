import cv2


cap = cv2.VideoCapture('videos/demo.mp4')

Number_Plate_Cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_russian_plate_number.xml')

count = 0

while True:
    success, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    if not success:
        break
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    number_plates = Number_Plate_Cascade.detectMultiScale(gray_frame, 1.1, 4)
    for (x,y,w,h) in number_plates:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
        cv2.putText(frame, 'Number Plate', (x,y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        frameROI = frame[y:y+h, x:x+w]
    cv2.imshow('ROI', frameROI)
        
    cv2.imshow('Number Plate Detection', frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()