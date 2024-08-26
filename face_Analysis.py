import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename #displays a file dialog for multiple file selections
from tkinter import messagebox as ms
import cv2 #By using it, one can process images and videos to identify objects, faces
import sqlite3
import os #a module that include many functions to interact with the file system
import numpy as np
import time
import emotion_1_updated as validate
#import video_capture as value
#import lecture_details as detail_data
#import video_second as video1

#import lecture_video  as video

global fn
fn = ""
global msg
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.state("zoomed")
root.title("FACE RECOGNITION SYSTEM")

# 430
#######lbl = tk.Label(root, text="Diabetic Retinopathy Detection System", font=('times', 35,' bold '), height=1, width=30,bg="seashell2",fg="indian red")
########lbl.place(x=350, y=5)
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('2.jpg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

#background_image = ImageTk.PhotoImage(image2)

#background_label = tk.Label(root, image=background_image)

#background_label.image = background_image

#background_label.place(x=0, y=0)

img=ImageTk.PhotoImage(Image.open("2.jpg"))

#img2=ImageTk.PhotoImage(Image.open("3.jpg"))

#img3=ImageTk.PhotoImage(Image.open("img4.jpg"))

logo_label=tk.Label()
logo_label.place(x=0,y=0)
 
x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()
# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="FACE RECOGNITION SYSTEM", font=("Georgia", 25, 'bold'),
                    background="#113F67", fg="white", width=70, height=2)
label_l1.place(x=0, y=0)

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)

def update_label(str_T):
    #clear_img()
    result_label = tk.Label(root, text=str_T, width=50, font=("bold", 25), bg='bisque2', fg='black')
    result_label.place(x=200, y=100)
    
#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def evaluation():
        # from subprocess import call
        # call(['python','detection_emotion_practice.py'])
        validate.upload()
  

          

def prediction_emotion():
    #clear_img()
    #update_label("Model Training Start...............")

    start = time.time()

    result = validate.files_count()
    #validate.files_count()
    end = time.time()
    #print("---" + result)
    ET = "Execution Time: {0:.4} seconds \n".format(end - start)

    msg = "Model Training Completed.." + '\n' + str(result) + '\n'+ ET

    update_label(msg)
    
   
    #mail(result)
    
# def mail(result):
#     import smtplib
#     from email.message import EmailMessage
#     import imghdr
    
#     Sender_Email = "ruchita.sct1@gmail.com"
#     Reciever_Email = "ruchita.sctcod@gmail.com"
    
#     Password ='7719849698'
#     newMessage = EmailMessage()    #creating an object of EmailMessage class
#     newMessage['Subject'] = "Sentiment Analysis" #Defining email subject
#     newMessage['From'] = Sender_Email  #Defining sender email
#     newMessage['To'] = Reciever_Email  #Defining reciever email  
#     newMessage.set_content(str(result)) #Defining email body
#     with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
#         smtp.login(Sender_Email, Password)              
#         smtp.send_message(newMessage)
#################################################################################################################
def window():
    root.destroy()



button3 = tk.Button(root, text="FIND EVALUATION",command=evaluation,width=18, height=1,font=('Georgia', 20, ' bold '), bg="#226597", fg="#F3F9FB")
button3.place(x=200, y=300)

# button4 = tk.Button(root, text="Prediction",command=prediction_emotion, width=12, height=1, bg="#34495E", fg="white",font=('times', 15, ' bold '))
# button4.place(x=20, y=240)

exit = tk.Button(root, text="EXIT", command=window,width=18, height=1,font=('Georgia', 20, ' bold '), bg="#226597", fg="#F3F9FB")
exit.place(x=200, y=450)

root.mainloop()