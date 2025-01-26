import pickle
import socket
import struct

import cv2

HOST = '192.168.1.182'
PORT = 12379

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(5)
print('Socket now listening')

conn, addr = s.accept()
print(f"{conn}, {addr}")
data = b'' ### CHANGED
payload_size = struct.calcsize("L") ### CHANGED

while True:

    print("Start Receving")
    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(4096)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(4096)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    print("Displaying")
    cv2.imshow('frame', frame)
    cv2.waitKey(1)