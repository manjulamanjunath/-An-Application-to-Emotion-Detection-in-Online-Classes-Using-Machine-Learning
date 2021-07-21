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

from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "AC33917b16d95bf53a3227ad4f99aa4122"
auth_token = "d28f103bcdea8e00a595b47764776784"

client = Client(account_sid, auth_token)

window1 = tk.Tk()  
window1.title("Register")
window1.geometry('1280x720')
window1.configure(background ='blue')
img= PhotoImage(file="C:\\Users\\MANJULA\\Desktop\\Student_performace_analysis_complete_project\\BIT_Student_performace_analysis50%\\background.png")
label= ttk.Label(window1,image = img)
message = tk.Label(window1, text="WELCOME TO STUDENT PERFORMANCE ANALYSIS"   ,fg="black"  ,width=50  ,height=1,font=('times', 25, 'italic bold underline')) 
message.place(x=250, y=5)
def faculty():
    window1 = tk.Toplevel()  
    window1.title("Register")
    window1.geometry('1280x720')
    window1.configure(background ='blue')
    img= PhotoImage(file="C:\\Users\\MANJULA\\Desktop\\Student_performace_analysis_complete_project\\BIT_Student_performace_analysis50%\\background.png")
    label= ttk.Label(window1,image = img)
    message = tk.Label(window1, text="WELCOME TO FACULTY HOME  PAGE"   ,fg="black"  ,width=50  ,height=1,font=('times', 25, 'italic bold underline')) 
    message.place(x=250, y=5)

    def notes():

        f=open("stress.csv", 'r')
        reader1 = csv.reader(f)
        f1=open("Database_stress.txt", 'a')
        pj=0
        sd=0
        count =0
        enter =0
        text=f.readlines()
        text=str(text)       
        i=0
        matched=10
        with open('stress.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                print(line[1])
                if line[1] == "stress":
                    print("matched")
        ##            mail="anuswathiml2020@gmail.com"
                    res="Dear {}\n your were under stress in the class.\nplease find the below attachment and also attached timetable for your reference\n Thanks and Regards,\n Facultyname".format(line[0])           

                    atttachem.sendMail( ["manjula.ms888@gmail.com"],
                                        "Notes for Student Under stress",
                                        res,
                                        ["timetable.jpg","Database_stress.txt"] )
                    print("mail sent")

        ##            phone1=str(line[2])
                    client.api.account.messages.create(
                        to = "8073129216",
                        from_="+19093652750" ,  #+1 210-762-4855"
                        body="your ward is not active in the class {} ".format(line[2]) )

        ##            print("your ward is not active in the class {}".format(line[2]))

    def mail():

        USERNAME = "manjula.ms888@gmail.com"
        PASSWORD = "9591msps"
        def sendMail(to, subject, text, files=[]):
##            shutil.make_archive('attendance','zip','Attendance')
            assert type(to)==list
            assert type(files)==list

            msg = MIMEMultipart()
            msg['From'] = USERNAME
            msg['To'] = COMMASPACE.join(to)
            msg['Date'] = formatdate(localtime=True)
            msg['Subject'] = subject
            
            msg.attach( MIMEText(text) )

            for file in files:
                part = MIMEBase('application', "octet-stream")
                part.set_payload( open(file,"rb").read() )
                Encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="%s"'
                               % os.path.basename(file))
                msg.attach(part)
                server = smtplib.SMTP('smtp.gmail.com:587')
                server.ehlo_or_helo_if_needed()
                server.starttls()
                server.ehlo_or_helo_if_needed()
                server.login(USERNAME,PASSWORD)
                server.sendmail(USERNAME, to, msg.as_string())
                server.quit()

        sendMail( ["manjula.ms888@gmail.com"],
            "Section b Performace",
            "this is the body text of the email",
            ["performance.csv", "stress.csv"] )
##    

    takeImg = tk.Button(window1, text="Notes", command=notes  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
    takeImg.place(x=650, y=150)

    takeImg = tk.Button(window1, text="Mail HOD", command=mail  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
    takeImg.place(x=650, y=250)

    takeImg = tk.Button(window1, text="Back", command=window1.destroy  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
    takeImg.place(x=650, y=350)

    label.pack()
    window1.mainloop()    
def student():
    os.system("python Student.py")

takeImg = tk.Button(window1, text="Faculty", command=faculty  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=650, y=150)

takeImg = tk.Button(window1, text="Student", command=student  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=650, y=250)

takeImg = tk.Button(window1, text="Quit", command=window1.destroy  ,fg="Black"  ,bg="White"  ,width=10  ,height=2, activebackground = "green" ,font=('times', 15, ' bold '))
takeImg.place(x=650, y=350)


label.pack()
window1.mainloop()
