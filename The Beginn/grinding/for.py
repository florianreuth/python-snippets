#Programmed by Florian Michael
#since 29.12.2020
#
#Examples for for in Python
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for aEntry in a:
    print ("Value ", aEntry)

#If you want to Access to Fields in Lists:
b = [5, 8, 10, 4]
print ("Before Edit ", b)
for bEntry in enumerate(b):
    b[bEntry[0]] = bEntry * 2
print ("After Edit ", b)

#Repeat Command with specific Count
for count in range (100):
    print (count + 1)

print ("Next Step")        
#Print Count with Min and Max
for count in range (5, 10):
    print (count + 1)
    
print ("Next Step")    
#Break in For
for count in range (10, 99):
    print (count + 1)
    if count == 10:
        break
        
print ("Next Step")    
#You can Add else: if break not exec        
for count in range (10, 99):
    print (count + 1)
    if count == 10:
        break
else:
    print ("Break not exec")

print ("Next Step")    
#Continue in For
objectList = [12, 18, 3, 6, 0, 46, 234, 23]
value = eval(input("Please enter A Number: "))
for objectListEntry in objectList:
    if objectListEntry == 0:
        print ("This is not possible")
        continue
    print (value / objectListEntry)    