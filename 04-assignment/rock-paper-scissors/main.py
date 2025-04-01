import random # for chossing a random option 

def play():
    user= input( 'choose r for rock , p for paper and s for scissor \n')
    computer = random.choice(['r','p','s'])
    
    if  user == computer:
        print(f'You choose {user} and the computer choose {computer} \n')
        return 'It is tie'
    if is_win(user,computer):
        print(f'You choose {user} and the computer choose {computer} \n')
        return 'You win'
  
  
    print(f'You choose {user} and the computer choose {computer} \n')
    return 'You lost'
    
def is_win(player ,opponent):
    if (player == 'r' and opponent == 's') or(player == 's' and opponent == 'p') or(player == 'p' and opponent == 'r'):
        return True
    
print(play())



