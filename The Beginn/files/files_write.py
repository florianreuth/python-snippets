#Programmed by Florian Michael
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
#path must already exist.
f = open('test.txt', 'w')

#Write Content in File
f.write("This is a Test") 

#Create new Line for Sorting
f.write("This is a Test" + "\n")