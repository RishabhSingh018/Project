print('''_                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')
print("Welcome to the treasure land\n Your mission is to find the treasure\nYou are at cross island")
direction=input("Where do you want to go?\n Type 'left' or 'right': ")
if direction=="left":
    print("You have come to a lake . There is an island in the middle of the lake ")
    action=input("Type 'wait' for the boat . Type 'swim' to swim across.\n")
    if action=="wait":
        print("You have arrived at the island unharmed. There is a house with 3 doors.\n One red One yellow and One blue")
        door=input("Which color do you want to chose? ").lower()
        if door=="yellow":
            print("You won the game")
        else:
            print("You lost")
    else:
        print("Attacked by the trout. Game over")
else:
    print("Game over")        

