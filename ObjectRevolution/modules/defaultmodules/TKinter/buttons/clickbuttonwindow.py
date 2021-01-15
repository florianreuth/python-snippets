from tkinter import *

class StartButton(Button):

    def action(self):
        print ("Test")

window = Tk() #Create A Window

window.geometry("400x200") #Set Window Size

window.title("First TKinter Program") #Set Window Title

testFrame = Frame(window, relief = "ridge", borderwidth=20) #Create Border with width 20 and ridge Design
testFrame.pack(fill="both", expand=1) #Expand the Border to the whole Screen

welcomeText = Label(testFrame, text = "Welcome to TKinter!") #Create a Text (Add Border)
welcomeText.pack(expand = 1) #Add Text to Window (Expand = 1 ^= Width = width / 2, Height = height / 2 ^= Center)

testButton = StartButton(testFrame, text = "Start the Game") #The TestFrame set this as ..(root) Object
testButton["command"] = testButton.action #Add Method to click
testButton["text"] = "Changed!" #Change the Text 
testButton.pack(side = "bottom") #Set The Position or something else idk

asdButton = Button(testFrame, text = "SAD") # Button Is Over the testButton
asdButton.pack(side = "bottom")

window.mainloop() #Loop the Window and Render it