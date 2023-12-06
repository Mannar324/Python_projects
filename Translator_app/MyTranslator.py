
from tkinter import *
import customtkinter as ctk
from tkinter import ttk
from translateapp import *

# interface of the app
app = ctk.CTk()
app.title("My Translator")
ctk.set_appearance_mode("dark")
app.resizable(False,False)
app.geometry("800x600")  # Fix the geometry string format

# Load your background image
background_image = PhotoImage(file="background.png")  # Replace with your image file path
background_label = Label(app, image=background_image)  # Corrected widget class name
background_label.place(relwidth=1, relheight=1)  # Make the label fill the entire window
appname=Label(app,text="Welcome to my translator ",bg="#FFF5E0",font="Engraves 20 bold",fg="black")
appname.place(x=370,y=0)

#create select box for input language
inputlabel=Label(app,text="Enter Text ",bg="#FFF5E0",font="Engraves 26 bold",fg="black")
inputlabel.place(x=100,y=150)
selectinput=ttk.Combobox(app,values=language)
selectinput.set("select input langauge")
selectinput.place(x=100,y=200,width=200)

#create textbox for input
inputext=Text(width=40,height=20)
inputext.place(x=50,y=230)

#create select box for output language
outputlabel=Label(app,text="output Text ",bg="#FFF5E0",font="Engraves 20 bold",fg="black")
outputlabel.place(x=600,y=150)
selectoutput=ttk.Combobox(app,values=language)
selectoutput.set("select input langauge")
selectoutput.place(x=660,y=200,width=200)

#create textbox for input
outputext=Text(width=40,height=20)
outputext.place(x=650,y=230)

# method to translate the text
def Translate():
    #codes=languages_dic()
    translator=Translator()
    translatedtext=translator.translate(inputext.get("1.0",END),src=selectinput.get(),dest=selectoutput.get())
    #outputext.delete("1.0",END)
    outputext.insert("1.0",translatedtext.text)
def Clear():
    outputext.delete("1.0",END)
    inputext.delete("1.0",END)
# translate button
translatebutton=Button(master=app,text="translate",fg="#B4B4B3",font=('Engraves',20,'bold'),command=Translate)
translatebutton.place(x=430,y=600) 
#clear button
clearimg=PhotoImage(master=app,file="clear.png")
clearbutton=Button(master=app,image=clearimg,width=150,height=60,command=Clear)
clearbutton.place(x=430,y=700)    
    
app.mainloop()

