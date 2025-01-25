
import imagiz
import cv2

client = imagiz.Client("cc1", server_ip="192.168.137.1")
vid = cv2.VideoCapture(0)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]

while True:
    r, frame = vid.read()
    if r:
        r, image = cv2.imencode('.jpg', frame, encode_param)
        client.send(image)
    else:
        break