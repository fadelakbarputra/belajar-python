from math import e
import random
game = [ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
]
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
game.append(paper)

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game.append(scissors)

choice = int(input("Mau batu (0), kertas (1), atau gunting (2)? \n"))
us = game[choice]
print(us)

computer_choice = random.randint(0,2)
computer = game[computer_choice]
print("Computer choose: \n")
print(computer)

if us == game[2] and computer == game[0]:
    print("You lose!")
elif choice > computer_choice:
    print("You win!")
elif choice < computer_choice:
    print("You lose!")
elif choice == computer_choice:
    print("Draw!")
else:
    print("Invalid input!, you lose!")