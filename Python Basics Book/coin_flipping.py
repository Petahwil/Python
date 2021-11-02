import random
# coin flip simulates the flip and returns a string for 0 (heads) 1 (tails)
def coinflip():
    if random.randint(0, 1) == 0:
        return 'heads'
    else:
        return 'tails'
# to make this unfair you would use the following function if you used the 
# function as unfair_coin_flip(.7) it would have a 70% chance of returning tails
# which if you run it cuts the ration from around 1.0 to around .40!
def unfair_coin_flip(probability_of_tails):
    if random.random() < probability_of_tails:
        return "tails"
    else:
        return "heads"

# flip a coin 9_999 times track heads or tails then divided them round 
# it to two decimal places and print the ratio of heads to tails.
heads,tails = (0,0)
for i in range(10_000):
    if coinflip() == 'heads':
        heads += 1
    else:
        tails += 1
ratio = round(heads/tails,2)
print (ratio)

