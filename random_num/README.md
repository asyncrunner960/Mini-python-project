# Guess the Number

A simple command-line game where the player tries to guess a randomly generated number between 1 and 100. Built with Python.

## How It Works

The program generates a random integer from 1 to 100. The player enters guesses, and the program provides feedback ("Too low" or "Too high") until the correct number is found. At the end, the player can choose to play again or exit.

## Features

- Random number generation for a unique game each time
- Input validation that prevents crashes on non-integer input
- Range checking with a clear message if the guess is outside 1–100
- Attempt counter to track performance
- Full replay loop so the game can be restarted without relaunching the script

## How to Run

1. Make sure you have Python 3 installed
2. Download `random_num.py`
3. Open terminal and run:
```
 python random_num.py
```

4. Follow the prompts to guess the number

## Example
```
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too high, try again.
Enter your guess: 25
Too low, try again.
Enter your guess: 37
You guessed it! Congratulations! It took you 3 attempts.
Do you want to play again?
(print <<yes>> to continue): yes
I'm thinking of a number between 1 and 100.
```

## What I Learned

- Generating random integers with the `random` module
- Building a game loop with `while True` and `break`
- Handling invalid user input gracefully with `try/except` and `continue`
- Validating numeric ranges for a better user experience
- Structuring a replayable interactive program

## Tech

Python 3, `random` module
