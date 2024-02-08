import cv2

#WEBCAM
#cap=cv2.VideoCapture(0)
#cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)  #hata alındığında yazılabilir


#VİDEO DOSYASİ
cap=cv2.VideoCapture("sarki.mp4")



while True:
    ret,frame=cap.read()
    #frame=cv2.flip(frame,1)   ###webcam için geçerli
    cv2.imshow("Bergen",frame)
    if cv2.waitKey(10) & 0xFF==ord("q"):  #q harfine basarsak videoyu kapatır
        break

cap.release()
cv2.destroyAllWindows()







