import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
# from PIL import Image

 
 
def object_detection_with_bounding_boxes(filename, model="yolov4-tiny", confidence=0.2):
 
     
    # Read the image into a numpy array
    img = cv2.imread(filename)
     
    # Perform the object detection
    bbox, label, conf = cv.detect_common_objects(img, confidence=confidence, model=model)
     
    # Print current image's filename
    # print(f"========================\nImage processed: {filename}\n")
     

    count = 0
    for l, c in zip(label, conf):
        if l == "person":
            count +=1
    output_image = draw_bbox(img, bbox, label, conf)
    outimg = filename.split(".jpg")[0]
    # print(outimg)
    cv2.imwrite(f"{outimg}.jpg", output_image)
    # print(count)
    return count
    # print( count)

    # Create a new image that includes the bounding boxes
    # 
    # cv2.imshow('', output_image)
    # cv2.waitKey(0)

# object_detection_with_bounding_boxes(r"C:\Users\Lenovo\OneDrive\Desktop\EatEasyProject\broken_images\crop_2.jpg")