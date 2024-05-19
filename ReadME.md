# Webcam Motion Detector

## Overview

The Webcam Motion Detector is a Python application designed to monitor a specified area using a webcam. When motion is detected within the camera's field of view, the application captures an image and sends an email notification to the user with the captured image attached. This tool is ideal for home security, office monitoring, or any other scenario where you need to keep an eye on a space remotely.

## Features

- **Real-time Motion Detection**: Continuously monitors the webcam feed for any movement.
- **Email Notifications**: Sends an email alert with an attached image when motion is detected.
- **Configurable Sensitivity**: Adjusts the sensitivity of motion detection to reduce false positives.
- **Image Capture**: Captures and saves an image whenever motion is detected.
- **Logging**: Logs all motion events with timestamps for easy tracking.

## Requirements

- Python 3.x
- OpenCV (cv2)
- Numpy
- smtplib
- email
- imutils (optional, for easier image processing)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Namesisneo/Webcam-Motion-Detector.git
   cd Webcam-Motion-Detector
