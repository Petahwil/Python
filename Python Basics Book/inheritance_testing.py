bikes = {
'TREK':{
'bad': ['Roscoe 8',
'Roscoe 7',
'Marlin 8',
'Marlin 6',
'Marlin 5',
'Marlin',
'Roscoe 6',
'Marlin 7',
'roscoe',
'820 WSD',
'Roscoe 20'],

'good': ['Madone SLR 9',
'slash',
'Madone SLR 9 eTap',
'Domane+ LT 9',
'Domane SLR 9',
'Checkpoint SLR 9 eTap',
'Madone SLR 7 eTap',
'Domane+ LT 7',
'Madone',
'Émonda',
'Checkpoint SLR 7',
'Checkpoint',
'Domane']
    },

'MARIN':{
'bad' : ['San Quentin 1', 'fairfax', 'kentfield', 'bobcat',],
'good' : ['San Quentin', 'San Quentin 2', 'rift zone', 'alpine trail', 'alcatraz']
}
}

class BikeRating:
    def run(self,bike):
        print('Rating Bikes')
        print('===================')     
        for bike in bike:
            print(f'{bike.bikeRating()}')

class Bike():
    wheels = 'two'
    def __init__(self,bikeBrand, bikeName):
        self.bikeBrand = bikeBrand
        self.bikeName = bikeName
    def __str__(self):
        return (f'{self.bikeBrand} {self.bikeName}')


class CreateBiker(Bike):
    def __init__(self,riderName,bikeBrand,bikeName):
        super().__init__(bikeBrand, bikeName)
        self.riderName = riderName
    def bikeRating(self):
        print(f'Hello {self.riderName}')
        print (f"Oh you have a {self}! Lets see if its cool {self.riderName}..")
            # converting bike name to upper and list to upper so everything is the same when compared
        if self.bikeName.upper() in (x.upper() for x in bikes[self.bikeBrand.upper()]['bad']):
            return (f"Your Bike Sucks {self.riderName}! Time to Upgrade!\n")
        if self.bikeName.upper() in (x.upper() for x in bikes[self.bikeBrand.upper()]['good']):
            return (f"Your Bike Is Sick {self.riderName}! Keep Ripping!\n")
        return (f"Your Bike Wasn't Found It Must Suck {self.riderName}! Time to Upgrade!\n")

toms_bike = CreateBiker('Tom','Trek','Marlin 5')
tims_bike = CreateBiker('Tim','Marin','Alcatraz')
BikeRating().run([toms_bike, tims_bike])

#Start
# class BikeRating:
#     def bikeRating(self,bike):
#         print('Rating Bikes')
#         print('===================')     
#         for bike in bike:
#             print(f'{bike.bikeRating()}')

# class Bike:
#     wheels = 'two'
#     def __init__(self,riderName,bikeName):
#         self.bikeName = bikeName
#         self.riderName = riderName


# class Trek(Bike):
#     def __init__(self,riderName,bikeName):
#         super().__init__(riderName,bikeName)
#     def bikeRating(self):
#         print(f'Hello {self.riderName}')
#         print (f"Oh you have a Trek {self.bikeName}! Lets see if its cool {self.riderName}..")
#         if self.bikeName.upper() == 'ROSCO':
#             return (f"Your Bike Sucks {self.riderName}! Time to Upgrade!\n")
#         if self.bikeName.upper() == 'SLASH':
#             return (f"Your Bike Is Sick {self.riderName}! Keep Ripping!\n")
#         return (f"Your Bike Wasn't Found It Must Suck {self.riderName}! Time to Upgrade!\n")



# toms_bike = Trek('Tom','Rosco')
# tims_bike = Trek('Tim','Slash')
# bike_rating = BikeRating()
# bike_rating.bikeRating([toms_bike,tims_bike])