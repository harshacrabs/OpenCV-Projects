import cv2

# Open the video file
video = cv2.VideoCapture('../videos/bikes.mp4')

# Optional: Resize dimensions
target_width = 640
target_height = 360

while True:
    check, frame = video.read()

    if check:
        # 1. Resize the frame
        frame = cv2.resize(frame, (target_width, target_height))

        # 2. Convert to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 3. Display both color and grayscale
        # cv2.imshow('Color Output', frame)
        cv2.imshow('Grayscale Output', gray_frame)

        # 4. Wait for 30ms between frames (controls FPS)
        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
    else:
        break

# 5. Release resources
video.release()
cv2.destroyAllWindows()