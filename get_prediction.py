import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors():
    def __init__(self): 

        self.game=['rock','paper','scissors']

    def get_computer_choice(self):
        return random.choice(self.game)

    def get_user_choice(self):
        pass
        # your_choice = input("choose rock, paper or scissors: ").lower()
        
        # while your_choice !='rock' and your_choice !='paper' and your_choice!='scissors':
        #     print(type(your_choice))
        #     print ('Invalid input, choose again.')
        #     your_choice= input("choose rock, paper or scissors: ").lower()
            
        # else: 
        #     return your_choice


    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

        while True: 
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            cv2.imshow('frame', frame)
            # Press q to close the window
            print(prediction)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                    
        # After the loop release the cap object
        cap.release()
        # Destroy all the windows
        cv2.destroyAllWindows() 

        result = np.where(prediction ==np.amax(prediction))


    def get_winner(self, computer_choice, user_choice):

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

 
 def play(): 
    game=RockPaperScissors()
    computer_choice=game.get_computer_choice()
    user_choice =game.get_user_choice()
    print (f'computer chooses {computer_choice}')
    game.get_winner(computer_choice, user_choice)


play()