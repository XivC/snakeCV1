
import numpy as np
import cv2
import cognitive_face as CF




class player():
  nickname = ''
  ingame = False
  score = 0
  def __init__(self,nick):
    nickname = nick






database = open('players.txt','r')
players_base = []

for line in database.readlines():
  arg1 = line.split()[0]
  arg2 = line.split()[1]
  players_base.append((arg1,arg2))

print(players_base)




#KEY = '4aafb44ca79a4eac8b423f9bd6d018f4'  
#CF.Key.set(KEY)

#BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  
#CF.BaseUrl.set(BASE_URL)








#faces = CF.face.detect(img_url)
#print(faces)

class human:
    a = 1






cap1 = cv2.VideoCapture(0)#"http://192.168.5.58:4747/mjpegfeed?1280x720")

while cap.isOpened == False:
    cap = cv2.VideoCapture("http://192.168.5.58:4747/mjpegfeed?1280x720")
    print('')
while(True):


    
    a,frame = cap.read()
    #cv2.imshow('frame',frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceCascade = cv2.CascadeClassifier('C:\\Users\\Xiv\\AppData\\Local\\Programs\\Python\\Python37\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    faces = faceCascade.detectMultiScale(
        gray,     
 
        minNeighbors=5,     
        minSize=(10, 10)
    )
    
    if len(faces) > 0:
      cv2.imwrite
    for (x,y,w,h) in faces:
        idd +=1
        #cv2.putText(frame, str(idd), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA) 
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]  
    window_name = 'test'
   # cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
    #cv2.moveWindow(window_name, screen.x - 1, screen.y - 1)
    #cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN,
      #                    cv2.WINDOW_FULLSCREEN)
    cv2.imshow(window_name, frame)
    #cv2.imshow('video',frame)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
#http://0.0.0.0:4747/mjpegfeed?640x480 


'''
import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('C:\\Users\\Xiv\\AppData\\Local\\Programs\\Python\\Python37\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
'''
