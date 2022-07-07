import random
from typing_extensions import Self
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors():
    def __init__(self): 

        self.game=['rock','paper','scissors']
        print ("Please look at camary and play rock, paper or scissors")
        print ("You need to win 3 times to win beofre ")

    def get_computer_choice(self):
        return random.choice(self.game)

    def get_user_choice(self):
        
        self.get_prediction()
        choice = ''
    
        while self.result == 3: 
            print ("Sorry I didn't catch it, play again")
            self.get_prediction()
        else: 
            if self.result==0:
                choice = 'rock'
            elif self.result==1:
                choice ='paper'
            elif self.result==2:
                choice ='scissors'
        
        return choice
    
    def get_prediction(self):
        model = load_model('keras_model.h5',compile=False)
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        self.result = -1
        start = time.time()
        finish = start +4

        while time.time()<finish: 
            
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            
            self.result = np.where(prediction[0]==np.amax(prediction[0]))[0][0]
                
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 

        return self.result

    

    def get_winner(self, computer_choice, user_choice):

        winner = ''

        if computer_choice == user_choice:
            print ('draw')
            winner = 'none'
        elif computer_choice=='rock' and user_choice=='scissors':
            winner = 'computer'
        elif computer_choice =='paper' and user_choice =='rock':
            winner = 'computer'
        elif computer_choice == 'scissors' and user_choice =='paper':
            winner = 'computer'
        else: 
            winner = 'user'
        
        return winner
    
    def play(self):

        user_chance = 0
        computer_chance=0
        
        while user_chance<3 and computer_chance<3:
            computer_choice = self.get_computer_choice()
            user_choice = self.get_user_choice()

            
            if self.get_winner(computer_choice, user_choice) == 'user': 
                user_chance+=1
                print(f'you select {user_choice}')
                print (f'computer chooses {computer_choice}')
                print(f'user wins {user_chance}')
                print(f'computer wins {computer_chance}')

            elif self.get_winner(computer_choice, user_choice) == 'computer':
                computer_chance+=1
                print(f'you select {user_choice}')
                print (f'computer chooses {computer_choice}')
                print(f'user wins {user_chance}')
                print(f'computer wins {computer_chance}')
            else: 
                print(f'you select {user_choice}')
                print (f'computer chooses {computer_choice}')
                print ("It is a draw, keep playing!")
                print(f'user wins {user_chance}')
                print(f'computer wins {computer_chance}')
                   
        else: 
            if user_chance==3:
                print('User wins!')
            elif computer_chance==3:
                print ('computer wins!') 


game = RockPaperScissors()
game.play()
                
                


        
        




