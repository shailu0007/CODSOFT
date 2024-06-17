import random

option = ("rock","paper","scissors")

running = True
while running:
        player = None
        computer = random.choice(option)
        while player not in option:
            player = input("Enter choice(rock,paper,scissors)")

            print(f"player: {player}")
            print(f"Computer: {computer}")

            if player == computer:
                print("It's a tie!")
            elif player == "rock" and computer == "scissors":
                print("You Win!")
            elif player == "scissors" and computer == "paper":
                print("You Win!")
            elif player == "paper" and computer == "rock":
                print("You Win!")
            else:
                print("You Lose!")
                
        if input("play again (y/n)").lower() == "n":
               running = False
               
print("-------------------------\n Thank you for playing \n-------------------------")
