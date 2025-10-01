import random


def guess_the_number():

    number_to_guess = random.randint(1, 100)
    attemts = 0
    
    print("Welcome to 'guess the number'!")
    print("i have selected a number between i and a 100.")
    print("try to guess it")


    while True:
        player_guess = input("enter number")
        if not player_guess.isdigit():
         print("please enter a valid number.")
         continue

        player_guess = int(player_guess)
        attemts += 1


        if player_guess < number_to_guess:
           print("too low, try again")
        elif player_guess > number_to_guess:
           print("too high, try again.")
        else:
           print(f"congratulations! you guessed the number {number_to_guess} in {attemts} attemts.")
           break
guess_the_number()