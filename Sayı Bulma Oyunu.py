import random

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def random_choice():
    return random.choice(number_list)

def play_game():
    secret_number = random_choice()
    guess_list = []

    print("Welcome to the number guessing game")
    print("Find the secret number")

    while True:
        number = int(input("Enter your guess: "))
        if number in number_list:
            print("Your guess is in the list.")
            
            if number == secret_number:
                print(f"Your guess is correct: {number}")
                break
            else:
                if number > secret_number:
                    print("Your guess number is greater than the secret number.")
                else:
                    print("Your guess number is less than the secret number.")
                print(f"Your guess is wrong. True number: {secret_number}\nTry again.")
        else:
            print("Your guess is not in the list")

play_game()
    


    

    

    
    
