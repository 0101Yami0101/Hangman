import random
from hangman_words import word_list
from hangman_art import stages


chosen_word = random.choice(word_list) #choosing random word from word_list 
word_length = len(chosen_word)

end_of_game = False   #To end the while loop #gameover condition TRUE if  out of lives or game won
lives = 6


from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks in a list according to number of letters in the chosen word
display = []
for _ in range(word_length):
    display += "_"

# condition to run the primary game loop,, While loop
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    #When guessed letter is same as previously guessed letters 
    if guess in display:
        print(f"You've already guessed {guess}")

    #Check guessed letter. If the guess is in chosen_word, The guess will appear in the same position in display
    for position in range(word_length):
        letter = chosen_word[position] #get each letter of the chosen_word with the for loop
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.#lose condition
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(f"You have {lives} lives left")
        if lives == 0:
            end_of_game = True #Escaping game loop
            print(f"The word was {chosen_word}..You lose.")

    print(f"{' '.join(display)}")

    #Win condition
    if "_" not in display:
        end_of_game = True #Escaping game loop
        print(f"The word was {chosen_word}.. You win.")

    print(stages[lives])
