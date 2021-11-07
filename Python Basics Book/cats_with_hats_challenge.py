cats = []
cats_with_hats = []
# walk around the circle 100 time
for round in range(1,101):
    #current round at 0 becuase list is 0-99
    current_round= 0
    # stop at each cat
    while current_round <= 100:
        #when the loop starts it will be empty so to have to append the first round
        try:
            #if you go to a cat and it does have a hat then put one on
            if cats[current_round] == False:
                    cats[current_round] = True
            #if it has a hat then take it off
            else:
                cats[current_round] = False
        except IndexError:
                cats.append(True)
        #adding rounds to the current to satisfy challenge increment
        current_round += round

#loop through cats and store the ones that have a hat on in a list and print the list
for i in range(len(cats)):
    if cats[i] == True:
        cats_with_hats.append(i)

print(f'These cats have hats! {cats_with_hats}')


# solution is good and more efficent then my approch 
# number_of_cats = 100
# cats_with_hats = []
# number_of_laps = 100

# # We want the laps to be from 1 to 100 instead of 0 to 99
# for lap in range(1, number_of_laps + 1):
#     for cat in range(1, number_of_cats + 1):

#         # Only look at cats that are divisible by the lap
#         if cat % lap == 0:
#             if cat in cats_with_hats:
#                 cats_with_hats.remove(cat)
#             else:
#                 cats_with_hats.append(cat)

# print(cats_with_hats)