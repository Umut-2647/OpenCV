import cv2
import numpy as np

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\line.mp4")

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480)) ##frami tekrardan boyutlandiriyoruz
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_yellow=np.array([20,100,100],np.uint8) ##burda videonun sarı kısmını ayırıyoruz
    upper_yellow=np.array([30,255,255],np.uint8)

    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)

    edges=cv2.Canny(mask,75,250) ##mask uyguladığımız videonun kenarlarını buluyoruz

    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)  ##burda ise birleştireceğimiz çizgileri buluyoruz


    for line in lines:  ##burda for dongüsüyle koordinatlardan birleştirme yapacağız
        (x1,y1,x2,y2)=line[0]
        cv2.line(frame,(x1,y1),(x2,y2),(255,0,0),5)

    cv2.imshow("frame",frame)

    if (cv2.waitKey(20) & 0XFF==ord('q')):
        break

cap.release()
cv2.destroyAllWindows()