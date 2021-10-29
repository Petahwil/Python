# def eletter():
#     guess = input("\nEnter a letter or word:")
#     guess = guess.upper()
#     return guess;

# def game(word, guess):
#     guess_letter = guess
#     result =False
#     while rounds > 0:
#         word = word
#         failed = 0
#         for char in word:
#             if char in guess_letter:
#                 print(char, end="")
#             else:
#                 print("_", end="")
#                 failed += 1
#         if (failed == 1) or (guess == word):
#             print("\nYou Win!")
#             result = True
#             return result
#         if len(guess) == 1:
#             guess_letter += guess
#             rounds -= 1
#             if guess_letter.count(guess) > 1:
#                 print("\nYou've already guessed that letter!")
#             if guess not in word:
#                 guess_letter = "".join(set(guess_letter))
#                 print("\nYour guess so far: " + guess_letter)
#             if rounds == 0:
#                 print("\nYou lose! The word was " + word)
#                 return result
#     return result

# def main():
#     round = 6
#     word_list = ['APPLE', 'OBVIOUS', 'XYLOPHONE']
#     word_index = 0
#     win = 0
#     while word_index < 3:
#         if game(word_list, word_index) is True:
#             win += 1
#         word_index += 1
#     print("You won " + str(win) + " out of 3")

# main()


    
def check_letter(word, guess, guess_letter, current_round):
    guessed_char = ""
    add_round = 0
    for char in word:
        if char in guess_letter:
            print(char, end="")
            guessed_char += char
        else:
            print("_", end="")
    if (guessed_char == word):
        print("\nYou Win! The word was " + word)
        return 6
    if guess_letter.count(guess) > 1:
        add_round -= 1
        print("\nYou've already guessed that letter!")
    if guess not in word:
        add_round += 1
        current_round += 1
        guess_letter = "".join(set(guess_letter))
        print("\nYour guess so far: " + guess_letter)
    if current_round == 6:
        print("\nYou lose! The word was " + word)
        return 1
    return add_round 


    
def main2():
    word_list = ['APPLE', 'BUTTHOLE', 'BEEFYBOI']
    total_round = 0
    add_guess = ''
    while total_round < len(word_list):
        current_round = 0
        guess_letter = ""
        while current_round < 6:
            guess = input("\nEnter a letter or word:").upper()
            if len(guess) == 1:
                guess_letter += guess
            did_you_win = check_letter(word_list[total_round] ,guess, guess_letter, current_round)
            if did_you_win == 6:
                current_round = 6
            if did_you_win == 1:
                current_round += 1
            print(f'\nYou have {6 - current_round} wrong guesses left')
            print(f'\n_____________________________')
        # print(total_round)
        total_round +=1

main2()