import os
import cv2
import numpy as np
import face_recognition
import argparse

parser = argparse.ArgumentParser(description="Add input images folder")
parser.add_argument("--folder", type=str, default="./images", help="Add path of the folder")
args = parser.parse_args()

path = args.folder
imagesList = []
personsNames = []
myList = os.listdir(path)

for item in myList:
    curImg = cv2.imread(f"{path}/{item}")
    imagesList.append(curImg)
    personsNames.append(item.replace(".jpg", ""))

print(personsNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        enodeImg = face_recognition.face_encodings(img)[0]
        encodeList.append(enodeImg)

    return encodeList

encodeListKnown = findEncodings(imagesList)
print("Encodings known now!")

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS, faceCurrentFrame)

    for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(matches, faceDis)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personsNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            cv2.putText(imgS, name, (int((x1+x2)/8), int((y1+y2)/8)), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Webcam", imgS)
    cv2.waitKey(1)
