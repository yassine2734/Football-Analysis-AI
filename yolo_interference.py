from ultralytics import YOLO
model = YOLO('yolov8x')  # load a pretrained YOLOv8x model

results = model.predict('input_videos/input_video_1.mp4',save = True)
print(results[0])
print('=======================================================')
for box in results[0].boxes:
    print(box)
