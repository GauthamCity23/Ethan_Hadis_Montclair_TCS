'''
Make a 2 player game of rock paper scissors
Each person will get a turn to enter their selection (rock/paper/scissors)
Should work for any upper or lower cased input
If someone types in a garbage value, ask them to reenter
If playerA enters a good value, playerB enters garbage, only ask player B to reenter, NOT PLAYERA
Make it best of 5 (firs to 3). 
If there is a tie, then no points awarded. Win is 1 point. Lose is 0. 
Print the score after every round. 
We needa greeting message at the start (hello, welcome to my game, etc etc)
Have a game over message + who won. 
Ask if they want to play again
If they say yes, they should be to play again without stopping the program
If they say no, give them a goodbye message and call it a day. 
'''
import time

welcome_back = False
aScore = 0
bScore = 0
round_number = 1
aStatus = 0
aChoice = ""
bChoice = ""

def battle_round():
    if aChoice == bChoice:
        aStatus = 0
        return
    elif aChoice == "rock":
        if bChoice == "paper":
            aStatus = -1
            bScore += 1
            return
        else:
            aStatus = 1
            aScore += 1
    elif aChoice == "paper":
        if bChoice == "rock":
            aStatus = 1
            aScore += 1
            return
        else:
            aStatus = -1
            bScore += 1
            return
    else:
        if bChoice == "paper":
            aStatus = 1
            aScore += 1
            return
        else:
            aStatus = -1
            bScore += 1
            return


while True:
    if welcome_back == False:
        print("Welcome to Rock, Paper, Scissors!")
    else:
        print("Welcome back!")
    time.sleep(1.5)
    while aScore != 3 and bScore != 3:
        print("Round " + round_number)
        aChoice = str(input("Player 1, choose rock, paper, or scissors."))
