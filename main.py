from ultralytics import YOLO
from PIL import Image
import cv2 as cv

#load model
model = YOLO("face-detection-yolov8/best.pt")

# load video
img_path = input('Digite o caminho para o vídeo: ')
img_path = img_path.split('"')
img_path = img_path[1]
video_name = img_path.split('.')
video_name = video_name[0]+'-edited'+'.'+video_name[1]
codec = cv.VideoWriter_fourcc(*'mp4v')

cap = cv.VideoCapture(img_path)
ret, frame = cap.read()
cv.resize(frame,(480,640))

altura, largura, _ = frame.shape
video_out = cv.VideoWriter(video_name, codec, 30, (largura, altura))

if not cap.isOpened():
    print('Erro ao abrir o vídeo')
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        #verificando a leitura do frame
        break

    results = model(frame)
    boxes = results[0].boxes
    # img = cv.imread(frame)

    position = (50,50)
    font = cv.FONT_HERSHEY_COMPLEX
    scale = 3
    color = (255,0,0)
    exp = 2

    faces = 0

    for box in boxes:
        top_left_x = int(box.xyxy.tolist()[0][0])
        top_left_y = int(box.xyxy.tolist()[0][1])
        bottom_right_x = int(box.xyxy.tolist()[0][2])
        bottom_right_y = int(box.xyxy.tolist()[0][3])

        # aplicando o blur na região de interesse
        region = frame[top_left_y:bottom_right_y, top_left_x:bottom_right_x]
        img_blur = cv.blur(region, (50,50))
        frame[top_left_y:bottom_right_y, top_left_x:bottom_right_x] = img_blur

        #marcando os rostos
        cv.rectangle(frame,(top_left_x,top_left_y),(bottom_right_x,bottom_right_y),(50,200,129),2)

        faces += 1

    cv.putText(frame, f"{faces} faces", position, font, scale, color, exp)
    print(f'there are {faces} faces')
    # cv.imwrite("test.jpg",frame)
    video_out.write(frame)

video_out.release()

print(f'video criado com sucesso no caminho {video_name}')