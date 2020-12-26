# Udp client to send messages.

import cv2
import socket

img = cv2.imread('nature.jpg')

# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# img = cv2.resize(img, (480, 360))

# print(type(img))

# convert np arr to string

img_string = img.tostring()

print(img_string)
print(type(img_string))
print(len(img_string))


# msgFromClient = "Hello UDP Server"
#
# bytesToSend = str.encode(msgFromClient)
#
serverAddressPort = ("127.0.0.1", 20001)
#
bufferSize = 1024

# Create a UDP socket at client side
# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPClientSocket.connect(("127.0.0.1", 20001))

UDPClientSocket.send(img_string)
# Send to server using created UDP socket



# UDPClientSocket.sendto(img_string, serverAddressPort)

# msgFromServer = UDPClientSocket.recvfrom(bufferSize)

# msg = "Message from Server {}".format(msgFromServer[0])

# print(msg)
