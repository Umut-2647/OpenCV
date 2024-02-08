import cv2



cap=cv2.VideoCapture("video.mp4")


while True:
    ret,frame=cap.read()
    if ret==False:
        break
    cv2.imshow("Sarki",frame)
    if cv2.waitKey(30)& 0xFF==ord("s"):
        cv2.imwrite("D:\opencv\img.jpg",frame)
        break

cap.release()
cv2.destroyAllWindows()