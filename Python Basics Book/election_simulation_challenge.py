# Suppose two candidates, Candidate A and Candidate B, are running
# for mayor in a city with three voting regions. The most recent polls
# show that Candidate A has the following chances for winning in each
# region:
# • Region 1: 87% chance of winning
# • Region 2: 65% chance of winning
# • Region 3: 17% chance of winning
# Write a program that simulates the election 10,000 times and prints
# the percentage of where Candidate A wins.
# To keep things simple, assume that a candidate wins the election if
# they win in at least two of the three regions.

# import random

# # my first and un-assisted try
# # #using the biased random win generatior
# def region_precent(chance_of_winning):
#     if random.random() < chance_of_winning:
#         return "wins"

# btotal, atotal = (0,0)
# rounds = 10_000
# for i in range(rounds):
#     awins = 0
#     # candidate a has %87 in regin one if they won add to a wins
#     if region_precent(.87) == 'wins':
#         awins += 1
#     # candidate a has %65 in regin one if they won add to a wins
#     if region_precent(.65) == 'wins':
#         awins += 1
#     # candidate a has %17 in regin one if they won add to a wins
#     if region_precent(.17) == 'wins':
#         awins += 1
#     # if a wins 2 or more regins then add to a total wins otherwise add to b total wins
#     if awins >= 2:
#         atotal += 1
#     else:
#         btotal +=1

# print (f'Candidate A has a %{round((atotal/rounds)*100)} chance of winning')
# print (f'Candidate B has a %{round((btotal/rounds)*100)} chance of winning')


# import random imports the random module, which contains a variety of things to 
# do with random number generation. Among these is the random() function, which 
# generates random numbers between 0 and 1. Doing the import this way this requires
# you to use the syntax random.random(). The random function can also be imported
# from the module separately: from random import random. This allows you to then 
# just call random() directly.


# After seeing solution tweeking my first try
from random import random

btotal, atotal = (0,0)
awinprec = [0.87,0.65,0.17]
rounds = 10_000
for i in range(rounds):
    awins = 0
    # go through the array 
    for i in range(len(awinprec)):
    # run biased random based on A % to win in that regin
        if random() < awinprec[i]:
            awins += 1
    # if a wins 2 or more regins then add to a total wins otherwise add to b total wins
    if awins >= 2:
        atotal += 1
    else:
        btotal +=1

print (f'Candidate A has a %{round((atotal/rounds)*100)} chance of winning')
print (f'Candidate B has a %{round((btotal/rounds)*100)} chance of winning')

