# Number Guessing Game

# Create a program where the computer randomly selects a number between 1–100.
# The user must guess it. After each guess, show “Too high”, “Too low”, or “Correct”.
# Count total attempts.


# ...existing code...
import random

def num_guess(max_attempts=5):
    rand_num = random.randint(1, 100)
    attempts_left = max_attempts
    while attempts_left > 0:
        try:
            user_num = int(input("Guess a number (1-100): "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        if user_num == rand_num:
            print("Correct! You guessed the number.")
            return True
        if user_num < rand_num:
            print("Too low")
        else:
            print("Too high")

        attempts_left -= 1
        if attempts_left:
            print(f"\nTry again, {attempts_left} attempts left")
            print("=========================")

    print("\nOut of attempts. The number was:", rand_num)
    return False

if __name__ == "__main__":
    print("=========================")
    print("#--Number Guessing Game--#")
    print("=========================")

    while True:
        num_guess()
        ask = input("\nDo you want to play again? (y/n): ").strip().lower()
        if ask != "y":
            print("Quitting...")
            break
# ...existing code...