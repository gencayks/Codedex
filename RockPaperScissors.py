import random

print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

player = int(input("Pick a number: "))

if player == 1:
    player = "rock"
elif player == 2:
    player = "paper"
elif player == 3:
    player = "scissors"
else:
    print("invalid number")
    exit()

computer = random.randint(1,3)
if computer == 1:
    computer = "rock" 
elif computer == 2:
    computer = "paper"
else:
    computer = "scissors"   

print(f"You chose: {player}")
print(f"CPU chose: {computer}")

if player == computer:
    print("It's a tie")
elif (player == "rock" and computer == "scissors") or (player == "scissors" and computer == "paper") or (player == "paper" and computer == "rock"):
    print("The player won!")
else:
    print("The CPU won!")