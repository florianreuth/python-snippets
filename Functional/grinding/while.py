#since 29.12.2020
#
#Examples for while in Python
a = 1
while a <= 100:
    print (a)
    a += 1
    
continueValue = "Yes"
while continueValue == "Yes":
    print ("Which number do you want to multiply?")
    number = eval(input())
    print (number*2)
    print ("Do you want to continue?")
    continueValue = input()
