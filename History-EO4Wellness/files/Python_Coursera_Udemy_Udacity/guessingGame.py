#!/usr/bin/env python3
# to run this game, open a terminal prompt and type 
# gedit guessingGame.py 

word = input('Please enter a word for your opponent: ')

# we need to initialize a number of variables 
# keep track of the wrong number of guesses

wrongGuesses = 7 
guessed = False
correctLetters = ''
wrongLetters = ''
blanks = ''

for letter in word:
    blanks = blanks+ '_ '
    
print(blanks)

print('You have', wrongGuesses, 'wrong guesses left.') 

while guessed is False and wrongGuesses > 0: 
    
    print('Correct Letters Guessed: ', correctLetters)
    print('Wrong Letters Guessed: ', wrongLetters) 
    
    guess = input("What letter would you like to guess? ') 
    
    blanks = ''
    validLetter = False 
    
    