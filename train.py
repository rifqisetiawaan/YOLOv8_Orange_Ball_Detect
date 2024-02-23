from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')

# Training.
results = model.train(
   data='/home/krsbi/YOLOv8_Orange_Ball_Detect2/bola-krsbi-2/data.yaml', 
   imgsz=640,
   epochs=100,
   batch=8,
   name='yolov8n_se'
)