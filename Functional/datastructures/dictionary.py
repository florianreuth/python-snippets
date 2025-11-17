#since 28.12.2020
#
#Examples to use Dictionaries in Python
#Declaration:
personalInformations1 = {"name": "Florian", "familiyname": "???"}
personalInformations2 = dict([("name", "Florian"), ("familiyname", "???")])
personalInformations3 = dict(name="Florian", familiyname="???")
#Getting:
print ("The name is ", personalInformations1["name"])
print ("The familiyname is ", personalInformations1["name"])
print ("Next Step")
personalInformations1["age"] = "13" #Add 'Age' with Key '13' to 'personalInformations1' 
print ("Add Age to List")
print ("The Age is ", personalInformations1["age"])
del personalInformations1["age"] #Remove 'Age' from 'personalInformations1'
print ("Remove Age from List")

print (list(personalInformations1.keys())) #List all Keys from 'personalInformations1'
print (list(personalInformations1.values())) #List all Values from 'personalInformations1'

print (sorted(personalInformations1.keys())) #Collect all Keys from 'personalInformations1' after Alphabet
print (sorted(personalInformations1.values())) #Collect all Values from 'personalInformations1' after Alphabet 
