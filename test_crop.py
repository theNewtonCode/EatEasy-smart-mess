import os
import cv2
import numpy as np

def crop_trapezium(image_path, trapezium_coords, output_dir):
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
    return result
    # filename = os.path.splitext(os.path.basename(image_path))[0] + '_crop.jpg'
    # output_path = os.path.join(output_dir, filename)

    # # Save the cropped image to the specified output file
    # cv2.imwrite(output_path, result)
# from PIL import Image

# # Load the image
# img = Image.open("hots.jpeg")

# # Get the size of the image
# width, height = img.size

# # Define the four corners of the image
# p = (0, 0)
# q = (width, 0)
# r = (0, height)
# s = (width, height)

# # Define the points on the sides pq and rs
# a = (int((1.4*width)/3), 0)
# b = (int((1.6*width)/3), 0)
# c = (int((1*width)/3), height)
# d = (int((2*width)/3), height)

# part1 = [p, a, c, r]
# part2 = [a, b, d, c]
# part3 = [b, q, s, d]
# # print(part1)
# crop_trapezium("pp8.jpeg", part1, "part1.jpg")
# crop_trapezium("pp8.jpeg", part2, "part2.jpg")
# crop_trapezium("pp8.jpeg", part3, "part3.jpg")


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
            imgs = crop_trapezium(image, coords[i])
            
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
            # Print the number of people in the cropped image
            # print(f"{filename} has {num_people} people.")
    print(img_name_count)
