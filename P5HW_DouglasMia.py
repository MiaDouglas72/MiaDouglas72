# Mia Douglas
# 04/04/2024
# P5HW
# Write a program that gives simple math quizes

import random
#menu options
def display_menu():
    print("Welcome to Math Quiz")
    print("MAIN MENU")
    print("1. Addition Random Numbers")
    print("2. Subtract Random Numbers")
    print("3. Exit")
#addition problems
def add_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 + num2
    print(f"{num1} + {num2}")
    guesses = 0
    while True:
        answer = int(input("Enter your answer: "))
        guesses += 1
        if answer == result:
            print(f"Congratulations! Your answer is correct. Number of guesses: {guesses}")
            break
        elif answer < result:
            print("Sorry, guess is too low. Try again.")
        else:
            print("Sorry, guess is too high. Try again.")
#subtraction problems
def subtract_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    result = num1 - num2
    print(f"{num1} - {num2}")
    user_answer = int(input("Enter the remainder of the subtraction: "))
    if user_answer == result:
        print("Congratulations! Your answer is correct.")
    else:
        print("Sorry, that's not the correct answer.")
#Menu options and extit message
def main():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == '1':
            add_random_numbers()
        elif choice == '2':
            subtract_random_numbers()
        elif choice == '3':
            print("Thank you for playing. Bye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

    
