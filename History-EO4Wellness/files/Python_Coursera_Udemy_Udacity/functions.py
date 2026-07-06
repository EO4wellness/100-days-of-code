# Functions are BLOCKS of CODE which are meant to be REUSED
# Python allows us to write our own functions.  

# To CREATE a functio we use this SYNTAX: 

def function(agruments): 
        statements 
        

# Example: 

# Function to prompt user. 
# If user answers no, if this is the first time
# the user plays, deliver one message.
# if the user has already played a round
# deliver a different message.
# in ither case, set gameOver to True. 

def play(prompt, gameOver):
    # String used to build prompt.
    text = "Would you likke to analyze {} number? (y/n)"
    
    # If first round use "a" 
    # For additional rounds use "another" 
    if prompt ==1: 
        det = "a"
    else:
        det = "another" 
    
    # Prompt user for choice using formatted text variable.
    answer = input(text.format(det))
    
    # While loop to process user input.
    # Loop will exectue unless the user enters
    # "y", "Y", "n", or "N" 
    while not (answer.lower() == "y" or answer.lower() == "n"):
        print("I'm sorry, I didn't understand.  Please try again")
        print("")
        answer = input(text.format(det))
        
    # if Statement to handle "n" response.
    if answer.lower() == "n":
        # Set gameOver variable to True
        gameOver = True 
        
        # If the first round, print one message.
        # If not the first round, print a different message. 
        if prompt == 1:
            print("That's too bad, we could have had fun.")
            print("")
            
        else: 
            print("No worries. Thank you for playing!")
            print("")
            
    # Else to process "y" response.
    # Increment prompt to indicate another round has started.
    else: 
        prompt += 1
        
    # Return statment returns the (new) values of prompt and gameOver
    return prompt, gameOver
    
# Function to ask the user for a number.
def getNumber():
    #Valid variable to test user input.
    # Starts as False.
    valid = False 
    
    # While loop to get and process input.
    while valid is False: 
        
        # Ask use to enter a number 
        numberInput = input("Please enter a number between 1 and 10: ") 
        
        # If the user enters non-numberic response return message an dmove to the next iteration 
        
        if numberI(nput.isdigit() is not True: 
            print("I am storry, I need a number")
            print('')
            continue 
            
        # If the user entered a numeric response below 1 or above 10, 
        # print message and move on to the next iteration
        elif in(numberInput) == ) or int(numberInput) > 10:
            print ("I'm sorry, your number must be between 1 and 10.")
            print ("")
            continue
    # Return the numbe3r to the main app
    return numberInput
    
# Function to process the number. 
def processNumber(number): 
    
    # Change the string to an integer
    number = int(number)
    
    # if ... elif  ... else statement
    # prints message according to number value
    if number == 10: 
        print("High Roller!")
    elif number >= 8:
        print("You like your numbers high!")
    elif number >= 4:    
        print("A middle of the road person, hm?")
    else:     
        print("Keeping it small.  I like it!") 
    
    print("")
    print(""    
    
# Main application begins
# Statements to initialized the three variables
prompt = 1 
GameOver = False 
number = ''

# WHile loop continues game play
@ As long as the user does not answer "n" 
# when asked to play a game
while gameOver is False:
    
    # Call the play function with the prompt, gameOver variables
    # store the updated values in the original variables
    prompt, gameOver = play(prompt, gameOver)
    
    # If the user said "n" break the loop which ends the game 
    if gameOver is True: 
        break 
    
    # if the user did not say no, call the getNumber() function
    # store the results in the number variable
    number = getNumber()
    
    # Then call the processNumber function
    #sending the number as the argument
    processNumber(number)
    
    
# Functions must always be DEFINED before they can be CALLED
# It is the BEST practice to define ALL funcitons at the TOP of the script. 
# Test functions are working before "lego" blocking them into the program.     

# When calling a function (example the function of play(), you have to provide the arguments in the order they are listed
#  Exception?  You can name the variables in the calling statement of your function
# Example: correct order
play(prompt, gameOver)
# Example variables in the statement but the arguments are out of order) 
play(gameOver = gameOver, prompt = prompt) #this technically works but it is not best practice
    