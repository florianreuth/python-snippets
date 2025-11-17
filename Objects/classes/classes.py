class Test:
    """
    This is a Example Class for Object Programming in Python 3
    """

    #Static Vars before __init__ (Java: Constructor)
    countOfTest = 0

    def __init__(self, name, age, __hobby):
        Test.countOfTest += 1
        """
        These are some Test Vars
        """
        self.Name = name
        self.Age = age
        self.__Hobby = __hobby #It is not possible to edit this and you can not access this like (Java: Protected & Final)
                                                # <-
    def getHobby(self): #Bypass for Access 
        return self.__Hobby    

testInstance = Test("Florian", 13, "Programming")
print (testInstance.Name)
print (testInstance.getHobby()) #Access Var

print (Test.countOfTest) #Access Var

"""
Def in Classes are Methods, Def out of Classes are Functions
"""
