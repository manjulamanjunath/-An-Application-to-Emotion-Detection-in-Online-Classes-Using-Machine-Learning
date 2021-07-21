import csv
import tkinter as tk
from tkinter import ttk
from tkinter import *
import csv
import cv2
import os
from keras.preprocessing.image import img_to_array
import imutils
from keras.models import load_model
import numpy as np
import time
import pandas as pd
import csv
import atttachem
import smtplib
##from email.MIMEMultipart import MIMEMultipart
##from email.MIMEBase import MIMEBase
##from email.MIMEText import MIMEText
##from email.Utils import COMMASPACE, formatdate
##from email import Encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import email.encoders as Encoders
import os    

window = tk.Tk()
#helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Emotion_Recogniser")


#answer = messagebox.askquestion(dialog_title, dialog_text)
 
#window.geometry('1200x800')
#window.configure(background='light cyan4')
img= PhotoImage(file="C:\\Users\\MANJULA\\Desktop\\Student_performace_analysis_complete_project\\BIT_Student_performace_analysis50%\\2.png")
label= ttk.Label(window,image = img)
message = tk.Label(window, text="STUDENT PERFORMANCE ANALYSIS"   ,fg="black"  ,width=50  ,height=1,font=('times', 25, 'italic bold underline')) 
message.place(x=250, y=5)

lbl1 = tk.Label(window, text="Username",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
lbl1.place(x=550, y=100)
txt1 = tk.Entry(window,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
txt1.place(x=800, y=100)

lbl2= tk.Label(window, text=" password",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
lbl2.place(x=550, y=150)
txt2 = tk.Entry(window,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
txt2.place(x=800, y=150)



def main():
    with open("UserDetails.csv","r") as file:
        file_reader=csv.reader(file)
        user_find(file_reader)
        file.close()
        
def user_find(file):
    global user
    user= txt1.get()
##    user = input ("enter user name")
    for row in file:
        if row[0] == user:
            print("user name found", user)
            user_found= [row[0], row[1]]
            pass_check(user_found)
            break
        else:
            print("not found")

def pass_check(user_found):
   # global user
    user =txt2.get()
##    user=input("enter password")
    if user_found[1] == user:
        print("password matched")
        successful()
    else:
        print("invalid password")
        unsuccess()


def register():
    global window1
    window1 = tk.Toplevel()  
    window1.title("Register")
    window1.geometry('1280x720')
    window1.configure(background ='blue')
    img= PhotoImage(file="C:\\Users\\MANJULA\\Desktop\\Student_performace_analysis_complete_project\\BIT_Student_performace_analysis50%\\background.png")
    label= ttk.Label(window1,image = img)


      
    lbl = tk.Label(window1, text="Username",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
    lbl.place(x=350, y=50)

    txt = tk.Entry(window1,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    txt.place(x=620, y=50)

    lbl2 = tk.Label(window1, text="  Password",width=18  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl2.place(x=350, y=100)

    txt2 = tk.Entry(window1,width=15  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt2.place(x=620, y=100)

    lbl3 = tk.Label(window1, text=" ID",width=18  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl3.place(x=350, y=150)

    txt3 = tk.Entry(window1,width=15  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt3.place(x=620, y=150)

    lbl4 = tk.Label(window1, text="  Phone",width=18  ,fg="Black"  ,bg="White"    ,height=1 ,font=('Arial', 15, ' bold ')) 
    lbl4.place(x=350, y=200)

    txt4 = tk.Entry(window1,width=15  ,bg="White"  ,fg="Black", font=('Arial', 15, ' bold ')  )
    txt4.place(x=620, y=200)


    def TakeImages():
        global ID
        global username
        username=(txt.get())
        password =(txt2.get())
        ID=(txt3.get())
        phone=(txt4.get())
##        location=(txt5.get())
##        print()
        row = [username, password, ID, phone ]
        with open('UserDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            
        csvFile.close()
        print("file Updated successfully")
        reg()
    
    takeImg = tk.Button(window1, text ="Submit",  
    command = TakeImages, fg ="white", bg ="blue",  
    width = 10, height = 1, activebackground = "Red",  
    font =('times', 10, ' bold ')) 
    takeImg.place(x = 550, y = 400)
    label.pack()
    window1.mainloop()
 
def em_success():
        root=Tk()
        root.geometry('250x150')
        root.title("Success")
        #cv2.destroy()
        
        lbl=Label(root, text="File updated Successfully")
        print("file updated Successful")   
        lbl.pack()
        def bb():
            camera.release()
            cv2.destroyAllWindows()
##            time.sleep(3)
            root.destroy()
           
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)

        root.mainloop()

def unsuccess():
        root=Tk()
        root.geometry('250x150')
        root.title("Success")
        #cv2.destroy()
        
        lbl=Label(root, text="Login Unsuccessful")
        print("Login Unsuccessful")   
        lbl.pack()
        def bb(): 
            cv2.destroyAllWindows()
            root.destroy()
           
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)

        root.mainloop()



def reg():
        root=Tk()
        root.geometry('250x150')
        root.title("Success")
        #cv2.destroy()
        
        lbl=Label(root, text="Registration Success")
        print("Registration Successful")   
        lbl.pack()
        def bb():
            window1.destroy()
            cv2.destroyAllWindows()
            root.destroy()
           
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)
        root.mainloop()
        
def emotion():

    # parameters for loading data and images
    detection_model_path = 'haarcascade_files/haarcascade_frontalface_default.xml'
    emotion_model_path = 'models/_mini_XCEPTION.102-0.66.hdf5'

    # hyper-parameters for bounding boxes shape
    # loading models
    face_detection = cv2.CascadeClassifier(detection_model_path)
    emotion_classifier = load_model(emotion_model_path, compile=False)
    EMOTIONS = ["angry" ,"disgust","scared", "happy", "sad", "surprised",
     "neutral"]


    #feelings_faces = []
    #for index, emotion in enumerate(EMOTIONS):
       # feelings_faces.append(cv2.imread('emojis/' + emotion + '.png', -1))

    # starting video streaming
    cv2.namedWindow('your_face')
    global camera
    camera = cv2.VideoCapture(0)
    while True:
        frame = camera.read()[1]
        #reading the frame
        frame = imutils.resize(frame,width=300)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detection.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30),flags=cv2.CASCADE_SCALE_IMAGE)
        
        canvas = np.zeros((250, 300, 3), dtype="uint8")
        frameClone = frame.copy()
        if len(faces) > 0:
            faces = sorted(faces, reverse=True,
            key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
            (fX, fY, fW, fH) = faces
                        # Extract the ROI of the face from the grayscale image, resize it to a fixed 28x28 pixels, and then prepare
                # the ROI for classification via the CNN
            roi = gray[fY:fY + fH, fX:fX + fW]
            roi = cv2.resize(roi, (64, 64))
            roi = roi.astype("float") / 255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi, axis=0)
            
            
            preds = emotion_classifier.predict(roi)[0]
            print("preds ",preds)
            emotion_probability = np.max(preds)
            print("emotion_probability",emotion_probability)
            label = EMOTIONS[preds.argmax()]
            print("label",label)
        else: continue

     
        for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
                    # construct the label text
                    text = "{}: {:.2f}%".format(emotion, prob * 100)
                    if emotion == "happy":
                        print("No stress")
                        emotion1="No stress"
##                        time.sleep(3)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            row = [user,emotion1]
                            with open('performance.csv','a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                csvFile.close()
                                print("performance file updated successfully")
                                em_success()
                           
                            
                        
                    if emotion == "angry":
                        print("stress")
##                        time.sleep(3)
                        emotion1="stress"
##                        time.sleep(3)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            row = [user, emotion1]
                            with open('stress.csv','a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                csvFile.close()
                                print("Stress file updated successfully")
                                em_success()
                            

                    if emotion == "sad":
                        print("stress")
                        time.sleep(3)
                        emotion1="stress"
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            row = [user, emotion1]
                            with open('stress.csv','a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                csvFile.close()
                                print("Stress file updated successfully")
                                em_success()
                                                        
##                            print("play another sound")
##                            break

                    if emotion == "neutral":
                        print("No stress")
                        time.sleep(3)
                        emotion1="No stress"
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            row = [user, emotion1]
                            with open('performance.csv','a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                csvFile.close()
                                print("performance file updated successfully")                                                      
                                em_success()                            
##                            print("play another sound")
##                            break

                    if emotion == "scared":
                        print("stress")
                        time.sleep(3)
                        emotion1="stress"
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            row = [user, emotion1]
                            with open('stress.csv','a+') as csvFile:
                                writer = csv.writer(csvFile)
                                writer.writerow(row)
                                csvFile.close()
                                print("Stress file updated successfully")                                                      
                                em_success()                            
##                            print("play another sound")
##                            break
                    # draw the label + probability bar on the canvas
                   # emoji_face = feelings_faces[np.argmax(preds)]

                    
                    w = int(prob * 300)
                    cv2.rectangle(canvas, (7, (i * 35) + 5),
                    (w, (i * 35) + 35), (0, 0, 255), -1)
                    cv2.putText(canvas, text, (10, (i * 35) + 23),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                    (255, 255, 255), 2)
                    cv2.putText(frameClone, label, (fX, fY - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                  (0, 0, 255), 2)
    #    for c in range(0, 3):
    #        frame[200:320, 10:130, c] = emoji_face[:, :, c] * \
    #        (emoji_face[:, :, 3] / 255.0) + frame[200:320,
    #        10:130, c] * (1.0 - emoji_face[:, :, 3] / 255.0)


        cv2.imshow('your_face', frameClone)
        cv2.imshow("Probabilities", canvas)
    ##    if cv2.waitKey(1) & 0xFF == ord('q'):
    ##        break

    camera.release()
    cv2.destroyAllWindows()



def successful():
##        global cam
        root=Tk()
        root.geometry('250x150')
        root.title("Success")
        #cv2.destroy()
        
        lbl=Label(root, text="Logged In Successfully")
        print("Login Successful")   
        lbl.pack()
        def bb():
            root.destroy()

##            cv2.destroyAllWindows()
##            time.sleep(3)
            emotion()
            
        quitWindow = tk.Button(root, text ="OK",  
        command = bb, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)
        time.sleep(1)

        root.mainloop()



    
def feedback_mail():
    global window3
    window3 = tk.Tk()
    #helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
    window3.title("feedback")


    #answer = messagebox.askquestion(dialog_title, dialog_text)
     
    window3.geometry('1200x800')
    window3.configure(background='light cyan4')
    ##img= PhotoImage(file="C:\\Users\\HP\\Desktop\\Student_performace_analysis\\2.png")
    ##label= ttk.Label(window,image = img)
    message = tk.Label(window3, text="Faculty Feedback"   ,fg="black"  ,width=50  ,height=1,font=('times', 25, 'italic bold underline')) 
    message.place(x=250, y=5)

    lbl1 = tk.Label(window3, text=" Enter your USN",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
    lbl1.place(x=450, y=100)
    txt1 = tk.Entry(window3,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    txt1.place(x=700, y=100)

    lbl2 = tk.Label(window3, text=" Enter your name",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
    lbl2.place(x=450, y=150)
    txt2 = tk.Entry(window3,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    txt2.place(x=700, y=150)

    lbl3= tk.Label(window3, text=" Enter Subject",width=18  ,height=1  ,fg="Black"  ,bg="White" ,font=('Arial', 15, ' bold ') ) 
    lbl3.place(x=450, y=200)
    txt3 = tk.Entry(window3,width=15  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    txt3.place(x=700, y=200)


    lbl4= tk.Label(window3, text=" Feedback ",width=10 ,height=2  ,fg="Black"  ,bg="light cyan4" ,font=('Arial', 15, ' bold ') ) 
    lbl4.place(x=550, y=250)
    txt4 = tk.Entry(window3,width=25  ,bg="White" ,fg="Black",font=('Arial', 15, ' bold '))
    txt4.place(x=700, y=250)
    var=0
    if var==1:
        print("Entering feedback")
        updated()
        var=0
        
        
    def updated():
        window=tk.Tk()
        window.title("feedback")
        window.geometry("250x150")
        lbl4= tk.Label(window, text=" Thanks for Your Feedback ")#width=20 ,height=2  ,fg="Black"  ,bg="light cyan4" ,font=('Arial', 15, ' bold ') )
        lbl4.pack()
        #lbl4.place(x=0, y=50)
        def ok():
            window3.destroy()
            window.destroy()
        quitWindow = tk.Button(window, text ="OK",  
        command = ok, fg ="white", bg ="blue",  
        width = 5, height = 1, activebackground = "Red",  
        font =('times', 15, ' bold ')) 
        quitWindow.place(x = 85, y = 50)            
        window.mainloop()

        
    def submit():
        #name
        usn=txt1.get()
        name=txt2.get()
        sub=txt3.get()
        feed=txt4.get()
        
        row=[usn, name, sub, feed]
        with open("feedback.csv", "a+") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
            print("successfully updated")
            updated()
            
    lbl4= tk.Button(window3, text=" Submit ",command= submit, width=10 ,height=2  ,fg="Black"  ,bg="light cyan4" ,font=('Arial', 15, ' bold ') ) 
    lbl4.place(x=450, y=350)
         
    lbl4= tk.Button(window3, text=" Quit ",command= window3.destroy, width=10 ,height=2  ,fg="Black"  ,bg="light cyan4" ,font=('Arial', 15, ' bold ') ) 
    lbl4.place(x=650, y=350)    
        
    window3.mainloop()



takeImg = tk.Button(window, text="Login", command=main  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=400, y=450)

takeImg = tk.Button(window, text="Register", command=register  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=600, y=450)

takeImg = tk.Button(window, text="FeedBack", command=feedback_mail  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=800, y=450)

takeImg = tk.Button(window, text="Quit", command=window.destroy  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=1000, y=450)

label.pack()
window.mainloop()


