import cv2

cap=cv2.VideoCapture("C:\\Users\\umuty\\Desktop\\OpenCV\\test_videos\\car.mp4")

##ne yaptığımıza karar verecek bir fonksiyona ihtiyacimiz var
circles=[]
def mouse(event,x,y,flags,params):      #event mouse la yaptığımız işlemi tutacak   x ve y ise çizeceğimiz çemberin merkezleri
    if event==cv2.EVENT_LBUTTONDOWN:   #eğer sol tuşa basıldıysa
        circles.append((x,y))


cv2.namedWindow("Frame")

cv2.setMouseCallback("Frame",mouse)

while 1:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    for center in circles:    #circlesin icindeki merkezleri çekicek
        cv2.circle(frame,center,20,(255,0,0),-1)

    cv2.imshow("Frame",frame)

    key=cv2.waitKey(1)

    if key==27:
        break
    elif key==ord("h"):
        circles=[]  #başka tusa basıldığında pencereyi temizlesin

cap.release()
cv2.destroyAllWindows()