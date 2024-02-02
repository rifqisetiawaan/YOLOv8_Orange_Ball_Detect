from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='dataset_bola-1\data.yaml', 
   imgsz=640,
   epochs=10,
   batch=5,
   name='yolov8n_se'
)