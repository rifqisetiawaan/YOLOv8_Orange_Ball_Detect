from ultralytics import YOLO
 
# Load the model.
model = YOLO('yolov8n.pt')
 
# Training.
results = model.train(
   data='data.yaml',
   imgsz=1280,
   epochs=10,
   batch=5,
   name='yolov8n_se'
)