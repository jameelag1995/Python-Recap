print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
win = False
road = input("There are two ways in front of you which way would you like to take (left or right)?\n").lower()
if road == 'left':
    checkpoint = input("There is a station would you like to wait for the next bus or continue walking?\n").lower()
    if checkpoint == 'wait':
        choose = input("You find three doors after getting out of the bus a red,blue and a yellow one which one would you open? \n").lower()
        if choose == 'yellow':
            win = True
            print("You Win!")
if not win:
    print("Game Over.")
