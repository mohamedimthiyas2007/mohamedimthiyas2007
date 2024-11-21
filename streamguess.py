import streamlit as st
import random

# Initialize variables
lowest_number = 1
highest_number = 25
answer = random.randint(lowest_number, highest_number)

# Streamlit app title and instructions
st.title("Python Guessing Game")
st.write(f"Select a number between {lowest_number} and {highest_number}")

# Session state to keep track of guesses and number of attempts
if 'guesses' not in st.session_state:
    st.session_state.guesses = 0
if 'running' not in st.session_state:
    st.session_state.running = True

# Input box for guessing
guess = st.number_input("Enter your guess:", min_value=lowest_number, max_value=highest_number, step=1)

# Check if the guess is valid and update game state
if guess:
    if guess < lowest_number or guess > highest_number:
        st.warning(f"The number is out of range. Select a number between {lowest_number} and {highest_number}.")
    else:
        st.session_state.guesses += 1
        if guess < answer:
            st.write("Very low! Try again.")
        elif guess > answer:
            st.write("Very high! Try again.")
        else:
            st.success(f"Correct! The answer was {answer}.")
            st.write(f"You guessed it in {st.session_state.guesses} attempts.")
            st.session_state.running = False

# If the game is over, reset the game state
if not st.session_state.running:
    if st.button('Play Again'):
        st.session_state.guesses = 0
        st.session_state.running = True
        answer = random.randint(lowest_number, highest_number)
        st.write(f"Game reset. Select a new number between {lowest_number} and {highest_number}.")


