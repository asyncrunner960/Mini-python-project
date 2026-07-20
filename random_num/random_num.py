from random import randint

num_random = randint(1, 100)
attempts = 0

print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        num_user = int(input("Enter your guess: "))
        attempts += 1
    except ValueError:
        print("Please enter a valid number.")
        continue

    if num_user > 100 or num_user < 1:
        print("Please enter a number between 1 and 100.")
    elif num_user < num_random:
        print("Too low, try again.")
    elif num_user > num_random:
        print("Too high, try again.")
    else:
        print(f"You guessed it! Congratulations! It took you {attempts} attempts.")
        print("Do you want to play again?")
        answer = input("(print <<yes>> to continue): ")
        if answer.lower() == "yes":
            print("I'm thinking of a number between 1 and 100.")
            num_random = randint(1, 100)
            attempts = 0
            continue
        
        print("Bye!")
        break
    