import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap=cv2.VideoCapture(0)
clientsocket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM,0)
clientsocket.connect(('fe80::b79e:dfb1:2fee:350c',8089,0,0))

while True:
    ret,frame=cap.read()
    # Serialize frame
    data = pickle.dumps(frame)

    # Send message length first
    message_size = struct.pack("L", len(data)) ### CHANGED

    # Then data
    clientsocket.sendall(message_size + data)
