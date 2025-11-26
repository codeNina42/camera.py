import cv2

# Open default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot access camera")
    exit()

print("Press 'q' to quit, 's' to save a photo")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        # Quit the camera
        break
    elif key == ord('s'):
        # Save current frame
        cv2.imwrite("capture.png", frame)
        print("Saved capture.png")

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
