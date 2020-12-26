#!/usr/bin/env python

# WS server example

import asyncio
import cv2
import face_recognition
import numpy as np
import os
import websockets


class WebsocketHelper:

    def __init__(self):
        """
        Init method to read all the images in the folder.
        """
        self.path = "./images"
        self.imagesList = []
        self.personsNames = []
        self.myList = os.listdir(self.path)
        self.encodeListKnown = []
        self._create_person_name_array()
        self.__find_encodings()
        print(self.personsNames)
        print(self.encodeListKnown)


    def _create_person_name_array(self):
        """
        Create the array for person's name
        :return:
        """
        for item in self.myList:
            cur_img = cv2.imread(f"{self.path}/{item}")
            self.imagesList.append(cur_img)
            self.personsNames.append(item.replace(".jpg", ""))

    def __find_encodings(self):
        """
        Find encoding method.
        :return:
        """
        for img in self.imagesList:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode_img = face_recognition.face_encodings(img)[0]
            self.encodeListKnown.append(encode_img)

    def register(self):
        """
        #TODO: Add functionality to this when there will be more than 1 client. We would register the client.
        """
        pass

    async def generate_image(self, websocket, path):
        """
        Capture the byte string of the image.
        """

        print(websocket)
        img = await websocket.recv()
        print(f'len of img={len(img)}')

        nparr = np.frombuffer(img, np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        print(img)

        img_s = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        img_s = cv2.cvtColor(img_s, cv2.COLOR_BGR2RGB)

        faceCurrentFrame = face_recognition.face_locations(img_s)
        encodeCurrentFrame = face_recognition.face_encodings(img_s, faceCurrentFrame)

        for encodeFace, faceLoc in zip(encodeCurrentFrame, faceCurrentFrame):
            matches = face_recognition.compare_faces(self.encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(self.encodeListKnown, encodeFace)
            print(matches, faceDis)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = self.personsNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                cv2.putText(img_s, name, (int((x1 + x2) / 8), int((y1 + y2) / 8)), cv2.FONT_HERSHEY_COMPLEX, 1,
                            (0, 255, 0), 2)

        cv2.imshow("Webcam", img_s)
        cv2.waitKey(1)




web = WebsocketHelper()
start_server = websockets.serve(web.generate_image, "localhost", 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
