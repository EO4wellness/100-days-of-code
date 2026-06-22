#!/usr/bin/env python3

# this code is an example of testing user input

# type gedit myscript.py in command prompt to test/run this file 


print('Welcome to the age calculator.')
answer = input('Would you like to know how old you will be in a particular year? (y/n)')

while not (answer == 'y' or answer == 'n'):
    print("The value of answer is", answer)
    print("I'm sorry, I didn't understand. Please try again.")
    answer = input('Would you like to know how old you will be in a particular year? (y/n)')

if answer == 'n':
    print("I'm sorry you're not interested. Goodbye!")
else:
    year = input('What year were you born?')
    month = input('In what month were you born?')
    day = input('On what day?')
    
    futureYear = input('What year did you want to know about?')
    futureMonth = input('What month did you want to know about?')
    futureDay = input('What day?')

    age = int(future) - int(year)

    print('In the year ', future, 'you will be ', age, ' years old.')
    print('Goodbye!')