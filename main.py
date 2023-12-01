from ultralytics import YOLO
from PIL import Image
import cv2 as cv

# # Create a new YOLO model from scratch
# model = YOLO('yolov8n.yaml')

# # Load a pretrained YOLO model (recommended for training)
# model = YOLO('yolov8n.pt')

# # Train the model using the 'coco128.yaml' dataset for 3 epochs
# results = model.train(data='coco128.yaml', epochs=3)

# # Evaluate the model's performance on the validation set
# results = model.val()

# # Perform object detection on an image using the model
# results = model('https://ultralytics.com/images/bus.jpg')

# # Export the model to ONNX format
# success = model.export(format='onnx')

#load model
model = YOLO("face-detection-yolov8/best.pt")
# load video
img_path = 'images.jpg'
results = model(img_path)
boxes = results[0].boxes
img = cv.imread(img_path)

faces = 0

for box in boxes:
    top_left_x = int(box.xyxy.tolist()[0][0])
    top_left_y = int(box.xyxy.tolist()[0][1])
    bottom_right_x = int(box.xyxy.tolist()[0][2])
    bottom_right_y = int(box.xyxy.tolist()[0][3])

    cv.rectangle(img,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(50,200,129),2)

    faces += 1

print(f'there are {faces} faces')
cv.imwrite("test.jpg",img)