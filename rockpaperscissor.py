import random
"""

0 - Rock
1 - Paper
2 - Scissor
 
"""
while True:
#takes the user input
    user_choice = int(input("Enter a number , 0-Rock , 1-Paper ,2-Scissor: "))
    if  user_choice < 0  or user_choice >=3:
        print("You have entered and invalid number, You Lose...!")
    else:
    #computer generates the random integer between 0-2
        computer_choice = random.randint(0,2)
        
        #Displays users and computer selection
        print("User Chose: "+str(user_choice))
        print("Computer chose:  "+str(computer_choice))
        
        #condition to check game is draw
        if user_choice == computer_choice:
           print("It's a draw")
        elif user_choice == 0 and computer_choice == 2:
            print("You win...!")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lost...!")
        elif computer_choice > user_choice:
           print("You Loose....!")
        elif user_choice > computer_choice:
            print("You won....!")
        elif user_choice == 0 and computer_choice == 2:
            print("You win...!")
        elif computer_choice == 0 and user_choice == 2:
            print("You Lost...!")
        
         # Ask the user if they want to play again, with input validation
        while True:
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again in ['y', 'n']:
                break
            else:
                print("Invalid input! Please enter 'y' or 'n'.")
    
           # Exit the loop if the user chooses not to play again
        if play_again == 'n':
            print("Thanks for playing!")
            break