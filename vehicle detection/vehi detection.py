import cv2
import imutils
imgfile="cars.xml"
load=cv2.CascadeClassifier(imgfile)
cam=cv2.VideoCapture(0)

while True:
    _,frame=cam.read()
    resize=imutils.resize(frame,width=1000)
    grayscale=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    coord=load.detectMultiScale(frame,1.1,5)
    for (x,y,w,h) in coord:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
    cv2.imshow("Frame",frame)
    b = str(len(coord))
    a = int(b)
    n = a
    print("North: %d " % (n))
    if n >= 8:
        print("North More Traffic, Please on the RED Signal")
    else:
        print("no traffic")
    key=cv2.waitKey(1)
    if key==27:
        break
frame.release()
cv2.destroyAllWindows()

