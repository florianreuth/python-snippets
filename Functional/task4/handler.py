#since 29.12.2020
#
#German
cars = [["VW", "Golf", 2010, 1000],["Spacer1", "Idk1", 1970, 1100],["Meddl", "Loide", 2012, 2000]]
print ("Please enter a Price Maximum: ")
pm = eval(input())
if cars[0][3] <= pm:
    print("This Car: ")
    print("", cars[0][0])
    print("", cars[0][1])
    print("", cars[0][2])
    print("", cars[0][3])
    
if cars[1][3] <= pm:
    print("This Car: ")
    print("", cars[1][0])
    print("", cars[1][1])
    print("", cars[1][2])
    print("", cars[1][3])
    
if cars[2][3] <= pm:
    print("This Car: ")
    print("", cars[2][0])
    print("", cars[2][1])
    print("", cars[2][2])
    print("", cars[2][3])
