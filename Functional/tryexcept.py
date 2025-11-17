#since 13.01.2020
#
#Try Catch Examples
import testerror
import sys

from testerror import TestError

try:
    print ("Test")
except ValueError: #Set Error
    print ("Rofl")    

print ("Next Step") 
try:
    print ("ASD")
except (ValueError, EnvironmentError):
    print("ASD123")       

print ("Next Step")    

try:
    print ("Test")
except ValueError: #Set Error
    print ("Rofl")    
except: #Default in SwitchCase (Java)
    print ("Error: ", sys.exec_info()[0])
else: #Success
    print ("Success!")    
finally: #This calls before close programm so High Perm
    print ("Pip.Gc") #Like Java

print ("Next Step")    
try:
    print ("Test")
    raise TestError("Test")
except TestError as fehler: #Set Error
    print ("Rofl")    


