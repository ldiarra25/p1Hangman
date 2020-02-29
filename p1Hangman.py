#Objective: This program will allow the user to play Hangman against the computer using a list of words from a text file.’
import random

keepPlaying = True

while(keepPlaying == True):
    print("Welcome")
    print("First to 2 wins. Press q to quit. Write in lower case!")
    #rock is 1, paper is 2, scissors is 3
   
    scoreComp = 0
    scorePlayer = 0
   
    while(scorePlayer < 2) and (scoreComp < 2):
        choiceComp = random.randint(1,3)
        choicePlayer = input("Type in rock, paper, or scissors: ")
       
        if(choicePlayer == "q"):
            keepPlaying = False
            break
        elif((choicePlayer == "rock" ) and (choiceComp == 1)) or ((choicePlayer == "paper" ) and (choiceComp == 2)) or ((choicePlayer == "scissors" ) and (choiceComp == 3)):
            print("DRAW!")
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
           
        elif((choicePlayer == "rock" ) and (choiceComp == 2)) or ((choicePlayer == "paper" ) and (choiceComp == 3)) or ((choicePlayer == "scissors" ) and (choiceComp == 1)):
            print("You lose this round")
            scoreComp = scoreComp + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        elif((choicePlayer == "rock" ) and (choiceComp == 3)) or ((choicePlayer == "paper" ) and (choiceComp == 1)) or ((choicePlayer == "scissors" ) and (choiceComp == 2)):
            print("You won this round!")
            scorePlayer = scorePlayer + 1
            print("Computer's Score: ", + scoreComp)
            print("Your Score: ", + scorePlayer)
        else :
            print("Input is invalid!")
           
    if (scorePlayer == 2):
            print("You win")
         
           
    if (scoreComp == 2):
            print("You lost")
           
    print("Computer's Score: ", + scoreComp , "Your Score: ", + scorePlayer)