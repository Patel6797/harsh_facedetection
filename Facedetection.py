import face_recognition
import cv2
import os
import csv
import numpy as np
from PIL import Image

# Directory containing photos of known individuals with their names as filenames
known_faces_dir = 'known_faces'

data = {}

# Load the CSV data and store it in the 'data' dictionary
with open('person_info.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # skip the header row
    for row in reader:
        key = f"{row[0]} {row[1]}"  # Full name (assuming First Name and Last Name columns)
        value = {
            'Address': row[2],
            'SSN': row[3]
        }
        data[key] = value

# Load known faces and their names
known_faces = []
known_face_names = []

for filename in os.listdir(known_faces_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(known_faces_dir, filename)
        
        # Open the image using PIL
        pil_image = Image.open(image_path).convert("RGB")
        
        # Convert the PIL image to a numpy array
        image = np.array(pil_image)
        
        # Get face encodings
        encodings = face_recognition.face_encodings(image)

        if len(encodings) > 0:
            known_faces.append(encodings[0])
            known_face_names.append(filename[:-4])
        else:
            print(f"No faces found in image: {image_path}")

# Open a connection to your camera (0 for default camera, or provide the camera index)
cap = cv2.VideoCapture(0)

photo_captured = False  # Flag to control photo capture

# Specify the folder path where you want to save the captured photos
output_folder = 'captured_photos'

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert the camera frame from BGR to RGB (face_recognition expects RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all face locations in the frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each detected face
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Compare the detected face with known faces
        matches = face_recognition.compare_faces(known_faces, face_encoding)

        name = ""
        address = ""
        ssn = ""

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if name in data:
                person_info = data[name]
                address = person_info['Address']
                ssn = person_info['SSN']

        # Draw a rectangle and name label around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, f'Name: {name}', (left + 6, bottom - 60), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'Address: {address}', (left + 6, bottom - 40), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'SSN: {ssn}', (left + 6, bottom - 20), font, 0.5, (255, 255, 255), 1)

        # Capture and save the photo with information
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Capture and save the photo with information
        captured_frame = frame[top:bottom, left:right]
        photo_name = os.path.join(output_folder, f'{name}_photo.jpg')
        cv2.imwrite(photo_name, captured_frame)
        print(f'Photo saved as: {photo_name}')

        photo_captured = True

    cv2.imshow('CCTV Feed with Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
