from PIL import Image
import os
from testpy import object_detection_with_bounding_boxes as count_people
# Define a function that counts  the number of people in an image

import os
import cv2
import numpy as np

def crop_trapezium(image_path, trapezium_coords):
    # Load the image
    img = cv2.imread(image_path)

    # Define the trapezium coordinates in clockwise order
    pts = np.array(trapezium_coords, np.int32)

    # Create a mask with the same shape as the image
    mask = np.zeros(img.shape[:2], np.uint8)

    # Fill the trapezium with white color
    cv2.fillPoly(mask, [pts], (255, 255, 255))

    # Apply the mask to the image to get the cropped image
    result = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    result = Image.fromarray(result)

    # Return the cropped image as a PIL image
    return result
    # return result

img_name_nickname_preference = {"hots_1":["Hotspot Entry Side", "Hotspot"], "hots_2":["Hotspot Middle Side", "Hotspot"], "hots_3":["Hotspot Counter Side", "Hotspot"], "host_1":["Hostel Entry Side", "Hostel"], "host_2":["Hostel Middle Side", "Hostel"], "host_3":["Hostel Counter Side", "Hostel"], "foot_1":["Football Entry Side", "Football"], "foot_2":["Football Middle Side", "Football"], "foot_3":["Football Counter Side", "Football"], "newmessup_1":["InsideStairs Counter Side", "InsideStairs"], "newmessup_2":["InsideStairs Middle Side", "InsideStairs"], "newmessup_3":["InsideStairs TV Side", "InsideStairs"]}
img_name_count = {"hots_1":[60, 0], "hots_2":[100, 0], "hots_3":[100, 0], "host_1":[50, 0], "host_2":[50, 0], "host_3":[50, 0], "foot_1":[50, 0], "foot_2":[50, 0], "foot_3":[50, 0], "newmessup_1":[30, 0], "newmessup_2":[30, 0], "newmessup_3":[30, 0]}
# counter_name_count = {}
rows = ['Hotspot Entry Side', 'Hotspot Middle Side', 'Hotspot Counter Side', 'Hostel Entry Side', 'Hostel Middle Side', 'Hostel Counter Side', 'Football Entry Side', 'Football Middle Side', 'Football Counter Side', 'InsideStairs Counter Side', 'InsideStairs Middle Side', 'InsideStairs TV Side']
image_names = ["hots.jpeg", "host.jpeg", "foot.jpeg", "newmessup.jpeg"]

# img_name_count.["host_1"] = 
# print(img_name_count.get("host_1")[1])


# img_name_count = {"hots_1":[60, 0], "hots_2":[100, 0], "hots_3":[100, 0], "host_1":[50, 0], "host_2":[50, 0], "host_3":[50, 0], "foot_1":[50, 0], "foot_2":[50, 0], "foot_3":[50, 0], "newmessup_1":[30, 0], "newmessup_2":[30, 0], "newmessup_3":[30, 0]}

# Define the path to the original image file
def take_nd_crop(listfimgs, img_name_count):
    for f in listfimgs:
        original_image_path = f
        # Open the image using Pillow
        image = Image.open(original_image_path)
        # Define the dimensions of the cropped images
        width, height = image.size

        p = (0, 0)
        q = (width, 0)
        r = (0, height)
        s = (width, height)

        # Define the points on the sides pq and rs
        a = (int((1.4*width)/3), 0)
        b = (int((1.6*width)/3), 0)
        c = (int((1*width)/3), height)
        d = (int((2*width)/3), height)


        part1 = [p, a, c, r]
        part2 = [a, b, d, c]
        part3 = [b, q, s, d]
        coords = [part1, part2, part3]
        # Loop through and crop the image into three equal sections
        for i in range(3):
            imgs = crop_trapezium(f, coords[i])
            
            # Create a new filename for the cropped image
            name = f"{f.split('.')[0]}_{i+1}"
            filename = f"{name}.jpg"
            
            # Define the path to the directory where the cropped images will be saved
            save_directory = "broken_images"
            
            # Save the cropped image to the specified directory
            imgs.save(os.path.join(save_directory, filename))
            
            # Count the number of people in the cropped image
            crop_path = os.path.join(save_directory, filename)
            num_people = count_people(crop_path)
            img_name_count.get(name)[1] = num_people

    # print(img_name_count)
    return img_name_count

take_nd_crop(image_names, img_name_count)

def find_max(d1, d2, nickname, value):
    # Create a list of tuples that contains the actual name, max value, and live value
    name_values = [(v[0], v[1][0], v[1][1]) for v in d1.items() if v[0] in d2 and d2[v[0]][1] == nickname]
    name_vals = [(v[0], v[1][0], v[1][1]) for v in d1.items()]
    # Sort the list in descending order of max value
    name_values.sort(key=lambda x: x[1], reverse=True)
    
    # Find the first name that satisfies the condition
    for name, max_val, live_val in name_values:
        if max_val - live_val >= value:
            return "Yes you can sit here", d2[name][0]
    
    # If no name satisfies the condition, find the first name with max value and live value greater than live_val
    for name, max_val, live_val in name_vals:
        if max_val - live_val >= value:
            return "Your Preferred area is full", d2[name][0]
    
    # If no name satisfies any condition, return None
    return None, None

def get_ratio_list(dict1):
    ratio_list = []
    for key, value in dict1.items():
        ratio = (value[0] - value[1]) / value[0] * 100
        ratio_list.append(ratio)
    return ratio_list

# print(find_max(img_name_count, img_name_nickname_preference, "Football", 6))
