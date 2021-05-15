import random
from hangman_art import stages, logo
from hangman_words import word_list as list

word_list = list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

game_over = False
lives = 6

print(logo)
# print(f"The solution is {chosen_word}")

display = []

for letter in chosen_word:
    display += "_"

while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed that letter")

    for position in range(word_length):
        letter = chosen_word[position]

        if guess == letter:
            display[position] = letter

    if guess not in chosen_word:
     
        print(f"guess not in the word you lost a life ")

        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose...")

    #Join all the elements in the list and turn it into a String
    if lives > 0:
        print(f"{' '.join(display)}")

    #Check if user has got all letters
    if "_" not in display:
        game_over = True
        print("You win!!!")

print(stages[lives])
