class Farm:
    def __init__(self,farmName):
        self.farmName = farmName
    def farmLocation(self):
        print (f"{self.name} is a {self.animal} at {self.farmName}")
    def sleeping(self):
        print (f"{self.name} is sleeping")
    def running(self):
        print (f"{self.name} is running around {self.farmName}!!")
    def walking(self):
        print (f"{self.name} is walking around {self.farmName}")
    def eating(self):
        print (f"{self.name} is eating")
    def aNoise(self):
        print(f"{self.animal} goes {self.noise}")
    def info(self,farm):
        print(f'{self.farmName} Details')
        print('===================')
        farmerCount = 0   
        animalCount = 0 
        for farm in farm:
            if farm.animal == 'Farmer' and farm.farmName.upper() == self.farmName.upper():
                farmerCount += 1
            elif farm.farmName.upper() == self.farmName.upper():
                animalCount += 1
        print(f'{self.farmName} has {farmerCount} farmer(s) and {animalCount} animal(s)')
    def __str__(self):
     return (f"{self.farmName}")
    

class Animals(Farm):
    noise = 'silent'
    animal = 'Animal'
    def __init__(self,farmName,name,sex,age):
        super().__init__(farmName)
        self.name = name
        self.sex = sex
        self.age = age
    def __str__(self):
        if self.sex.upper() == 'MALE':
            return (f"{self.name} is a {self.animal} at {self.farmName}. He is {self.age} years old")
        if self.sex.upper() == 'FEMALE':
            return (f"{self.name} is a {self.animal} at {self.farmName}. She is {self.age} years old")
        return (f"{self.sex} is not a valid type")

class Cow(Animals):
    noise = 'Moo'
    animal = 'Cow'

class MilkCow(Cow):
    noise = 'Moo'
    animal = 'Cow'
    def aNoise(self):
        print(f"{self.name} the {self.animal} is {self.noise}ing becasue they need to be milked")

class BeefCow(Cow):
    noise = 'Moo'
    animal = 'Cow'
    def aNoise(self):
        print(f"{self.name} the {self.animal} is {self.noise}ing becasue they want to")

class Sheep(Animals):
    noise = 'Baahhh'
    animal = 'Sheep'
    def eating(self):
        print (f"{self.name} the {self.animal} is eating people RUNN!!")

    
class Farmers(Farm):
    noise = 'silent'
    animal = 'Farmer'
    def __init__(self,farmName,name,sex,age):
        super().__init__(farmName)
        self.name = name
        self.sex = sex
        self.age = age
    def __str__(self):
        if self.sex.upper() == 'MALE':
            return (f"{self.name} is a {self.animal} that works at {self.farmName}. He is {self.age} years old")
        if self.sex.upper() == 'FEMALE':
            return (f"{self.name} is a {self.animal} that works at {self.farmName}. She is {self.age} years old")
        return (f"{self.sex} is not a valid type")


def main():
    tim = Farmers("Milky's Farm",'Tim','Male','32')
    sally = Animals("Milky's Farm",'Sally','Female','4')
    kali = MilkCow("Milky's Farm",'Kali','Male','7')
    bob = BeefCow("Hemp Farm",'Bob','Male','3')
    dan = Sheep("Hemp Farm",'Dan','Male','1')
    tommy = Farmers("Hemp Farm",'Tommy','Male','73')
    tim.farmLocation()
    tim.sleeping()
    print(kali)
    dan.farmLocation()
    kali.running()
    print(sally)
    bob.walking()
    bob.aNoise()
    kali.aNoise()
    dan.aNoise()
    dan.eating()
    sally.aNoise()
    tim.aNoise()
    Farm("Milky's Farm").info([tim,sally,tommy,kali,dan,bob])
    Farm("Hemp Farm").info([tim,sally,tommy,kali,dan,bob])

main()