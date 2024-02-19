import face_recognition
import cv2

# Load the image of the known person
known_image = face_recognition.load_image_file("known_person.jpg")

# Encode the known image
known_image_encoding = face_recognition.face_encodings(known_image)[0]

# Load the image to be recognized
unknown_image = face_recognition.load_image_file("unknown_person.jpg")

# Encode the unknown image
unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]

# Compare faces
results = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)

if results[0] == True:
    print("Known person detected!")
else:
    print("Unknown person detected!")