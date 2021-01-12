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