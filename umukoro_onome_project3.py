#Day 3 project: Treasure Island
print('''
*******************************************************************************
 __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/'
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the diamond.")
choice1 = input('You\'re at a crossroad, where do you want to go?'
                'Type "left" or "right."\n').lower()

if choice1 == "left":
    choice2 = input(
        'You\'ve come to a lake. '
        'There is an island in the middle of the lake. '
        'Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n').lower()

    if choice2 == "wait":
        choice3 = input("You're at the island unharmed."
                        "There's house with 3 doors. One red. "
                        "Which color do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game over!")
        elif choice3 == "yellow":
            print("You found the diamond. You win!")
        elif choice3 == "blue":
            print("You enter a room full of beasts. Game over!")
        else:
            print("You choose a door that doesn't exist. Game over!")
    else:
        print("You got attacked by an angry trout. Game over!")

else:
    print("You fell into a hole. Game over!")