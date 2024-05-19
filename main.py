

import cv2
import time
import glob
import os
from emailing import send_email
from threading import Thread


# Capital letter are Algorithms
def clean_folder():
    print("clean function started")
    images = glob.glob("images/*.jpg")
    for image in images:
        os.remove(image)
    print("Clean function ended!")


video = cv2.VideoCapture(0)
# 0 -> for primary camera
# 1 -> for secondary camera
time.sleep(1)
first_frame = None
status_list = []
count = 1
while True:
    status = 0
    check, frame = video.read()

    # Converting to grey
    grey_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # cvt-->convert
    grey_frame_gau = cv2.GaussianBlur(grey_frame, (21, 21), 0)
    # gau--> gaussian blur method
    # 21,21 --> amt of blur
    # 0 --> standard deviation
    if first_frame is None:
        first_frame = grey_frame_gau
    # Stage 5
    # cv2.imshow("My Video", grey_frame_gau)

    delta_frame = cv2.absdiff(first_frame, grey_frame_gau)
    # difference between first_frame and grey_frame_gau shown by whiteness
    # cv2.imshow("My Video", delta_frame)
    # For classification of pixels stage 6
    thresh_frame = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    # To remove fluctuations
    dilate_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("My Video", dilate_frame) Stage 7
    # [1] --> we want to extract 2nd item of list
    # The Threshold value for white pixels 30 or higher
    # Will we inserted and converted into 255
    contours, check = cv2.findContours(dilate_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # To remove extra objects from detection
    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        # Where x,y are coordinates and w,h are width and height of other corners in Stage 8
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))  # -->green colour rectangle
        if rectangle.any():
            # Since rectangle can be more than 1
            status = 1
            cv2.imwrite(f"images/{count}.jpg", frame)
            count += 1
            all_images = glob.glob("images/*.jpg")
            index = int(len(all_images) / 2)
            image_with_object = all_images[index]

    status_list.append(status)
    # ex - [0,0,0,0,1,1,1,0,0]
    status_list = status_list[-2:]
    if status_list[0] == 1 and status_list[1] == 0:
        # , --> so we know it is a tuple not string
        email_thread = Thread(target=send_email, args=(image_with_object,))
        email_thread.daemon = True
        clean_thread = Thread(target=clean_folder)
        clean_thread.daemon = True

        email_thread.start()
    print(status_list)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        # if Press "q" program will stop
        break

video.release()
clean_thread.start()
