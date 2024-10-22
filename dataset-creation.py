import cv2
import os

# Load Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Create a dataset folder
dataset_path = 'dataset'
os.makedirs(dataset_path, exist_ok=True)

def capture_face_images(user_name):
    cap = cv2.VideoCapture(0)
    img_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img_count += 1
            face_img = frame[y:y + h, x:x + w]
            # Save the face image in the dataset folder
            cv2.imwrite(f"{dataset_path}/{user_name}_{img_count}.jpg", face_img)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Capturing Face", frame)

        if cv2.waitKey(1) == 27 or img_count >= 10:  # Esc key or 10 images limit
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Captured {img_count} images for {user_name}")

# Usage
user_name = input("Enter your name: ")
capture_face_images(user_name)


