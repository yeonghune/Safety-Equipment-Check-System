import tkinter.messagebox as msgbox
from tkinter import *
import os
import cv2
from matplotlib.pyplot import text
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
#얼굴 검출과 웹캠 여는 함수
def faceDection():
  cnt = 0
  # For webcam input:
  cap = cv2.VideoCapture(0)
  with mp_face_detection.FaceDetection(
      model_selection=0, min_detection_confidence=0.7) as face_detection:
    while cap.isOpened():
      
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      image2 = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = face_detection.process(image)

      # Draw the face detection annotations on the image.
      image.flags.writeable = True
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
      if results.detections:
        for detection in results.detections:
          mp_drawing.draw_detection(image, detection)
          if cnt % 50 == 0:
            cv2.imwrite('Face\{0}\{1}.jpg'.format(entry1.get(),cnt),image2)
      # Flip the image horizontally for a selfie-view display.
      cv2.imshow('face extraction for image training', cv2.flip(image, 1))
      if cv2.waitKey(5) & 0xFF == 113:
        break
      cnt += 1
  cap.release()
  cv2.destroyAllWindows()
  root.destroy()

#추출 사진 저장 경로 설정(사번입력)
def createDirectory():
      os.mkdir('Face\{0}'.format(entry1.get()))
      faceDection()
      return None

root = Tk()
root.title("안전점검 얼굴 인식 프로그램")
root.geometry("400x300")

label1 = Label(root, text="사번을 입력하세요")
label1.pack()

entry1 = Entry(root, width = 20)
entry1.pack()

btn1 = Button(root, padx = 10, pady = 10, text = "얼굴 등록", command=createDirectory)
btn1.pack()
root.mainloop()

