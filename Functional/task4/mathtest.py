#since 29.12.2020
#
#Simple Math Test
points = 0
userInput = ""

print ("Enter the Result of 4 + 4: ")
userInput = eval(input())
if (userInput == 8):
    points = points + 1
    print ("Yes! +1 Point")
else:
    print ("No! No Points")
    
print ("Enter the Result of 2 + 4: ")
userInput = eval(input())
if (userInput == 6):
    points = points + 1
    print ("Yes! +1 Point")
else:
    print ("No! No Points")
    
print ("Enter the Result of 1 + 8: ")
userInput = eval(input())
if (userInput == 9):
    points = points + 1
    print ("Yes! +1 Point")
else:
    print ("No! No Points")
    
print ("Enter the Result of 1000 + 8: ")
userInput = eval(input())
if (userInput == 1008):
    points = points + 1
    print ("Yes! +1 Point")
else:
    print ("No! No Points")
    
print ("Enter the Result of 5 * 5: ")
userInput = eval(input())
if (userInput == 25):
    points = points + 1
    print ("Yes! +1 Point")
else:
    print ("No! No Points")
    
if points == 5:
    print ("Very Good")
elif points > 3:
    print ("Good")
elif points > 1:
    print ("Okay")
else:
    print (":(")
