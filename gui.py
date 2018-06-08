from tkinter import *
myGui = Tk()

def submit():
    b = a.get()
    myLabel3 = Label(text=b,fg='red', bg='yellow').pack()

def delete():
    myLabel4 = Label(text='deleted',fg='red', bg='yellow').pack()

def newfi():
    myLabel4 = Label(text='Clicked on new file',font=('times',24,'bold')).pack()

def mbox():
    messagebox.showinfo(title='no recent files',message='damn you')
    
a = StringVar()   
myGui.title('Hello')

myGui.geometry('500x500+100+50')

myLabel1 = Label(text='Label one',fg='red', bg='yellow').pack()
myButton1 = Button(text='submit',fg='blue',command = submit,font=('arial',24,'italic')).pack()
myButton2 = Button(text='Delete',fg='green',font=('times',24,'bold'),command = delete).pack()
text = Entry(textvariable = a).pack()
mymenu = Menu()
listone = Menu()
listone.add_command(label='New File',command = newfi)
listone.add_command(label='Open....')
listone.add_command(label='Open Module')
listone.add_command(label='Recent Files',command = mbox)
listtwo = Menu()
listtwo.add_command(label='Undo')
listtwo.add_command(label='Redo')
listtwo.add_command(label='Cut')
listtwo.add_command(label='Copy')


mymenu.add_cascade(label='File',menu=listone)
mymenu.add_cascade(label='Edit',menu=listtwo)
mymenu.add_cascade(label='Format')
mymenu.add_cascade(label='Run')
mymenu.add_cascade(label='Options')
myGui.config(menu=mymenu)


myGui.mainloop()
