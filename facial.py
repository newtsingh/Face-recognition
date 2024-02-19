import face_recognition
import cv2


known_image = face_recognition.load_image_file("known_person.jpg")


known_image_encoding = face_recognition.face_encodings(known_image)[0]


unknown_image = face_recognition.load_image_file("unknown_person.jpg")


unknown_image_encoding = face_recognition.face_encodings(unknown_image)[0]


results = face_recognition.compare_faces([known_image_encoding], unknown_image_encoding)

if results[0] == True:
    print("Known person detected!")
else:
    print("Unknown person detected!")
