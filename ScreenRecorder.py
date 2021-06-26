from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
ts = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
fn = f'{ts}.mp4'
video_capture = cv2.VideoWriter(fn, fourcc, 20.0, (width, height))

print(width)
print(height)

cam = cv2.VideoCapture(0)

while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_np = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    
    _, frame = cam.read()
    fh, fw, _ = frame.shape
    
    img_np[height-fh:, width-fw:, :] = frame[0:fh, 0:fw, :]
    
    cv2.imshow('Screen Recorder', img_np)
    video_capture.write(img_np)
    if cv2.waitKey(10) == ord('q'):
        break