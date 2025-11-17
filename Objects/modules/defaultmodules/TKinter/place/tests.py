from tkinter import *

window = Tk() #Create A Window

window.geometry("300x100") #Set Window Size

window.title("First TKinter Program") #Set Window Title

testFrame = Frame(window, relief = "ridge", borderwidth = 5) #Create Border with width 20 and ridge Design
testFrame.pack(fill="both", expand=1) #Expand the Border to the whole Screen

welcomeText = Label(testFrame, text = "Welcome to TKinter!") #Create a Text (Add Border)
welcomeText.grid(row = 1, column = 1, columnspan = 2, pady = 15, padx = 50) #Distance

okButton = Button(testFrame, width = 10, text = "Ok!")
okButton.grid(row = 2, column = 1, pady = 10)

cancelButton = Button(testFrame, width = 10, text = "Cancel!")
cancelButton.grid(row = 2, column = 2)

window.mainloop() #Loop the Window and Render it