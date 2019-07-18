import picamera

with picamera.PiCamera() as cam:
    print(cam.MAX_RESOLUTION)
