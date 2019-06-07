import random
import re

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

word = random_word
current_guesses = []

first_letter_choice = input("Please enter one letter: ").lower()

if len(first_letter_choice) == 1:
    current_guesses.append(first_letter_choice)

while len(first_letter_choice) != 1:
    print("Invalid entry - please try again.  Remember to type only one letter with each guess.")
    first_letter_choice = input("Please enter one letter: ").lower()













