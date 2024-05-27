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
---'   ____)____
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
import random
player = int(input("What do you choose? Type  0 for Rock, 1 for Paper or 2 for Scissors.\n"))
cpu = random.randint(0,2)
result = ''
if player == cpu: result = 'Draw'
if player == 0:
    if cpu == 1: result = 'You lose'
    if cpu == 2: result = 'You win'
if player ==  1:
    if cpu == 0: result = 'You win'
    if cpu == 2: result = 'You lose'
if player ==  2:
    if cpu == 0: result = 'You lose'
    if cpu == 1: result = 'You win'
options = [rock,paper,scissors]
print(options[player])
print("Computer chose:")
print(options[cpu])
print(result)