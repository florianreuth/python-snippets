#Programmed by Florian Michael
#since 29.12.2020
#
#Python Functions
# 
def printRandomStuff ():
    print ("Hello Rofl")
    print ("For asdasd")

#Main-method (Later with __name__ case)
print ("Hello Guys")    
printRandomStuff()

#
# You can Use Vars
#
print ("Next Step")

def multi (inputCount):
    print (int(inputCount) * 2)

multi(10)

#
# You can use with Default Args
#
print ("Next Step")

def defaultArg (name = "Hello"):
    print ("Your Name is follow: ", name)

defaultArg()
defaultArg("Custom")
#If you want to Set a Specific Arg, you need to call it
defaultArg(name = "Custom")

#
# You can Return Values
#
print ("Next Step")

def getMulti (count):
    return count * 2 # You can Return Everything like Dicts, Lists, Integers, Strs, ...

print ("The Multi of 2 is: ", getMulti(2))    

#
# You can use if else for returns to return other things with diffrent stages but i think a example 
# for this is very useless
#