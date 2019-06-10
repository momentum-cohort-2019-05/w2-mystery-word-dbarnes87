import random
import re

def main():

    f = open("words.txt")
    word_list = (f.read()).lower()
    split_word_list = word_list.split()

    # print(random.choice(split_word_list))

    easy_words = []
    normal_words = []
    hard_words = []

    for word in split_word_list:
        if len(word) > 4 and len(word) <= 6:
            easy_words.append(word)
        elif len(word) >= 6 and len(word) <= 8:
            normal_words.append(word)
        elif len(word) >= 8:
            hard_words.append(word)

    # print(normal_words)

    user_choice = input("Which mode would you like to play on: easy, normal, or hard? ")

    user_choice_lower_case = user_choice.lower()

    # while user_choice != "easy" or "normal" or "hard":
    while user_choice_lower_case not in ["easy", "normal", "hard"]:
        print("Invalid Entry.  Please check your spelling and try again")
        user_choice = input("Which mode would you like to play on: easy, normal, or hard? ")

    user_choice_lower_case = user_choice.lower()


    if user_choice_lower_case == "easy":
        random_word = random.choice(easy_words)
        print ("This words is", len(random_word), "characters long.")
    elif user_choice_lower_case == "normal":
        random_word = random.choice(normal_words)
        print ("This word is", len(random_word), "characters long.")
    elif user_choice_lower_case == "hard":
        random_word = random.choice(hard_words)
        print ("This word is", len(random_word),  "characters long.")
    # elif user_choice_lower_case != "easy" or "normal" or "hard":
    #     print ("Please check your spelling and try again.")

    print("You have 8 lives remaining.")
    word = random_word
    current_guesses = [] 
    print(word)
    word_match = word.replace("", " ")
    word_match = word_match.strip()
    print(word_match)

    def display_letter(letter, guesses):
        if letter in guesses:
            return letter
        else:
            return "_"
        [display_letter(letter, current_guesses)
        for letter in word]

    def print_word(word, guesses):
        output_letters = [display_letter(letter, guesses) 
                        for letter in word]
        return (" ".join(output_letters))
    

    # def play_again(play_again_choice):

    guess_counter = 8

    guess = input("Please enter one letter: ").lower()


    wordGuessed = False

    while guess_counter > 1 and wordGuessed is False:

        if len(guess) != 1 and guess_counter > 0:
            print("Invalid entry - please try again.  Remember to type only one letter with each guess.")
            guess = input("Please enter one letter: ").lower()
                
        if guess not in word and len(guess) == 1:
            current_guesses.append(guess)
            guess_counter -= 1
            print("Sorry, that letter is incorrect.  Please guess again.")
            print("Lives remaining: ", guess_counter)
            print("Current guesses: ", current_guesses)   
            print(print_word(word, current_guesses))
            # print("Current guesses: ", current_guesses)
                
        if guess in word:
            current_guesses.append(guess)
            print("Good job.  Please guess again.")
            print("Lives remaining: ", guess_counter)
            print("Current guesses: ", current_guesses)
            print(print_word(word, current_guesses))

        if word_match ==  print_word(word, current_guesses):
            wordGuessed is True
            print("Congratulations - you won!")
            break        
        
        print_word(word, current_guesses)
        guess = input("Please enter one letter: ").lower()
            # print("Lives remaining: ", guess_counter)

        if guess in current_guesses:
            # guess_counter += 1
            print("Duplicate guess - please guess again!")
                # print("Lives remaining: ", guess_counter)
            print("Current guesses: ", current_guesses)


        

    if guess_counter <= 1:
        current_guesses.append(guess)
        print(current_guesses)
        print("Sorry - you have no lives remaining.  GAME OVER!")
        print(f"Your word was", word)

            
        # print_word(word, current_guesses)

        # input("Would you like to play again - yes or no? ")
    play_again_choice = input("Would you like to play again - yes or no? ")
    if play_again_choice == "yes":
        main()



    # play_again("yes")

if __name__ == '__main__':
    main()
    # if play_again_choice == "yes":
    #     play_again
    # else:
    #     print("Okay - have a nice day!")




    # if play_again_choice == "yes":
    #     play_again
    # else:
    #     print("Okay - have a nice day!")






# print_word(word, current_guesses)

# if output_letters = word:
#     print(word)




# if guess not in word:
#     current_guesses.append(guess)
#     guess = input("Please enter one letter: ").lower()
#     print("Sorry, that letter is incorrect.  Please guess again.")
    


# print_word(word, current_guesses)

# input("Please enter another letter: ").lower()

# another_letter_choice = input("Please enter another letter: ").lower()

# if another_letter_choice not in word:
#     print("Sorry, that letter is incorrect.  Please guess again.")
#     another_letter_choice = input("Please enter another letter: ").lower()

# [display_letter(letter, current_guesses)
#  for letter in word]

    













