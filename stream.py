import streamlit as st
import random

lowest_number=1
highest_number=100
answer=random.randint(lowest_number,highest_number)

guesses=0
running=True

print("python guessing game :")
print(f"select a number between {lowest_number} and {highest_number}")

while running:
    guess=input("enter your guess :")
    
    if guess.isdigit():
        guess=int(guess)
        guesses+=1

        if guess <lowest_number or guess > highest_number:
            print("the number is an out of range")
            print(f"select a number between {lowest_number} and {highest_number}")
            
        elif guess<answer:
            print("very low try again")
        elif guess>answer:
            print("very high try again")
        else:
            print(f"correct the answer was {answer}")
            print(f"number of guesses {guesses}")
            running=False
            
        
    else:
        print("invalid guess")
        print(f"select a number between {lowest_number} and {highest_number}")
        

