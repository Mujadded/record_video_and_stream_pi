# Raspberry Pi Camera Module Video Recording and Streaming

This simple program allows you to record video using the Raspberry Pi camera module and stream it to a web interface. The code consists of two main files: `record.py` for video recording and `capture_and_stream.py` for web streaming.

## `record.py`

The `record.py` file captures video from the Raspberry Pi camera module and records it to a local file. It also provides a callback function for further processing the captured frames. The video is saved in the AVI format, and the recorded video files are stored in the "captured_video" directory.

### Dependencies
- OpenCV (`cv2`)
- picamera2

### Usage

To start video recording using the Raspberry Pi camera module, you can use the `start` function provided in this file.

```python
from record import start

# Your callback function to process captured frames
def callback_function(frame):
    # Process the frame as needed
    pass

# Start video recording and processing
start(callback_function)
```

## `capture_and_stream.py`

The `capture_and_stream.py` file creates a Flask web application for streaming the recorded video in real-time. The web interface allows you to view the live video stream from the Raspberry Pi camera.

### Dependencies
- Flask
- OpenCV (`cv2`)

### Usage

1. Run the Flask application using the following command:

```bash
python capture_and_stream.py
```

2. Open a web browser and navigate to `http://<your_raspberry_pi_ip>:5000/` to view the live video stream.

### Routes
- `/`: Home page with the video stream.
- `/video_feed`: Video streaming route used in the `<img>` tag on the home page.

### Important Notes
- The video stream is accessible over your local network. Ensure your Raspberry Pi is on the same network, and you have the Pi's IP address.
- The video streaming may not work securely over the internet without additional configurations (port forwarding, security measures, etc.).

## About

This project provides a simple way to record video with the Raspberry Pi camera module and view it in real-time through a web interface. You can customize the code to meet your specific needs, such as saving video files, processing frames, or enhancing the web interface. Enjoy capturing and streaming videos with your Raspberry Pi!