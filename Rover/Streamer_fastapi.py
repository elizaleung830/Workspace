import cv2
import time
import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import StreamingResponse

app = FastAPI()
camera = cv2.VideoCapture(0)  # init the camera
templates = Jinja2Templates(directory="templates")


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        time.sleep(0.03)


@app.get('/')
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/video_feed')
def video_feed():
    return StreamingResponse(gen_frames(), media_type='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    uvicorn.run(app, host='192.168.1.144', port=12379)
