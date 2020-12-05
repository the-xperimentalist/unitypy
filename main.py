import cv2
import numpy as np
import face_recognition

imgManmohan = face_recognition.load_image_file("images/manmohan.jpg")
imgManmohanGray = cv2.cvtColor(imgManmohan, cv2.COLOR_BGR2RGB)
imgManmohanTest = face_recognition.load_image_file("images/gandhi.jpg")
imgManmohanTestGray = cv2.cvtColor(imgManmohanTest, cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgManmohanGray)[0]
encodeManmohan = face_recognition.face_encodings(imgManmohanGray)[0]
cv2.rectangle(imgManmohanGray,(faceLoc[3], faceLoc[0]) , (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)

faceLocTest = face_recognition.face_locations(imgManmohanTestGray)[0]
encodeManmohanTest = face_recognition.face_encodings(imgManmohanTestGray)[0]
cv2.rectangle(imgManmohanTestGray, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 0), 2)

# Face distance lower implies match of face encodings
results = face_recognition.compare_faces([encodeManmohan], encodeManmohanTest)
faceDis = face_recognition.face_distance([encodeManmohan], encodeManmohanTest)
print(results, faceDis)
cv2.putText(imgManmohanTestGray, f"{results} {round(faceDis[0], 2)}", (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow('Manmohan Singh', imgManmohanGray)
cv2.imshow('Manmohan Singh test', imgManmohanTestGray)
cv2.waitKey(0)
