#Python
# You can use an else: branch in loops. 
# In a while loop, an else: branch exectues once the condition becomes False. 
# In a for loop, the else: branch executes hen the loop is finished iterating. 

# Example: 

# Ask the user a question: 
answer = input('Would you like to play a game? (y/n) ')

# While loop to test for valid input: 
while not (answer == "y" or answer == "n"): 
	print("I'm sorry, I didn't understand.  Pleease try again answering y or n.")
	anser = input("Would you like tplay a game? (y/n) ")
	
# Else: Executes when condition ends. 
else: 
	print ("Thank you for following directions.") 
	
	
# Now let's look at a FOR loop: 

# Loop for range(5)
for i in range(5):
        print(i)
        
# Else: print a message that the loop is completed. 
else: 
        print("All done!")
        
# Note if you run the above for I code--it will output 0, 1, 2, 3, 4, All done! 

#The break statement terminates the loop and executes the very next statement.

# Initialize the counter.
counter = 1 

# Ask the user for the password.
pwd = input("Please enter your password:  ")

# Start while loop to test if the password is valid.
# If the user types it right the first time?) 
# Loop never exectues. 

while pwd !="password": 
    print("I'm sorry, that's incorrect.") 
    # Test to see if there have been three wrong passwords. 
    # If so, exit the loop. 
    if counter == 3: 
        print("You are limited to three incorrect attempt.") 
        break 
    pwd = input("Please enter your password: ") 
    counter +=1
# Tests to see if password was typed correctly.
# If so, contratulate the user. 
if counter < 3:
    print("You have been authenticated.") 
print("Goodbye!")     

# Ask the user for some numbers
answer = input("Please put in some numbers :")

#Create the even variable and set it to zero.
even = ) 

# for loop to iterate thorugh the values 
for i in answer: 
    
    # if the modulo of the mnumber divided by 2
    # is not 0, then number is odd. 
    # in that case, move on to the next number. 
    
        if int(i) % 2 !=):
            continue 
# if the number wasn't odd, add one to even. 
        event += 1
# print the results.
print("There were",  even, "even numbers. " )
        
# Pass does nothing.  It can therefore be used as a placeholder until you write the actual statements. 
# Example:  you know you will need a loop for the item you are scripting.  HOwever, you've not written it yet.  You could do this: 

# Pass as a placeholder, loop needs to still be written

for i in range(5):
    pass 
else: 
    print("Finish!") 
    
    

 