from  tkinter  import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='': #nothing in there means null
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Dee'and passwordEntry.get()=='2118':
        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import sms
        
    else:
        messagebox.showerror('Error','Plese enter correct credentials')



window=Tk()
window.geometry('1920x1080+0+0') #length breadth of widnow + 00 are the distance from x and y axis
window.title('Login System Of Student Management System')
# window.resizable(False, False)  #if i want ot disable button 


#uploading a bg image
backgroundImage=ImageTk.PhotoImage(file='bg1.jpg') 
bgLabel = Label(window,image=backgroundImage) 
bgLabel.place(x=0,y=0) # 0,0 coordinate value

loginFrame = Frame(window, bg='black')
loginFrame.place(x=500, y=150)

#creating a logo
logoImage=PhotoImage(file='student.png')
logoLabel=Label(loginFrame,image=logoImage)
logoLabel.grid(row=0,column=0,columnspan=2,pady=10) # span is used from logo to take both 0,1 value when the username value or image is added



# creating user name text and uploading image  adding values to it
usernameImage=PhotoImage(file='username.png')
usernameLabel=Label(loginFrame,image=usernameImage ,text='Username',compound =LEFT ,bg='white'  ,font=('Pt times new roman',16,'bold'))
usernameLabel.grid (row=1,column=0,pady=10,padx=20)

usernameEntry=Entry(loginFrame,font=('Pt Times New Roman',16,'bold'),bd=5,fg='black')   #making space to enter values
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


#creating password
passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage ,text='Password',compound =LEFT ,bg='white'  ,font=('Pt Times new roman',16,'bold'))
passwordLabel.grid (row=2,column=0,pady=10,padx=20)

passwordEntry=Entry(loginFrame,font=('Pt times new roman',16,'bold'),bd=5,fg='black')   #making space to enter values
passwordEntry.grid(row=2,column=1,pady=10,padx=20)


#creating a button
loginButton=Button(loginFrame,text='LOGIN',font=('Pt Times new roman',15,'bold'),
width=15, fg='white',bg='black',
cursor='hand2', command=login)
loginButton.grid(row=3,column=1,pady=10)






window.mainloop() #to see window contineously


