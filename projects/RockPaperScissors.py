from sys import exit
import random

choices = [
            "rock",
            "paper",
            "scissors",
]

player_name = input("Username: ")

while True:

    def game():

        user_score = 0
        computer_score = 0

        while (user_score < 5) and (computer_score < 5):

            choice = input("rock, paper, or scissors? >>> ")
            computer_ans = choices[random.randint(0, 2)]


            def conditions():
        
                if (choice == choices[0]) and (computer_ans == choices[0]):
                    return None
                elif (choice == choices[0]) and (computer_ans == choices[1]):
                    return False
                elif (choice == choices[0]) and (computer_ans == choices[2]):
                    return True
                elif (choice == choices[1]) and (computer_ans == choices[0]):
                    return True
                elif (choice == choices[1]) and (computer_ans == choices[1]):
                    return None
                elif (choice == choices[1]) and (computer_ans == choices[2]):
                    return False
                elif (choice == choices[2]) and (computer_ans == choices[0]):
                    return False
                elif (choice == choices[2]) and (computer_ans == choices[1]):
                    return True
                elif (choice == choices[2]) and (computer_ans == choices[2]):
                    return None
                else:
                    print("The developer of this program has made a mistake.\n")

            conditions()
    
            if conditions() == True:
                user_score += 1
            elif conditions() == False:
                computer_score += 1

            print(f"\n{player_name}: {choice}\n")
            print(f"Computer: {computer_ans}\n")

            if conditions() == True:
                print(f"1 point to {player_name}\n")
            elif conditions() == False:
                print("1 point to Computer.\n")
            elif conditions() == None:
                print("It's a draw! Points to none.\n")

            print(f"Score ( {user_score} : {computer_score} )\n")

        if user_score >= 5:
            print(f"Congratulations {player_name}, You won!")
        elif computer_score >= 5:
            print("Computer won.")
    game()
    while True:
        ans = input("Wanna play again? (*1* for yes, *2* for no) ")
        if ans == "1":
            game()
        elif ans == "2":
            print("Aww :( ")
            exit(0)
        else:
            print("Type 1 for 2, ")