import pickle
import cv2
import face_recognition
import numpy as np
import requests
import json
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load known face encodings and their names
with open('encodeFile.p', 'rb') as file:
    encodeListKnownWithNames = pickle.load(file)

encodeListKnown, studentsNames = encodeListKnownWithNames
print(studentsNames)

# URL of your Django server's attendance update endpoint
url = 'http://<your-django-server-ip>:8000/attendance/update/'  # Replace with your Django server's IP

# Initialize an empty set to keep track of detected students
detected_students = set()

while True:
    success, img = video_capture.read()
    imgSm = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Detect faces and compute encodings
    faceCurFrame = face_recognition.face_locations(imgSm)
    encodeCurFrame = face_recognition.face_encodings(imgSm, faceCurFrame)

    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        # Identify the best match
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            student_name = studentsNames[matchIndex]
            detected_students.add(student_name)
            print(f'Detected: {student_name}')

    cv2.imshow("face recognition", img)
    cv2.waitKey(1)

    # To break the loop and send data (you can define your own condition)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Prepare the data to send
attendance_data = {
    'students': list(detected_students),  # List of detected students
    'class_id': 'X',  # Replace with actual class ID
    'date': datetime.now().strftime('%Y-%m-%d')  # Current date
}

# Send POST request to the Django server
response = requests.post(
    url,
    data=json.dumps(attendance_data),
    headers={'Content-Type': 'application/json'}
)

if response.status_code == 200:
    print('Attendance data successfully sent.')
else:
    print(f'Failed to send attendance data. Status code: {response.status_code}')

# Release video capture object and close windows
video_capture.release()
cv2.destroyAllWindows()
