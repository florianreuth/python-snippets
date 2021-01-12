#Programmed by Florian Michael
#since 29.12.2020
#
#Examples for IF KeyWord in Python
a = "Test"
if a == "Test":
    print("Meddl") 

print("Next Step")    

b = 5
c = eval(input())
if b == 5 and c == 4:
    print("Ok!")
    
print("Next Step")   
 
if not c > 5:
    print("C is not bigger than 5")

print("Next Step")    

if not (c > 5 and b == 5):
    print("This is ez")

print("Next Step")    
a = "Test"
b = "Exploit"

if a == "Test" or b == "Meddl":
    print("Ok Now it works")
    
print("Next Step")    

if not (a == "Test" or b == "Meddl"):
    print("Ok Now it works222")
