from tkinter import *
import time
import ttkthemes
from tkinter import ttk




#functionality part
count =0
text=''
def slider():
    global text, count
    if count==len(s): ##this block of code is for repeating sms again as it reaches the end of spelling
        count=0
        text=''
    text =text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(150,slider)

def clock():
    date=time.strftime('%d/%m/%y') # used to showing day month and year format
    currenttime=time.strftime('%H:%M:%S') #for hours minutes and seconds
    datetimeLabel.config(text=f' Date: {date}\nTime: {currenttime}') #\n = new line character
    datetimeLabel.after(1000,clock)






#GUI part
root=ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('smog')


root.geometry('1174x680+0+0')
root.resizable(0,0)   #here 0,0 is same as [flase , flase]
root.title('Student Management System')

datetimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'),fg='purple')
datetimeLabel.place(x=5,y=5)
clock()



#creating a slider 
s='Student Management System'
sliderLabel=Label(root,font=('times new roman',28,'bold'),fg='Black',width=30)
sliderLabel.place(x=200,y=0)
slider()


#creating a button
connectButton=ttk.Button(root,text='Connecet to the Database')
connectButton.place(x=980,y=0)

#creating left frame
leftFrame=Frame(root,)
leftFrame.place(x=50,y=80,width=300,height=600)


#importing image in left Frame
logo_image=PhotoImage(file='best1.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid (row=0,column=0,pady=20)

#adding buttons 
addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25)
addstudentButton.grid(row=1,column=0,pady=20)


searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25)
searchstudentButton.grid(row=2,column=0,pady=20)




deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25)
deletestudentButton.grid(row=3,column=0,pady=20)




updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25)
updatestudentButton.grid(row=4,column=0,pady=20)




showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25)
showstudentButton.grid(row=5,column=0,pady=20)


exportstudentButton=ttk.Button(leftFrame,text='Export Data',width=25)
exportstudentButton.grid(row=6,column=0,pady=20)


exitButton=ttk.Button(leftFrame,text='Exit')
exitButton.grid(row=7,column=0,pady=20)






#now creating the right frame
rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)



ScrollbarX=Scrollbar(rightFrame,orient=HORIZONTAL)
ScrollbarY=Scrollbar(rightFrame,orient=VERTICAL)


studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile Number','Address','Gender',
                                              'D.O.B','Email','Added Date','Added Time'),
                                              xscrollcommand=ScrollbarX.set,yscrollcommand=ScrollbarY.set)
ScrollbarX.config(command=studentTable.xview)
ScrollbarY.config(command=studentTable.yview)


studentTable.pack(fill=BOTH,expand=1)



ScrollbarX.pack(side=BOTTOM,fill=X)
ScrollbarY.pack(side=RIGHT,fill=Y)

studentTable.heading('Id',text='Id')

root.mainloop()

