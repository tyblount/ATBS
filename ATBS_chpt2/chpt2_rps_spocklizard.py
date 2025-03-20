import random, sys
import time
print('Rock, Paper, Scissors, Spock, Lizard')
#following variables keep track of wins/losses/ties
wins = 0
losses = 0
ties = 0
#main loop
while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:     #player input loop
        print('What\'s your move? (ro)ck (pa)per (sc)issors (sp)ock (li)zard or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()     #quit program
        if playerMove == 'ro' or playerMove == 'pa' or playerMove == 'sc' or playerMove == 'sp' or playerMove == 'li':
            break     #break out of 'player input loop'
        print ('Type one of ro, pa, sc, sp, li, or q.')
    #diplay player's choice
    if playerMove == 'ro':
        print('ROCK versus...')
    elif playerMove == 'pa':
        print('PAPER versus...')
    elif playerMove == 'sc':
        print('SCISSORS versus...')
    elif playerMove == 'sp':
        print('SPOCK versus...')
    elif playerMove == 'li':
        print('LIZARD versus...')
    #adding suspense
    time.sleep(1.5)
    #display computer's choice
    randomNumber = random.randint(1,5)
    if randomNumber == 1:
        computerMove = 'ro'
        print('ROCK')
    if randomNumber == 2:
        computerMove = 'pa'
        print('PAPER')
    if randomNumber == 3:
        computerMove = 'sc'
        print('SCISSORS')
    if randomNumber == 4:
        computerMove = 'sp'
        print('SPOCK')
    if randomNumber == 5:
        computerMove = 'li'
        print('LIZARD')
    #adding suspense
    time.sleep(0.5)
    #display and record win/loss/tie
    if playerMove == computerMove:
        print('It\'s a tie!')
        ties = ties + 1
    elif (     #Parentheses group all win conditions
    (playerMove == 'ro' and computerMove == 'sc') or  # Rock vs. Scissors
    (playerMove == 'ro' and computerMove == 'li') or  # Rock vs. Lizard
    (playerMove == 'pa' and computerMove == 'ro') or  # Paper vs. Rock
    (playerMove == 'pa' and computerMove == 'sp') or  # Paper vs. Spock
    (playerMove == 'sc' and computerMove == 'pa') or  # Scissors vs. Paper
    (playerMove == 'sc' and computerMove == 'li') or  # Scissors vs. Lizard
    (playerMove == 'sp' and computerMove == 'ro') or  # Spock vs. Rock
    (playerMove == 'sp' and computerMove == 'sc') or  # Spock vs. Scissors
    (playerMove == 'li' and computerMove == 'sp') or  # Lizard vs. Spock
    (playerMove == 'li' and computerMove == 'pa')     # Lizard vs. Paper
    ):
        print('You win!')
        wins += 1
    elif (     #Parentheses group all loss conditions
    (playerMove == 'ro' and computerMove == 'pa') or  # Rock vs. Paper
    (playerMove == 'ro' and computerMove == 'sp') or  # Rock vs. Spock
    (playerMove == 'pa' and computerMove == 'sc') or  # Paper vs. Scissors
    (playerMove == 'pa' and computerMove == 'li') or  # Paper vs. Lizard
    (playerMove == 'sc' and computerMove == 'ro') or  # Scissors vs. Rock
    (playerMove == 'sc' and computerMove == 'sp') or  # Scissors vs. Spock
    (playerMove == 'sp' and computerMove == 'li') or  # Spock vs. Lizard
    (playerMove == 'sp' and computerMove == 'pa') or  # Spock vs. Paper
    (playerMove == 'li' and computerMove == 'ro') or  # Lizard vs. Rock
    (playerMove == 'li' and computerMove == 'sc')     # Lizard vs. Scissors
    ):
        print('You lose!')
        losses += 1