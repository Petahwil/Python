class Farm():
    # eating = 'is eating'
    # running = 'is running'
    # walking = 'is walking'
    def __init__(self,farmName):
        self.farmName = farmName
    def sleeping(sleeper):
        return (f"{sleeper} is sleeping")
    # def __str__(self):
    #     return (f"You are at {self.farmName}.")

class Animals(Farm):
    pass
class Farmers(Farm):
    def __init__(self,farmName,farmerName,sex,age):
        super().__init__(farmName)
        self.farmerName = farmerName
        self.sex = sex
        self.age = age
    def __str__(self):
        if self.sex.upper() == 'MALE':
            return (f"{self.farmerName} works at {self.farmName}. He is {self.age} years old")
        if self.sex.upper() == 'FEMALE':
            return (f"{self.farmerName} works at {self.farmName}. She is {self.age} years old")
        return (f"{self.sex} is not a valid type")


tim = Farmers("Milky's Farm",'Tim','Male','32')
print(tim)
print(Farm.sleeping(tim.farmerName))
