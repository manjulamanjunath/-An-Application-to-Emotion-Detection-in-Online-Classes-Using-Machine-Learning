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

USERNAME = "manjulaam14@gmail.com"
PASSWORD = "9591msps*"

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

            atttachem.sendMail( ["manjulaam14@gmail.com"],
                                "Notes for Student Under stress",
                                res,
                                ["timetable.jpg","Database_stress.txt"] )
            print("mail sent")

##            phone1=str(line[2])
##        client.api.account.messages.create(
##                to = phone1,
##                from_="+12057829308" ,  #+1 210-762-4855"
##                body="your ward is not active in the class {} ".format(line[1]) )

##            print("your ward is not active in the class {}".format(line[2]))
