from tkinter import*
import tkinter as tk 
from tkinter import messagebox as ms
from PIL import Image, ImageTk
import sqlite3

root=tk.Tk()
root.configure(background='white')
w,h=root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("Forget Password")


image2= Image.open("pxfuel (8).jpg")
image2=image2.resize((w,h),Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label=tk.Label(root,image=background_image)

background_label.image=background_image

background_label.place(x=0,y=0)

email= tk.StringVar()
password = tk.StringVar()
confirmPassword = tk.StringVar()

db = sqlite3.connect('crop1.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Fullname TEXT, address TEXT, Email TEXT, age TEXT, Gender TEXT, Phoneno TEXT, password TEXT)")
db.commit()




def change_password():
    
    
    #Email=email.get()
    new_password_entry = password.get()
    confirm_password_entry = confirmPassword.get()
    
    with sqlite3.connect('air writing1.db') as db:
        c = db.cursor()

    
    find_user = ('SELECT * FROM registration WHERE Email=?')
    c.execute(find_user, [(str(email.get()))])
    
    
    #find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
    #c.execute(find_entry, [(email.get()), (password.get())])
    
    result = c.fetchall()
    if result:
        if new_password_entry == confirm_password_entry:
            db = sqlite3.connect("air writing1.db")
            curs = db.cursor()
    
            curs.execute("update registration set password=? WHERE Email=? ",(str(new_password_entry),email.get()))
            #curs.execute(insert, [new_password_entry ])
            db.commit()
            db.close()
            ms.showinfo('Congrats', 'Password changed successfully')
    
    else:
            ms.showerror('Error!', "Passwords didn't match")





# frame=Frame(root,bg="black")
# frame.place(x=10,y=150,height=300,width=400)

labl_1 =tk.Label(root, text="forgot password",width=15,font=("bold", 40),bg="white")  
labl_1.place(x=350,y=200) 

labl_1 =tk.Label(root, text="Email",width=10,font=("bold", 13),bg="white")  
labl_1.place(x=370,y=330)  
  
entry_1 =tk.Entry(root,textvariable=email)  
entry_1.place(x=550,y=330,height=20,width=150)  

labl_2=tk.Label(root, text="New Password",width=15,font=("bold", 13),bg="white")  
labl_2.place(x=370,y=370)  

new_password_entry =tk.Entry(root,textvariable=password)  
new_password_entry.place(x=550,y=370,height=20,width=150)


labl_2=tk.Label(root, text="Confirm Password",width=15,font=("bold", 13),bg="white")  
labl_2.place(x=370,y=420)  

confirm_password_entry =tk.Entry(root,textvariable=confirmPassword)  
confirm_password_entry.place(x=550,y=420,height=20,width=150)


forget_button = tk.Button(root, text="Forgot Password", font=("bold", 14), bg="red", fg="black", padx=20, pady=10,command=change_password)
forget_button.place(x=470, y=500,height=35, width=150)









root.mainloop()