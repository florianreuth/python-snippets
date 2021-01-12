import test_module
import folder.folder_module

simpleModule = folder.folder_module # You dont need to import the Module before

print (test_module.getShit())
print (folder.folder_module.getShit())
print ("Next Step")
print (simpleModule.getShit())