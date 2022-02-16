def script():
    import random

    top_of_range = int(input("What do you want the max number to be? "))
    if top_of_range < 4:
        print("Please type a number greater than 4")
        quit()

    random_number = random.randint(0, top_of_range)
    computer_pick = random_number
    guesses = 0 


    while True:
        user_guess = int(input("Guess a number: "))
        guesses += 1
        if user_guess < computer_pick:
            print("Your guess is below the number!")
            continue
        elif user_guess > computer_pick:
            print("You're guess is above the number!")
            continue
        if user_guess == computer_pick:
            print("Correct!")
            print(" ")
            print("It took you", guesses, "guesses to guess the number.")
        user_choice = input("Would you like to restart the game yes or no?: ").lower().strip()
        if user_choice == "yes":
            script()
            
        else:
            quit()
script()