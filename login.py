from tkinter import*
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3 #helps to work on multiple db and does not require a seperate server process maikng it flexible
from PIL import Image, ImageTk


root = tk.Tk() 
 
root.title("login page")  
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.state("zoomed")



############################################# DATABASE CONNECTION ################################################
username = tk.StringVar()
password = tk.StringVar()


def forget():
    from subprocess import call
    call(["python","forgot password.py"])
def registration():
    from subprocess import call
    call(["python","registration.py"])
    root.destroy()

def login():
        # Establish Connection

    with sqlite3.connect('evaluation.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('evaluation.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
                           "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM admin_registration WHERE username = ? and password = ?')
         c.execute(find_entry, [(username.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            # self.logf.pack_forget()
            # self.head['text'] = self.username.get() + '\n Loged In'
            # msg = self.head['text']
            #            self.head['pady'] = 150
            print(msg)
            ms.showinfo("messege", "LogIn sucessfully")
            # ===========================================
            # root.destroy()

            from subprocess import call
            call(['python','GUI_Master.py'])
            
            # root.destroy()
            
         # ================================================
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')

################################################# LOGIN PAGE ###################################################

# canvas=tk.Canvas(root,background="black",borderwidth=5)
# canvas.place(x=0,y=0,width=700,height=500)

   
image2= Image.open("wallpaperflare.com_wallpaper (9).jpeg")
image2=image2.resize((w,h),Image.ANTIALIAS) #reduces bandwidth by removing high frequency

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

canvas=tk.Canvas(root,background="#226597") #add structured graphics to application
canvas.place(x=100,y=150,width=440,height=400)

img = Image.open(r'pngtree-vector-users-icon-png-image_856952.png')
img = img.resize((100,100), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=270, y=185)
  
labl_1 = tk.Label(root, text="USERNAME",width=10,font=("Georgia", 14, "bold"),bg="light blue")
labl_1.place(x=180,y=320)
  
entry_1 = tk.Entry(root,textvariable=username)  
entry_1.place(x=330,y=320,height=31,width=150)

labl_2= tk.Label(root, text="PASSWORD",width=10,font=("Georgia", 14, "bold"),bg="light blue")
labl_2.place(x=180,y=370)

entry_2 = tk.Entry(root,show="*",textvariable=password)  
entry_2.place(x=330,y=370,height=31,width=150)

tk.Button(root, text='SUBMIT',width=16,bg='#113F67',fg='white',font=("Georgia", 12, "bold"),command=login).place(x=230,y=430)
tk.Button(root, text='FORGET PASSWORD',width=16,bg='#113F67',fg='white',command=forget,font=("Georgia", 12, "bold")).place(x=130,y=490)
tk.Button(root, text='CREATE ACCOUNT',width=16,bg='#113F67',fg='white',font=("Georgia", 12, "bold"),command=registration).place(x=330,y=490)
 

root.mainloop()