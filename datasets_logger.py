from roboflow import Roboflow
rf = Roboflow(api_key="mivzZ8eMkZ7M6Chri5SN")
project = rf.workspace("krsbipolmanws").project("bola-krsbi")
version = project.version(3)
dataset = version.download("yolov8")
