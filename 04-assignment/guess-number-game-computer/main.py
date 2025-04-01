import random # importing random for generating a random number

def computer_guess(x):
    low = 1 # lowest guess
    high = x # highest guess
    feedback = '' #user feedback default empty 
    attempts = 0  # Counter to track number of guesses

    print(f"\nThink of a number between {low} and {high} and let the computer guess it!\n")

    while feedback != 'c': # if feedback is equal to c "means correct"
        attempts += 1  # increase attempts in each loop
        if low != high: # low is not equal to high 
            guess = random.randint(low, high) # generating a number
        else:
            guess = low  #  low == high  means that the value of low or high is same

       
        try: # if there is any error than execute except 
            feedback = input(f"If the guess  {guess} is too high (H), too low (L), or correct (C)? ").strip().lower() # get input from user(feedback)
            
            if feedback not in ['h', 'l', 'c']: #if feedback is not in h,l,c 
                raise ValueError("Invalid input! Please enter 'H', 'L', or 'C'.") #printing error
            
          
            if feedback == 'h':  
                high = guess - 1  # Adjust the range
            elif feedback == 'l':
                low = guess + 1  # Adjust the range
            elif feedback == 'c':
                break  # Exit loop if correct

            else:  # If feedback is invalid
                attempts -= 1  # Don't count invalid attempts
          
            


        except ValueError as e: # if the  try get any error than except will be executed
            print(e)  # show error
            attempts -= 1  # don't count invalid attempts

    print(f'\n Wow! The computer guessed your number, {guess}, correctly in {attempts} attempts!')

# Call the function with an upper limit
computer_guess(15)
