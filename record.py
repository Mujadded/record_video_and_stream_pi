import cv2
from datetime import datetime
from picamera2 import Picamera2

# Frame shape
_FRAME_WEIGHT, _FRAME_HEIGHT = 1024, 768


def start(callback_function):
    # Initiating camera instance
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (_FRAME_WEIGHT, _FRAME_HEIGHT)}))
    picam2.start()

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc('F','M','P','4')
    video_name= f"./captured_video/{datetime.today().strftime('%Y%m%d%H%M%S')}.avi"

    # FPS for recording video. Setting 6 as the real fps is 6 to 7
    fps = 12.0
    # Video Recorder instance
    out = cv2.VideoWriter(video_name,fourcc, fps, (_FRAME_WEIGHT, _FRAME_HEIGHT))
    
    while(True):
        # Grab frame from video stream
        image = picam2.capture_array()

            # Converting the image from 640x480x4 to 640x480x3
        output_image=cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        out.write(output_image)
        cv2.imshow('Pose detector', image)
        callback_function(output_image)
        # Key to quite display
        if cv2.waitKey(1) == ord('q'):
            break
    out.release()

    

