import random

options = ('rock', 'paper', 'scissors')



running =True


while True:
    player = None

    computer = random.choice(options)
    
    
    while player not in options:
        player = input('Enter a choice (rock, paper, scissor): ')

    print(f' player: {player}')
    print(f' computer: {computer}')

    if player == computer:
        print('It\'s a tie!')
    elif player == 'rock' and computer == 'scissors':
        print('You win!')
    elif player == 'paper' and computer == 'rock':
        print('You win!')
    elif player == 'scissors' and computer == 'paper':
        print('You win!')
    else:
        print('You loose!')
        
    play_again = input('Play again? (y/n):').lower()
    if not play_again == 'y':
        running = False
        
print('Thanks for playing')
        
    