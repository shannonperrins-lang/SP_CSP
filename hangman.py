#SP, hangman

#create a list of 10 words on a sperate txt of file

#create another file holds win/loos counts 0,0

# read your files use spilt (",") on the content of the words txt docu,ent to create your list of words 

#pull win and lose totals from the other txt file and save them as 2 separate veriables 

# save the correct word as a veribile use this code random.choice(name of the list)
#number of wrong guesses
#what letters have been guessed 
#funtion to difplay hangman (needs number of wrong guesses)

#    ___
#   |  |
#   |  O
#   | /|\
#   | / \
#   |______

#funtion to show the letters and spaces (the correct word, letters that have been guessed)
#loop over the corect word
#varible for display word (starts as an empty string)
#check if letter has been guess
#if they havent guessed it the letter
# add an underscore to the display word
#return the finished display word (outside of the loop)

#main game loop (while true)
#call funtion to show hangman
# print funtion call to show display word create variable and ask user to guess a letter
#add the letter to list of guessed letters
# check if not letter in word: (line of code)
#increase incorrect guesses
#check if display word is same as the word
#tell user if they won
#increase win total
#ask if they want to play again
#reset random word, rest wrong guess count 
#check to see if they lost 
#tell them what the word was
#increase the lost count 
# ask if they want to play again