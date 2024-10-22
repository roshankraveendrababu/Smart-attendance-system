import cv2
import pickle
import pandas as pd
from datetime import datetime

# Load saved features and names using pickle
with open('features.pkl', 'rb') as f:
    saved_features = pickle.load(f)

with open('names.pkl', 'rb') as f:
    saved_names = pickle.load(f)

# Initialize ORB and BFMatcher
orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Set to keep track of marked attendance in the current session
marked_attendance = set()

def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime('%Y-%m-%d')
    time_str = now.strftime('%H:%M:%S')

    # Create or append to Attendance.xlsx
    file_name = 'Attendance.xlsx'
    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Name', 'Date', 'Time'])

    # Check if attendance is already marked for the same date
    if not ((df['Name'] == name) & (df['Date'] == date_str)).any():
        df = pd.concat([df, pd.DataFrame([[name, date_str, time_str]], columns=['Name', 'Date', 'Time'])], ignore_index=True)
        df.to_excel(file_name, index=False)
        print(f"Attendance marked for {name}")

def recognize_face():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            face_img = gray[y:y + h, x:x + w]
            keypoints, descriptors = orb.detectAndCompute(face_img, None)

            if descriptors is not None:
                best_match_name = "Unknown"
                best_match_count = 0

                for saved_descriptors, name in zip(saved_features, saved_names):
                    matches = bf.match(descriptors, saved_descriptors)
                    if len(matches) > best_match_count:
                        best_match_count = len(matches)
                        best_match_name = name

                if best_match_name != "Unknown" and best_match_name not in marked_attendance:
                    mark_attendance(best_match_name)
                    marked_attendance.add(best_match_name)  # Add to set to prevent re-entry

                cv2.putText(frame, best_match_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) == 27:  # Stop on Esc key
            break

    cap.release()
    cv2.destroyAllWindows()

# Start recognizing faces
recognize_face()




