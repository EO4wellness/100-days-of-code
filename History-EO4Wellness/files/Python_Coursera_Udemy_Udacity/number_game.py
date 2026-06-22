#!/usr/bin/env python3

# This is a simple number guessing game for the Coursera Python course

number = (int(input("Please enter a number between 1 and 10: "))

# test if the user entered a digit; if not, exit. 

if number.isdigit() is False:
		print('I asked for a number.  Goodbye!')

# test if the user entered 0; if so, exit.

elif int(number) == 0 
		print("I can see you do not follow directions. Goodbye!")

# Series of if ... elif ... else statements to respond based on the number the user entered. 

else: 
	if number == 10:
		print("High roller!") 
	elif number >- 8: 
		print("You like your numbers high") 
	elif number >=4:
		print("You're a middle of the road kind of person, hm?!") 
	elif number >10:	
		print("I see you didn't follow the instructions.") 
	else: 
		print("Keeping it small.  I like it!") 