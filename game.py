import random
import time

class Player:
    def __init__(self):
        self.score=0
        self.num=0
    def generate_num(self):
        self.num=random.randint(1,3)
    def win_round(self):
        self.score+=1

    def get_num(self):
        return self.num
    def get_score(self):
        return self.score


class Game:
    def __init__(self, p1:Player, p2:Player):
        self.p1=p1
        self.p2=p2
        self.trials=0
        
    def start(self):
        print("Game has begun!")
    def end(self):
        print("Game has ended!")
    
    def display_round_result(self):
        print(f"Player 1 score: {self.p1.get_score()}\nPlayer 2 score: {self.p2.get_score()}\n___________________________")

    def display_winner(self):
        print(f"Max score: {max(self.p1.get_score(),self.p2.get_score())}")
        if self.p1.get_score()>self.p2.get_score():
            print("player 1 won")
        elif self.p1.get_score()<self.p2.get_score():
            print("player 2 won")
        else:
            print("Draw")
        
    def loop(self):
        while(self.trials<=4):
            self.p1.generate_num()
            self.p2.generate_num()
            self.play()
            self.display_round_result()
            time.sleep(2)
            self.trials+=1
        self.display_winner()

    def play(self):
        if(self.p1.get_num() == self.p2.get_num() ):
            pass #draw
        if(self.p1.get_num()==1 and self.p2.get_num()==2):
            self.p2.win_round() #2 wins
        if(self.p1.get_num()==1 and self.p2.get_num()==3):
            self.p1.win_round() #1 wins
        if(self.p1.get_num()==2 and self.p2.get_num()==1):
            self.p1.win_round() #1 wins
        if(self.p1.get_num()==2 and self.p2.get_num()==3):
            self.p2.win_round()  #2 wins
        if(self.p1.get_num()==3 and self.p2.get_num()==1):
            self.p2.win_round()  #2 wins
        if(self.p1.get_num()==3 and self.p2.get_num()==2):
            self.p1.win_round()  #1 wins




