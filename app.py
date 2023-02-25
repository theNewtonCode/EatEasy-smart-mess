from PIL import Image
import os
from testpy import object_detection_with_bounding_boxes as count_people
# Define a function that counts the number of people in an image


# Define the path to the original image file
original_image_path = "pp8.jpeg"

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
    filename = f"crop_{i+1}.jpg"
    
    # Define the path to the directory where the cropped images will be saved
    save_directory = "broken_images"
    
    # Save the cropped image to the specified directory
    crop.save(os.path.join(save_directory, filename))
    
    # Count the number of people in the cropped image
    crop_path = os.path.join(save_directory, filename)
    num_people = count_people(crop_path)
    
    # Print the number of people in the cropped image
    print(f"{filename} has {num_people} people.")

# Determine which cropped image has the fewest people
counts = []
for i in range(1, 4):
    filename = f"crop_{i}.jpg"
    crop_path = os.path.join("broken_images", filename)
    num_people = count_people(crop_path)
    counts.append(num_people)
    
min_count_index = counts.index(min(counts)) + 1
min_count_filename = f"crop_{min_count_index}.jpg"

print(f"The image with the fewest people is {min_count_filename}.")
