GameName = ('_____ROCK - PAPER - SCISSOR - GAME_____')
(print(GameName.center(150)))
playerScore = 0
computerScore = 0
tie = 0
print()
print('Enter Your Name:')
name = input()
Name = name.upper()
print('Welcome', Name)
print('use specific keywords for playing a GAME as mentioned below!!')
board = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSOR'}
for i, j in board.items():
    print(i, ':', j)

# Computer's moves
import random
list = ['R', 'P', 'S']
computerMoves = random.choice(list)
print("I had selected my move now it's your turn: ")

# Player's moves

for moves in range(10):
    print('Take Your Turn: ')
    playersMove = input().upper()

    # checking for various condition's
    # For ROCK
    if computerMoves == 'R' and playersMove == 'P':
        playerScore += 1
        print(Name, 'has', playerScore, 'point.')
    elif computerMoves == 'R' and playersMove == 'S':

        computerScore += 1
        print('Computer has', computerScore, 'point.')
    # for PAPER
    elif computerMoves == 'P' and playersMove == 'S':
        playerScore += 1
        print(Name, 'has', playerScore, 'point.')
    elif computerMoves == 'P' and playersMove == 'R':
        computerScore += 1
        print('Computer has', computerScore, 'point.')
    # for SCISSORS
    elif computerMoves == 'S' and playersMove == 'R':
        playerScore += 1
        print(Name, 'has', playerScore, 'point.')
    elif computerMoves == 'S' and playersMove == 'P':
        computerScore += 1
        print('Computer has', computerScore, 'point.')
    elif computerMoves == playersMove:
        tie += 1
        break

# winning and losses
print(Name, 'won:', playerScore)
print('########')
print('computer won:', computerScore)
print('########')
print('ties:', tie)

# Result Analysis
if playerScore > computerScore:
    print('Hence!', Name, 'won the match.')
elif playerScore < computerScore:
    print('And thus computer won the match. ')
else:
    print('MATCH TIE!')



