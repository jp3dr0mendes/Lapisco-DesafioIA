from ultralytics import YOLO
from PIL import Image
import cv2 as cv

#load model
model = YOLO("face-detection-yolov8/best.pt")
# load video
img_path = 'images.jpg'

results = model(img_path)
boxes = results[0].boxes
img = cv.imread(img_path)

position = (20,20)
font = cv.FONT_HERSHEY_COMPLEX
scale = 1
color = (255,0,0)
exp = 1

faces = 0

for box in boxes:
    top_left_x = int(box.xyxy.tolist()[0][0])
    top_left_y = int(box.xyxy.tolist()[0][1])
    bottom_right_x = int(box.xyxy.tolist()[0][2])
    bottom_right_y = int(box.xyxy.tolist()[0][3])

    # aplicando o blur na região de interesse
    region = img[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
    img_blur = cv.blur(region, (15,15))
    img[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = img_blur

    #marcando os rostos
    cv.rectangle(img,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(50,200,129),2)

    faces += 1

cv.putText(img, f"{faces} faces", position, font, scale, color, exp)
print(f'there are {faces} faces')
cv.imwrite("test.jpg",img)