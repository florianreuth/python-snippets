from tkinter import *

window = Tk() #Create A Window

window.geometry("400x200") #Set Window Size

window.title("First TKinter Program") #Set Window Title

welcomeText = Label(text = "Welcome to TKinter!") #Create a Text
welcomeText.pack() #Add Text to Window

window.mainloop() #Loop the Window and Render it