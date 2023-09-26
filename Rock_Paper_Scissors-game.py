import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_selection = input("Choose [r]ock, [p]aper or [s]cissors: ")

if player_selection == "r":
    player_selection = rock
elif player_selection == "p":
    player_selection = paper
elif player_selection == "s":
    player_selection = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_selection = random.randint(1, 3)
computer_selection = ""
if computer_random_selection == 1:
    computer_selection = rock
elif computer_random_selection == 2:
    computer_selection = paper
else:
    computer_selection = scissors

if (player_selection == rock and computer_selection == scissors) \
        or (player_selection == paper and computer_selection == rock) \
        or (player_selection == scissors and computer_selection == paper):
    print("You win!")
elif player_selection == computer_selection:
    print("Draw!")
else:
    print("You lose!")