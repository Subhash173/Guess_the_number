
import random

while True:
    print("\nWelcome to the number guessing game!")
    print("Guess the number between 1 and 100.")
    print("You have only 5 attemps to guess. Good luck!")

    number = random.randint(1, 100)

    attempts = 5

    while True:
        guess = int(input("\nEnter the number: "))
        attempts -= 1
        print("Attempts left",attempts,".")

        if attempts == 0:
            print("The correct number is ",number,".")
            print("\n----------Game Over----------")
            break
        

        if guess > number:
            print("Too high, try again.")

        elif guess < number:
            print("Too low, try again.")
        else:
            print(f"\nCongrats! You have guessed the number {number} in {attempts} attempts!")
            break

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again == "yes":
        print("")

    else:
        print("\nThanks for playing.")
        break

    