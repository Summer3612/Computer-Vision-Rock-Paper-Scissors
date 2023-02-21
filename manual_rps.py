import random


game=['rock','paper','scissors']

def get_computer_choice():
    return random.choice(game)

def get_user_choice():
    
    your_choice = input("choose rock, paper or scissors: ").lower()
    
    while your_choice !='rock' and your_choice !='paper' and your_choice!='scissors':
        print(type(your_choice))
        print ('Invalid input, choose again.')
        your_choice= input("choose rock, paper or scissors: ").lower()
        
    else: 
        return your_choice

def get_winner(computer_choice, user_choice):

    if computer_choice == user_choice:
        print ('draw')
    elif computer_choice=='rock' and user_choice=='scissors':
        print ('computer wins!')
    elif computer_choice =='paper' and user_choice =='rock':
        print ('computer wins!')
    elif computer_choice == 'scissors' and user_choice =='paper':
        print ('computer wins!')
    else: 
        print('User wins!')

def play (): 
    
    computer_choice=get_computer_choice()
    print(type(computer_choice))
    user_choice = get_user_choice()
    print (f'computer chooses {computer_choice}')
    get_winner(computer_choice, user_choice)

 
