from random import choice

# First, fill out the following dictionary with the remaining states and
# their associated capitals in a file called capitals.py 
capital_dic={
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona':'Phoenix',
    'Arkansas':'Little Rock',
    'California': 'Sacramento',
    'Colorado':'Denver',
    'Connecticut':'Hartford',
    'Delaware':'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
    'Hawaii': 'Honolulu',
    'Idaho': 'Boise',
    'Illinios': 'Springfield',
    'Indiana': 'Indianapolis',
    'Iowa': 'Des Monies',
    'Kansas': 'Topeka',
    'Kentucky': 'Frankfort',
    'Louisiana': 'Baton Rouge',
    'Maine': 'Augusta',
    'Maryland': 'Annapolis',
    'Massachusetts': 'Boston',
    'Michigan': 'Lansing',
    'Minnesota': 'St. Paul',
    'Mississippi': 'Jackson',
    'Missouri': 'Jefferson City',
    'Montana': 'Helena',
    'Nebraska': 'Lincoln',
    'Neveda': 'Carson City',
    'New Hampshire': 'Concord',
    'New Jersey': 'Trenton',
    'New Mexico': 'Santa Fe',
    'New York': 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck',
    'Ohio': 'Columbus',
    'Oklahoma': 'Oklahoma City',
    'Oregon': 'Salem',
    'Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence',
    'South Carolina': 'Columbia',
    'South Dakoda': 'Pierre',
    'Tennessee': 'Nashville',
    'Texas': 'Austin',
    'Utah': 'Salt Lake City',
    'Vermont': 'Montpelier',
    'Virginia': 'Richmond',
    'Washington': 'Olympia',
    'West Virginia': 'Charleston',
    'Wisconsin': 'Madison',
    'Wyoming': 'Cheyenne'  
}

# Next, pick a random state name from the dictionary and assign both
# the state and its capital to two variables. You’ll need to import the
# random module at the top of your program.

state,capital = choice(list(capital_dic.items()))

# Then display the name of the state to the user and ask them to enter
# the capital. If the user answers incorrectly, then repeatedly ask them
# for the capital until they either enter the correct answer or type "exit" .

guess = input(f"\nWhat is the capital of {state}: ").upper()

while guess != capital.upper() and guess != 'EXIT':
    guess = input(f"\nPlease try capital of {state} again: ").upper()

# If the user answers correctly, then display "Correct" and end the pro-
# gram. However, if the user exits without guessing correctly, display
# the correct answer and the word "Goodbye" .
if guess == capital.upper():
    print('Correct')
else:
    print('Goodbye')