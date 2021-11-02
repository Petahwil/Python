import random

def coinflip(): 
    # start trials at one because there is one round that is not counted with the if or else statement
    trials = 1
    if random.randint(0, 1) == 0:
    # while it is heads add to trials
        while random.randint(0, 1) == 0:
            trials += 1
    # add one becasue the coin was flipped but it was tails so the loop wont count it
        return trials + 1
    else:
    # while it is tails add to trials
        while random.randint(0, 1) == 1:
            trials += 1
    # add one becasue the coin was flipped but it was heads so the loop wont count it
        return trials + 1

flips,rounds= (0,0)
rounds = 10_000
for i in range(rounds):
    # get how many flips happened in the trail and add it to flips
    flips += coinflip()
#devided total flip count by rounds to get average        
avg = flips/rounds
print (f'The average number of coin flips: {avg}')

