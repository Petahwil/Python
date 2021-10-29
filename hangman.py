
def check_letter(word, guess, guess_letter, current_round):
    guessed_char = ""
    #add round is set up to notify main if the user guesses wrong add a round to current round
    add_round = 0
    # check if guess is in the word
    for char in word:
        #looking through the guessed letters to put word together
        if char in guess_letter:
            print(char, end="")
            # add the chars found to this string so we can use it through the funtion
            guessed_char += char
        #if it is not found then put a blank in
        else:
            print("_", end="")
    # If the guessed char makes up the word return 6 signal win
    if (guessed_char == word):
        print("\nYou Win! The word was " + word)
        return 6
    #had to add minus roung becuase this runs ever time the next if runs and you dont want to add a round here
    if guess_letter.count(guess) > 1:
        add_round -= 1
        print("\nYou've already guessed that letter!")
    #if they guess a letter wrong add a round and print out what they have guessed
    if guess not in word:
        add_round += 1
        guess_letter = "".join(set(guess_letter))
        print("\nYour guess so far: " + guess_letter)
    #if the user guesses wrong 6 times they lose return one to tell they
    if current_round == 6:
        print("\nYou lose! The word was " + word)
        return 1
    # return round to add one if the user is wrong otherwise it will add 0
    return add_round 


    
def main():
    word_list = ['APPLE', 'BUTTHOLE', 'BEEFYBOI']
    total_round = 0
    add_guess = ''
    #while there are words not used yet in the array keep playing game
    while total_round < len(word_list):
        #resetting current round and the letters user guesses inbetween rounds
        current_round = 0
        guess_letter = ""
        #loop for the game the user is currently playing
        print(f'\nStart Hangman!')
        while current_round < 6:
            #prompt the user for there guess
            guess = input("\nEnter a letter or word:").upper()
            # if the guess is in the right format then continue the game if not have them re-enter
            if len(guess) == 1:
                #add all the letters guessed to str
                guess_letter += guess
                #running funtion to check the letter that was guessed
                did_you_win = check_letter(word_list[total_round] ,guess, guess_letter, current_round)
                # return 6 user wins return 1 user guessed wrong add a round
                if did_you_win == 6:
                    current_round = 6
                if did_you_win == 1:
                    current_round += 1
            # if user guesses word then they win otherwise entry invalid
            if guess == word_list[total_round]:
                print("\nYou Win! The word was " + word_list[total_round])
                current_round = 6
            else:
                print(f'\nYou entry was invalid')
            print(f'\nYou have {6 - current_round} wrong guesses left')
            print(f'\n_____________________________')
        total_round +=1

main()