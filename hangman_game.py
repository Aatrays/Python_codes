import random
# custom modules
from hangman_art import stages, logo
from hangman_word import word_list

print(logo)

print("Enter a letter to start the game!")
print("If letter in the word then guess the next letter.")
print("If letter is not in word you lose lives and your hangman dies")


#word_list = ["aardvark","baboon","camel"] - We are using the module name hangman_word instead of manual list.

#1. Randomly choose a word from the word_list.
#For each letter in the chosen_word, add a "_" to 'display'.a
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#print(f"The chosen word in {chosen_word}")

display = []
# the append function will replace "_" to each letter.
for x in chosen_word:
  x == display.append("_") # or display += "_"
#print(display)

lives = 6

end_of_game = False

while not end_of_game:
  if "_" not in display:
    end_of_game = True
    print("You win")

  #2. Ask the user to guess a letter
  guess = input("Guess a letter: ").lower()

  # if user guessed the same letter
  if guess in display:
    print(f"You have already guessed {guess}")

  # letter == guess will hold each aplhabet from the word.
  # 3. check the letter the user guessed is in the word.

  for letter in range(0, word_length):
    position = chosen_word[letter]
    #print(f"Current position: {letter}\n Current letter: {position}\n Guessed letter: {guess}")
    if position == guess:
      display[letter] = position
  
  if guess not in chosen_word:
    print(f"You guessed {guess}, that's not in the word. You lose a life")
    lives -= 1
    if lives == 0:
      end_of_game = True
      print("You Lose.")
  
  print(f"{' '.join(display)}")

  print(stages[lives])
      

  #print(display)

  # if "_" not in display:
  #   end_of_game = True
  #   print("You win")
