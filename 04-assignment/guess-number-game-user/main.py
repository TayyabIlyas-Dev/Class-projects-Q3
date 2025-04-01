# for stylish ui in browser
# import random
# import streamlit as st

# def guess_the_number():
#     st.title("🎯 Guess the Number Game")
    
#     if 'number' not in st.session_state:
#         st.session_state.number = random.randint(1, 10)
#         st.session_state.attempts = 0
    
#     guess = st.number_input("Guess a number (1-10):", min_value=1, max_value=10, step=1)
#     if st.button("Submit Guess"):
#         st.session_state.attempts += 1
        
#         if guess < st.session_state.number:
#             st.warning("Too low! Try again.")
#         elif guess > st.session_state.number:
#             st.warning("Too high! Try again.")
#         else:
#             st.success(f"🎉 You got it in {st.session_state.attempts} tries!")
#             st.session_state.number = random.randint(1, 10)
#             st.session_state.attempts = 0

# if __name__ == "__main__":
#     guess_the_number()






# for console

import random # importing random for generating a random number

def guess_the_number(): 
    print("Welcome to the  number guessing game!") # welcome message to the user 
    lower_bound = 1 # this is the lowest guess
    upper_bound = 10 # this is the highest guess 
    secret_number = random.randint(lower_bound, upper_bound) # generate a random number and saves it in the  variable secret_number
    attempts = 0 # default attempts should be 0
    guess = 0 # default guess should be is 0
    
    while guess != secret_number: # if user guess is not equal to secret_number
        try: # if there is any error than execute except 
            guess = int(input(f"Guess a number between {lower_bound} and {upper_bound} : ")) # get input (guess) from user 
            attempts += 1 # increase the number of attempts every time the loop is executed
            
            if guess < lower_bound or guess > upper_bound: # if use guess is less than lower_bound or  if the user guess is greater than upper_bound 
                print("Out of bounds! Try again.")
                continue # if the condition is true then loop will  start again  
            
            if guess < secret_number:# if user guess is lower than secret_number
                print("Too low! Try again.")
            elif guess > secret_number: # if user guess is greater than secret_number
                print("Too high! Try again.")
            else: 
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break # loop  will be stopped
        except ValueError: # if the  try get any error than except will be executed
            print("Invalid input! Please enter a valid number.")





guess_the_number() 
