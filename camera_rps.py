import random
from timeit import Timer
from typing_extensions import Self
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors():
    def __init__(self):
        self.game=['rock','paper','scissors']
        print ("Please look at the camara and play rock, paper or scissors")
        print ("You need to win 3 times before the computer to win this game! ")
        time.sleep(2)

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
        timer = int(4)

        while timer >= 0:  
            ret, frame = cap.read()
            resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
            image_np = np.array(resized_frame)
            normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
            data[0] = normalized_image
            prediction = model.predict(data)
            font = cv2.FONT_HERSHEY_SIMPLEX

            cv2.putText(frame, 
                str(timer), 
                (600, 600), font, 10, 
                (255,0,255), 
                10, 
                cv2.LINE_4)
            
            curr = time.time()
            if curr - start >=1:
                start = curr
                timer=timer-1

            print(prediction)
  
            cv2.imshow('frame', frame)
        
            self.result = np.where(prediction[0]==np.amax(prediction[0]))[0][0]
            # Press q to close the window    
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
                print(f'You select {user_choice}')
                print (f'Computer chooses {computer_choice}')
                print(f'User wins {user_chance}')
                print(f'Computer wins {computer_chance}')

            elif self.get_winner(computer_choice, user_choice) == 'computer':
                computer_chance+=1
                print(f'You select {user_choice}')
                print (f'Computer chooses {computer_choice}')
                print(f'User wins {user_chance}')
                print(f'Computer wins {computer_chance}')

            else: 
                print(f'You select {user_choice}')
                print (f'Computer chooses {computer_choice}')
                print ("It is a draw, keep playing!")
                print(f'User wins {user_chance}')
                print(f'Computer wins {computer_chance}')
            
            time.sleep(3)

        else: 
            if user_chance==3:
                print('User has won! Congrats!')
                time.sleep(1)
                # check this out 
                exit()
            elif computer_chance==3:
                print ('Computer has won! Good luck next time!') 
                time.sleep(1)
                exit()

if __name__ == '__main__':
    game = RockPaperScissors()
    game.play()


# def start_video(self):
#     while True: 
#         ret, frame = self.cap.read()
#         resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
#         image_np = np.array(resized_frame)
#         normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
#         self.data[0] = normalized_image
#         self.prediction = self.model.predict(self.data)
#         cv2.imshow('frame', frame)
#         self.start_game()
#             # Press q to close the window
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         self.stop_video()

# def start_game(self):
    
#     while self.user_score <3 and self.computer_score <3:
#         self.timer()
#         #print(self.prediction)
#         user_choice = self.get_prediction()
#         print(user_choice)
#         computer_choice = self.get_computer_choice()
#         print(computer_choice)
#         self.get_winner(computer_choice,user_choice)
#         if self.user_score == 3: 
#             print('You have won! What a hero')
#             exit()
#         elif self.computer_score == 3:
#             print('You lost the game! Doofus')
#             exit()

    # def timer(self):
    #     countdown_timer = 3
    #     while countdown_timer>0:
    #         print(f"Show you hand in {countdown_timer} seconds")
    #         sleep(1)
    #         countdown_timer -= 1
    #     print('GO!')
    #     ret, frame = self.cap.read()
    #     resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    #     image_np = np.array(resized_frame)
    #     normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    #     self.data[0] = normalized_image
    #     self.prediction = self.model.predict(self.data)
    #     self.get_prediction()

    # def start_timer(self):
    #     countdown_timer = 3
    #     while countdown_timer>0:
    #         print(f"starts in {countdown_timer} seconds")
    #         sleep(1)
    #         countdown_timer -= 1
    #     print('START GAME!')
    #     ret, frame = self.cap.read()
    #     resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
    #     image_np = np.array(resized_frame)
    #     normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
    #     self.data[0] = normalized_image
    #     self.prediction = self.model.predict(self.data)
    #     self.get_prediction()




        
        




