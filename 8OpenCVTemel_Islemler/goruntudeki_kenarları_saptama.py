import cv2

#cv2.Canny(input,minThreshold,maxThreshold)

cap=cv2.VideoCapture(0)

while True:
     ret,frame=cap.read()
     frame=cv2.flip(frame,1)

     if ret==False: ##video bittiginde duracak
         break

     edges=cv2.Canny(frame,100,200)  ##videodaki kenarları bulmak icin kullanacağımız fonksiyon
     cv2.imshow("Frame",frame)
     cv2.imshow("Edges",edges)

     if cv2.waitKey(1)& 0xFF==ord("q"):
         break


cap.release()
cv2.destroyAllWindows()