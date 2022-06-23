import cv2
from tkinter import *
########################################
#              버튼 클릭시              #
#              카메라 열림              #
########################################

def VideoOpen():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        exit()

    while True :
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('camera',frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


root = Tk()
root.title("안전점검 얼굴 인식 프로그램")

btn1 = Button(root, padx = 10, pady = 10, text = "카메라 켜기", command=VideoOpen)
btn1.pack()
root.mainloop()

