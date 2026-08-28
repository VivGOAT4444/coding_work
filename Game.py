import random


computer_number = random.randint(1, 3)
if computer_number == 1:
    computer_action = "rock"
elif computer_number == 2:
    computer_action = "paper"
else:
    computer_action = "scissors"


user_action = input("Enter your choice (rock, paper, scissors): ")

print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")


if user_action == computer_action:
    print("It's a tie!")
elif (user_action == "rock" and computer_action == "scissors") or \
     (user_action == "paper" and computer_action == "rock") or \
     (user_action == "scissors" and computer_action == "paper"):
    print("You win!")
else:
    print("You lose!")

