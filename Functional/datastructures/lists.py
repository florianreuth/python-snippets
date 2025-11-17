#since 28.12.2020
#
#Examples to use Lists in Python
#Declaration:
informationList = ["Hello", "World", 1337, 1510]
#Getting:
print (informationList[0]) #Get "Hello"
print (informationList[0:2]) #Get "Hello", "World" but not 1337 because 0:CAUSE-1 (Format=Arrays.asList)
print (informationList[-1]) #Get Last Object in the List (1510)
informationList[0] = "Test"
print (informationList[0])
print ("Next Step")
informationList = informationList + ["1010"] #Add new Object in the List
print ("Next Step")
moreDimensions = [["Test", "VW"], ["WORLD", "Hello"]] #Two Dimension List
print ("1 List: ", moreDimensions[0])
print ("2 List: ", moreDimensions[1])
print ("Next Step")
print ("Value from 1 Element in 1 List: ", moreDimensions[0][0])
print ("Value from 2 Element in 1 List: ", moreDimensions[0][1])
print ("Value from 1 Element in 2 List: ", moreDimensions[1][0])
print ("Value from 2 Element in 2 List: ", moreDimensions[1][1])
