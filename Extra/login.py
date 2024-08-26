from tkinter import*
import tkinter as tk
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk


root = tk.Tk() 

root.geometry('500x500')  
root.title("login page")  
w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))


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

   
image2= Image.open("wallpaperflare.com_wallpaper (9).jpg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

canvas=tk.Canvas(root,background="#3D59AB",borderwidth=5)
canvas.place(x=310,y=230,width=440,height=400)

img = Image.open(r'pngtree-vector-users-icon-png-image_856952.jpg')
img = img.resize((100,100), Image.ANTIALIAS)
logo_image = ImageTk.PhotoImage(img)

logo_label = tk.Label(root, image=logo_image)
logo_label.image = logo_image
logo_label.place(x=440, y=230)
  
labl_1 = tk.Label(root, text="Username",width=10,font=("bold", 13),bg="#3D59AB")  
labl_1.place(x=315,y=350)  
  
entry_1 = tk.Entry(root,textvariable=username)  
entry_1.place(x=420,y=350,height=20,width=150)  

labl_2= tk.Label(root, text="Password",width=10,font=("bold", 13),bg="#3D59AB")  
labl_2.place(x=315,y=400)  

entry_2 = tk.Entry(root,show="*",textvariable=password)  
entry_2.place(x=420,y=400,height=20,width=150)

tk.Button(root, text='Submit',width=14,bg='green',fg='black',font=18,command=login).place(x=430,y=450)  
tk.Button(root, text='Forget password',width=14,bg='light blue',fg='black',command=forget,font=18).place(x=330,y=520)
tk.Button(root, text='Create Account',width=14,bg='orange',fg='black',font=18,command=registration).place(x=550,y=520)  
 

root.mainloop()