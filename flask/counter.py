from PIL import Image
import os
from testpy import object_detection_with_bounding_boxes as count_people
from cctv import get_image
import os
import cv2
import numpy as np


def find_counter():
    
    # Dictionary to keep count of people on specific counters and also images related to them
    counter_dict = {"hotspot_counter":["hotspot_counter.jpg",0,"hotspot_counter_map.jpg"],
                    "hostel_counter":["hostel_counter.jpg",0,"hostel_counter_map.jpg"],
                    # "football_counter":["spicy_counter.jpg",0,"football_counter_map.jpg"],
                    # "spicy_counter":["spicy_counter.jpg",0,"spicy_counter_map.jpg"],
                    }
    
    image_names = ["hotspot_counter", "hostel_counter", "football_counter", "spicy_counter"]
    image_name = ["hotspot_counter.jpg", "hostel_counter.jpg", "football_counter.jpg", "spicy_counter.jpg"]
    urls = ["http://10.12.46.193:8080/shot.jpg", "http://10.12.34.208:8080/shot.jpg", "http://XX.XX.XX.XXX:XXXX/shot.jpg", "http://XX.XX.XX.XXX:XXXX/shot.jpg"]

    # Capturing the images

    # for i in range(4):
    #     get_image(urls[i],image_names[i])

    get_image(urls[0],image_names[0])
    get_image(urls[1],image_names[1])


    # Iterate over the dictionary and updating the number of people on counters

    # c = 0
    # for key, value in counter_dict.items():
    #     image_path = image_name[c]
    #     value[1] =  count_people(image_path)
    #     c+=1
    

    counter_dict["hotspot_counter"][1] =  count_people(image_name[0])
    counter_dict["hostel_counter"][1] =  count_people(image_name[1])

    # Finding the minimum density counter and storing it's key 
    min_key = min(counter_dict, key=lambda k: counter_dict[k][1])



    return min_key
