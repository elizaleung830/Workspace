import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
footage_socket = context.socket(zmq.SUB)
footage_socket.bind('tcp://192.168.1.182:12379')
footage_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode_(''))

while True:
    try:
        frame = footage_socket.recv_string()
        img = base64.b64decode(frame)

        npimg = np.frombuffer(img,np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break