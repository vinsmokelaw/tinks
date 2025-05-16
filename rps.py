import random

options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player= input("Enter a choice (rock, paper, scissors): ")

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")

    # play_again = input("Play again? (y/n): ").lower()
    # if  play_again.lower() != "y":
    #     running = False

    if not input ("Play again? (y/n): ").lower == "y":
        running = False

print("Thanks for playing!")