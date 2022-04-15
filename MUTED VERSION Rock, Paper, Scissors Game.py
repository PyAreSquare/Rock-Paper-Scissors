#game engine from TechWithTim, completely modified by PyAreSquare
import random
import time
wins = 0
losses = 0
def gamestart(): #half of the code in gamestart() is from TechWithTim, check his YouTube channel!
    options = ["rock", "paper", "scissors"]
    wins = 0
    losses = 0
    games = int(input('how many rounds will there be?'))#modification
    gamesplayed = 1
    while games >= gamesplayed:
        user_input = input("rock paper or scissors?")

        if user_input not in options:
            continue

        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("the computer picked", computer_pick + ".")

        if user_input == "rock" and computer_pick == "scissors":
            print("you won!")
            wins += 1
            gamesplayed = gamesplayed+1#modification

        elif user_input == "paper" and computer_pick == "rock":
            print("you won!")
            wins += 1
            gamesplayed = gamesplayed+1#modification

        elif user_input == "scissors" and computer_pick == "paper":
            print("you won!")
            wins += 1
            gamesplayed = gamesplayed+1#modification

        elif user_input == computer_pick:#modification
            print("it's a draw!")#modification
            gamesplayed = gamesplayed+1#modification

        else:
            print("you lost!")
            losses = losses+1
            gamesplayed = gamesplayed+1#modification
            playsound("Bonk.wav")
    print('=======__GAME OVER__=======')#everything below or anything with '#modification' is done by me :)
    print("you won", wins, "times.")
    print("you lost", losses, "times.")
    time.sleep(3)
    if wins > losses :
        print('****__WELL_PLAYED!__****')
    elif wins < losses:
        print('****__BETTER_LUCK_NEXT_TIME!__****')
    elif wins == losses:
        print('***__WOW_ITS_A_DRAW!__***')
        time.sleep(3)
game_status = 'yes'
while game_status == 'yes' or game_status =='Yes':
    gamestart()
    game_status = str(input('do you want to play again?'))
print('=======__THANKS FOR PLAYING!__=======')
closingtime = 5
print('I hope you enjoyed!')
time.sleep(2)
print('closing in...')
while closingtime != 0:
    print(closingtime)
    closingtime = closingtime -1
    time.sleep(1)
time.sleep(1)

