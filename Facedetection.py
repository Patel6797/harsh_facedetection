import face_recognition
import cv2
import os
import csv

# Directory containing photos of known individuals with their names as filenames
known_faces_dir = 'known_faces'

def load_person_info(csv_file):
    person_data = {}
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)  # Using DictReader for easier column access
            for row in reader:
                name = f"{row['First Name']} {row['Last Name']}"  # Full name
                person_data[name] = {
                    'Address': row['Address'],
                    'SSN': row['SSN'],
                    'DOB': row['DOB']  # Date of Birth
                }
    except Exception as e:
        print(f"Error reading CSV file: {e}")
    return person_data

data = load_person_info('person_info.csv')

def load_known_faces(known_faces_dir):
    if not os.path.exists(known_faces_dir):
        raise FileNotFoundError(f"The directory '{known_faces_dir}' does not exist.")

    known_faces = []
    known_face_names = []

    for filename in os.listdir(known_faces_dir):
        if filename.lower().endswith((".jpg", ".png")):
            image_path = os.path.join(known_faces_dir, filename)
            try:
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)
                if encoding:
                    known_faces.append(encoding[0])
                    known_face_names.append(filename[:-4])
                else:
                    print(f"No face encoding found in image {filename}.")
            except Exception as e:
                print(f"Error processing image {filename}: {e}")

    return known_faces, known_face_names

known_faces, known_face_names = load_known_faces(known_faces_dir)

cap = cv2.VideoCapture(0)
output_folder = 'captured_photos'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from camera.")
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces, face_encoding)
        name = "Unknown"
        address = ""
        ssn = ""
        dob = ""

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]
            if name in data:
                person_info = data[name]
                address = person_info['Address']
                ssn = person_info['SSN']
                dob = person_info['DOB']

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, f'Name: {name}', (left + 6, bottom - 80), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'Address: {address}', (left + 6, bottom - 60), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'SSN: {ssn}', (left + 6, bottom - 40), font, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, f'DOB: {dob}', (left + 6, bottom - 20), font, 0.5, (255, 255, 255), 1)

        height, width = frame.shape[:2]
        top = max(0, top)
        right = min(width, right)
        bottom = min(height, bottom)
        left = max(0, left)
        captured_frame = frame[top:bottom, left:right]

        if captured_frame.size == 0:
            print("Captured frame is empty. Skipping save.")
        else:
            photo_name = os.path.join(output_folder, f'{name}_photo.jpg')
            cv2.imwrite(photo_name, captured_frame)
            print(f'Photo saved as: {photo_name}')

    cv2.imshow('CCTV Feed with Face Recognition', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
