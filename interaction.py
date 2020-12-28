#Programmed by Florian Michael
#since 28.12.2020
#
#Example for Interaction with the User
print ("Please enter something")
text = input()
text = text * 2
print ("Output: ", text)
#When using the eval() function, keep in mind that the user 
#could also insert Python command code and it will be executed, 
#this poses a high security risk:
print ("Next Step")
print ("Please enter something")
text = eval(input())
text = text * 2
print ("Output: ", text)
#The input method can also directly output 
#something when asked to enter something:
print ("Last Step")
print ("")
finalText = input("Please enter something>> ")
print("Last Value: ", finalText)