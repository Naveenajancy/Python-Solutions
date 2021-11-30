# playing rock, paper, scissors
import random

while True:
    computer_answer = random.choice(['rock','paper','scissors'])
    user_choice = input("Choose you options Rock, Paper, Scissors\n")
    user_choice = user_choice.lower()
#   print("Please check your answer")
    if computer_answer == user_choice:
        print(f"Both players selected {computer_answer}. It's a Tie! ")
    elif user_choice == 'paper' and computer_answer == 'rock':
        print("Paper beats rock ! You win :) the computer had " + computer_answer)
    elif user_choice == 'rock' and computer_answer == 'scissors':
        print("you win :) the computer had " + computer_answer)
    elif user_choice == 'scissors' and computer_answer == 'paper':
        print("you win :) the computer had " + computer_answer)
    else:
        print("Computer Win the computer had " + computer_answer)

    play_again = input("Do you want to play again? (y/n):")
    if play_again.lower() == "y":
        continue
    if play_again.lower() == "n":
        print(f"Thanks for playing see you soon")
        break
    elif play_again.lower() != "y" and "n":
        print("please press (y/n)")
