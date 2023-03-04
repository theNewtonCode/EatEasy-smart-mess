import requests
import cv2
import numpy as np
import imutils

# Getting Image and store it
def get_image(url):
    # Setting the URL of the CCTV camera's web interface(Generic Case-Later Delete it!)
    url = "http://XX.XX.XX.XXX:8080/shot.jpg"
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    
    # Storing the image in Caputres Folder as Android_cam.jpg
    cv2.imwrite("EatEasy-smart-mess/captures/Android_cam.jpg", img)

