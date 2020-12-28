#Programmed by Florian Michael
#since 28.12.2020
#
#Example for Dynamic typing
#In Python, variables are not bound to types, in most programming languages, 
#when declaring a variable, it is immediately determined which type it has,
# this type can then often no longer be changed. Example: (Java)
#int a = 10;
#A is now a natural number, you can only change the value of a but not the type. 
#With Python this is possible:
#
a = 10
#Now a is a Integer
a = "Test"
#Now a is a String
print ("Dynamic Types are cool: ", a)
print ("Next Step")
a = 5
print ("Value: ", a)
a = 5.3
print ("Value: ", a)