rock = '''
    _______
---'   ____)
        (_____)
        (_____)
        (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)_____
            ______)
            _______)
            _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
            ______)
        __________)
        (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = int(input("What do you choose> Type 0 for Rock, 1, for Paper or 2 for Scissors.\n"))

choices = [rock, paper, scissors]

print(choices[player_choice])

print("Computer chooses:")

comp_choice = random.randint(0,2)
print(choices[comp_choice])

if player_choice == 0 and comp_choice == 1:
    print("You Lose")
elif player_choice == 0 and comp_choice == 2:
    print("You Win")
elif player_choice == 0 and comp_choice == 0:
    print("Draw")
elif player_choice == 1 and comp_choice == 0:
    print("You Win")
elif player_choice == 1 and comp_choice == 2:
    print("You Lose")
elif player_choice == 1 and comp_choice == 1:
    print("Draw")
elif player_choice == 2 and comp_choice == 0:
    print("You Lose")
elif player_choice == 2 and comp_choice == 1:
    print("You Win")
elif player_choice == 2 and comp_choice == 2:
    print("Draw")