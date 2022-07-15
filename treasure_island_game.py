from turtle import left


print('''
____▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄_
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────
─▄▄──█░░░▀█▀░░░█──▄▄─
█░░█─▀▄░░░░░░░▄▀─█░░█
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█---╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗-█
█---║║║╠─║─║─║║║║║╠─-█
█---╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝-█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
''')

print("Welcome to treasure island!")
print("Your mission is to find the treasure")
left_right = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'")

if left_right == "left":
    lake = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if lake == "wait":
        doors = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        if doors == "yellow":
            print("You found the treasure! You win!")
        elif doors == "blue":
            print("You enter a room of beasts. Game over.")
        elif doors == "red":
            print("It's room full of fire. Game over.")
        else:
            print("You chose a door that doesn't exist. Game over.")
    elif lake == "swim":
        print("You get attacked by an angry trout. Game over.")
    else:
        print("You get attacked by an angry trout. Game over.")
else:
    print("You fell into a hole. Game over")
