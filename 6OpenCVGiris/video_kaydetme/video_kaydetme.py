import cv2


#cap=cv2.VideoCapture(0)
cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)  #hata alındığında yazılabilir


fileName = "D:\opencv\sarky.jpeg"
codec = cv2.VideoWriter_fourcc('C', 'J', 'P', 'G')
frameRate = 30
resolution=(640,480)
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)


while True:
    ret, frame = cap.read()
    frame=cv2.flip(frame, 1)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        videoFileOutput.write(frame)
        break

videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()