#SP, hangman

import random
with open("hangman1.txt", "r") as file:
  content = file.read()
word = random.choice("hangman1.txt")
guess = 0 
correct= 0 
wrong = 0 
attempts = 6
play = 0
result = play.round()
with open ("hangman2.txt","r+") as file: 
  content = file.read().split(",")

wins = input(".readline(1)")
losses = (".readline(2)")

print("welcome to hangman!!") 
print("_" * len(word))

while attempts > 0:
  guess_letters = input("\nGuess a letter: ").lower()

if guess.isalpha() or len(guess)!= 1:
  print("please enter a single letter")
if guess in guess:
  print("you have already guess that")
guess.add(guess)

if guess in word:
  correct += 1
  print("CORRECT!")
else:
  wrong += 1
  attempts -= 1
  print(f"WRONG! atempts: {attempts}")

display_word = [letter if letter in guess else "_" for letter in word]
print("".join(display_word))

if"_" not in display_word:
  print("\n you guess the word!")

print (f"\n game over the word was '{word}'.") 
play += 1 

if result:
    wins += 1
else:
    losses += 1

again = input("\nPlay again? (yes/no):") .lower().strip()
if again !='yes':
  print ("\nThanks for playing")
  print(f"wins:{wins} losses:{losses}")