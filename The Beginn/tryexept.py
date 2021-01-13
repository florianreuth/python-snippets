#Programmed by Florian Michael
#since 13.01.2020
#
#Try Catch Examples
try:
    print ("Test")
except ValueError: #Set Error
    print ("Rofl")    

print ("Next Step") 
try:
    print ("ASD")
except (ValueError, EnvironmentError):
    print("ASD123")       