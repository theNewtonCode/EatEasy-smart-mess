from PIL import Image
import os
from testpy import object_detection_with_bounding_boxes as count_people
# Define a function that counts  the number of people in an image

img_name_nickname_preference = {"hots_1":["Hotspot Entry Side", "Hotspot"], "hots_2":["Hotspot Middle Side", "Hotspot"], "hots_3":["Hotspot Counter Side", "Hotspot"], "host_1":["Hostel Entry Side", "Hostel"], "host_2":["Hostel Middle Side", "Hostel"], "host_3":["Hostel Counter Side", "Hostel"], "foot_1":["Football Entry Side", "Football"], "foot_2":["Football Middle Side", "Football"], "foot_3":["Football Counter Side", "Football"], "newmessup_1":["InsideStairs Counter Side", "InsideStairs"], "newmessup_2":["InsideStairs Middle Side", "InsideStairs"], "newmessup_3":["InsideStairs TV Side", "InsideStairs"]}
img_name_count = {"hots_1":[60, 0], "hots_2":[100, 0], "hots_3":[100, 0], "host_1":[50, 0], "host_2":[50, 0], "host_3":[50, 0], "foot_1":[50, 0], "foot_2":[50, 0], "foot_3":[50, 0], "newmessup_1":[30, 0], "newmessup_2":[30, 0], "newmessup_3":[30, 0]}
# counter_name_count = {}

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
        crop_width, crop_height = image.size[0] // 3, image.size[1]

        # Loop through and crop the image into three equal sections
        for i in range(3):
            # Define the left, upper, right, and lower coordinates for the crop
            left = i * crop_width
            upper = 0
            right = (i + 1) * crop_width
            lower = crop_height
            
            # Crop the image using Pillow
            crop = image.crop((left, upper, right, lower))
            
            # Create a new filename for the cropped image
            name = f"{f.split('.')[0]}_{i+1}"
            filename = f"{name}.jpg"
            
            # Define the path to the directory where the cropped images will be saved
            save_directory = "broken_images"
            
            # Save the cropped image to the specified directory
            crop.save(os.path.join(save_directory, filename))
            
            # Count the number of people in the cropped image
            crop_path = os.path.join(save_directory, filename)
            num_people = count_people(crop_path)
            img_name_count.get(name)[1] = num_people
            # Print the number of people in the cropped image
            # print(f"{filename} has {num_people} people.")
    print(img_name_count)

take_nd_crop(image_names, img_name_count)
# Determine which cropped image has the fewest people
# counts = []
# for i in range(1, 4):
#     filename = f"crop_{i}.jpg"
#     crop_path = os.path.join("broken_images", filename)
#     num_people = count_people(crop_path)
#     counts.append(num_people)
    
# min_count_index = counts.index(min(counts)) + 1
# min_count_filename = f"crop_{min_count_index}.jpg"

# print(f"The image with the fewest people is {min_count_filename}.")
