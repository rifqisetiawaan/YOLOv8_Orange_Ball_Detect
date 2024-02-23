from roboflow import Roboflow
rf = Roboflow(api_key="mivzZ8eMkZ7M6Chri5SN")
project = rf.workspace("krsbipolmanws").project("bola-krsbi")
dataset = project.version(2).download("yolov8")
