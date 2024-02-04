import cv2
cams_test = 10
for i in range(0, cams_test):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    test, frame = cap.read()
    print("i : "+str(i)+" /// result: "+str(test))