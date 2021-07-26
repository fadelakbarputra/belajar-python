print('''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("======================WELCOME TO TREASURE ISLAND=========================")
print("Your mission is to find the treasure!")
direction = input("You are now in the road, what do you choose? left or right?\n")
if direction.lower() == "right":
    print("You are just crashed by truck, go to isekai and game over!")
elif direction.lower() == "left":
    choice = input("You reached lake, wanna swim or wait for ship?\n")
    if choice.lower() == "swim":
        print("You are eaten by crocodile, game over!")
    elif choice.lower() == "wait":
        door = input("You have arrived at temple, which door do you want to open? Blue, red, or yellow?\n")
        if door.lower() == "red":
            print("You are burned by fire, game over!")
        elif door.lower() == "blue":
            print("You are eaten by monster, game over!")
        elif door.lower() == "yellow":
            print("You win!!!")
        else:
            print("Game over!")
    else:
        print("Game  over!")
else:
    print("Game over!")