# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.state("zoomed")
root.title("Speech Emotion Detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('dep1.jpeg')
image2 = image2.resize((w, h), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="SPEECH EMOTION AND FACE RECOGNITION SYSTEM",font=("Georgia", 25, 'bold'),
                    background="#113F67", fg="#F3F9FB", width=85, height=2)
label_l1.place(x=-150, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def test():
    from subprocess import call
    call(["python","test.py"])

def log():
    from subprocess import call
    call(["python","face_Analysis.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="FACE RECOGNITION", command=log, width=20, height=1,font=('Georgia', 20, ' bold '), bg="#113F67", fg="#F3F9FB")
button1.place(x=200, y=250)

button2 = tk.Button(root, text="SPEECH RECOGNITION",command=test, width=20, height=1,font=('Georgia', 20, ' bold '), bg="#113F67", fg="#F3F9FB")
button2.place(x=200, y=400)

button3 = tk.Button(root, text="EXIT",command=window,width=20, height=1,font=('Georgia', 20, ' bold '), bg="#113F67", fg="#F3F9FB")
button3.place(x=200, y=550)
root.mainloop()