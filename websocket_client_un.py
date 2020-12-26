#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import cv2


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # path = '.images'
        # os.listdir(path)

        img = cv2.imread('./images/gandhi.jpg')
        # img_string = img.tostring()
        img_string = cv2.imencode('.jpg', img)[1].tostring()

        print(img_string)
        print(type(img_string))
        print(len(img_string))

        await websocket.send(img_string)
        print(f"> {img_string}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

asyncio.get_event_loop().run_until_complete(hello())
