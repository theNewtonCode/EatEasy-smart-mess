# import cv2

# # Load the HOG descriptor for pedestrian detection
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# # Load the image and resize it
# image = cv2.imread('pp4.jpeg')
# image = cv2.resize(image, (640, 480))

# # Detect people in the image
# (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4), padding=(8, 8), scale=1.05)

# # Draw rectangles around the detected people
# for (x, y, w, h) in rects:
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# # Count the number of people detected
# num_people = len(rects)

# # Display the image with the detected people and the number of people
# cv2.putText(image, "Number of people: {}".format(num_people), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()







# import cv2
# import numpy as np

# # Load YOLOv3 network
# net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')

# # Set classes that YOLOv3 can detect
# classes = ['person']

# # Load image
# img = cv2.imread('pp1.jpeg')

# # Get image dimensions
# height, width, _ = img.shape

# # Create a blob from the image
# blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), swapRB=True)

# # Set the input to the network
# net.setInput(blob)

# # Run forward pass and get output
# outs = net.forward(net.getUnconnectedOutLayersNames())

# # Initialize variables to count people
# count = 0
# indexes = []

# # Loop over all detected objects
# for out in outs:
#     for detection in out:
#         # Get class ID and confidence of detection
#         scores = detection[5:]
#         class_id = np.argmax(scores)
#         confidence = scores[class_id]
#         # print(class_id)
#         # If detection is a person and confidence is high enough, count it
#         if classes[class_id] == 'person' and confidence > 0.5:
#             count += 1
#             indexes.append(class_id)
            
# # Draw bounding boxes around detected people
# colors = np.random.uniform(0, 255, size=(len(indexes), 3))
# for i in indexes:
#     x, y, w, h = outs[i][0:4] * np.array([width, height, width, height])
#     x, y, w, h = int(x - w/2), int(y - h/2), int(w), int(h)
#     color = [int(c) for c in colors[i]]
#     cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)

# # Display image with bounding boxes and number of people counted
# cv2.putText(img, 'People Count: {}'.format(count), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
# cv2.imshow('Crowd', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()










# import cv2

# # Reading the Image
# image = cv2.imread('pp4.jpeg')

# # initialize the HOG descriptor
# hog = cv2.HOGDescriptor()
# hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# # detect humans in input image
# (humans, _) = hog.detectMultiScale(image, winStride=(10, 10),
# padding=(32, 32), scale=1.1)

# # getting no. of human detected
# print('Human Detected : ', len(humans))

# # loop over all detected humans
# for (x, y, w, h) in humans:
#    pad_w, pad_h = int(0.15 * w), int(0.01 * h)
#    cv2.rectangle(image, (x + pad_w, y + pad_h), (x + w - pad_w, y + h - pad_h), (0, 255, 0), 2)

# # display the output image
# cv2.imshow("Image", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()