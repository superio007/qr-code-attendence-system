import cv2
from datetime import datetime
import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",database="student_data",passwd="123456")


cap =cv2.VideoCapture(0)
# initialize the cv2 QRCode detector
detector = cv2.QRCodeDetector()

while True:
    ret, img = cap.read()

# detect and decode
     
    data, bbox, _ = detector.detectAndDecode(img)
   # check if there is a QRCode in the image
    Student_Id=[]
    Student_Name=[]
    Deparment=[]
    Div=[]
    if data:
        a=data
        Student_Id=str(data[2:7])
        Student_Name=str(data[11:24])
        Deparment=str(data[28:32])
        Div=str(data[36:37])
        time_now = datetime.now()
        dStr = time_now.strftime("%y-%m-%d")
        tStr = time_now.strftime("%H:%M:%S")
        break
    cv2.imshow("QRCODEscanner", img)   
    if cv2.waitKey(1) == ord("q"):
        break

mycursor= mydb.cursor()
s="INSERT INTO data (DATE,Student_ID,Student_Name,Department,Std,TIME) VALUES(%s,%s,%s,%s,%s,%s)" 
b1=(dStr,Student_Id,Student_Name,Deparment,Div,tStr)
mycursor.execute(s,b1)
mydb.commit()

    
print(dStr)
print(data)
print(Student_Id)
print(Student_Name)
print(Deparment)
print(Div)
print(tStr)
 


cap.release()
cv2.destroyAllWindows()
