import random

#Variables
options = ("rock","paper", "scissors")

user_wins = 0
computer_wins = 0


while True:
    #Asking User for their pick
    user_pick = input("Choose rock, paper, scissors or q to quit: ").strip().lower()


    # if statement that shows the user wins, computer wins, then closes the program
    if user_pick == "q":
        print("The User got", user_wins, "wins!")
        print("The Computer got", computer_wins, "wins!")
        if user_wins > computer_wins:
            print("The User wins the game!")
        elif user_wins == computer_wins:
            print("It's a tie!")
        else:
            print("The Computer wins the game!")
        break
    
    if user_pick not in options or not "q":
        print("Type in a valid pick.")
        continue
    
    random_pick = random.choice(options)
    computer_pick = random_pick
    print(computer_pick)    

    # if statment to determine who wins based on the user and computer picks
    if user_pick == computer_pick:
        print("It's a tie!")
    if user_pick == "rock" and computer_pick == "scissors":
        user_wins += 1
        print("The user wins!")
    elif user_pick == "paper" and computer_pick == "rock":
        user_wins += 1
        print("The user wins!")
    elif user_pick == "scissors" and computer_pick == "paper":
        user_wins += 1
        print("The user wins!")
    else:
        computer_wins += 1
        print("Computer wins!")



