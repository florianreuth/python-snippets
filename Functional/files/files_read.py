#since 15.01.2020
#
#Files in Python
#Permission Level List:
# 
# 'r' - Only Read
# 'w' - Only Write (override exists File)
# 'a' - Add New Stuff to Current File
# 'r+' - Read and Write
#
#Path is like Java (So only File Name = RUN_DIRECTORY/FILE_NAME or Path and File name = INPUT)
#Python creates the file if it does not exist, but the folders at the 
#path must already exist
input = eval(input("Please enter readType: "))
if input == "simple":
    f = open("test.txt", "r")

    content = f.read()
    print (content)
else:
#!!!! If you read Things, The Things are removed from the Object 

#You can use readLine() Function to Read Line and go to next but there is no end and you need a While Statement to do THis (So Shitty)

#You Can use readLines() to get A List with all Lines
    contentList = f.readlines() 
    length = int(len(contentList)) 
    print ("List Size", length)

#Close the File to remove it from WorkSpace
f.close()    
