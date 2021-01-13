class Car:
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age = Age

class SUV(Car): # This Class extends the Car Class and use their Args
    def __init__(self, Name, Age, Other):
        Car.__init__(self, Name, Age)
        self.Other = Other

test = SUV("Mercedes-Benz", 2014, "Spacer")
print (test.Name)
print (test.Other)