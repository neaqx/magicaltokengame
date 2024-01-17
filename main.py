# Welcome to the Magical Token Machhine. Start the game in the terminal. Run the code.

import random


symbols = ["A", "B", "C", "D"]
symbols_count = {"A":4, "B":5, "C":10, "D":12}
symbols_value = {"A":10, "B":5, "C":2, "D":1}


class magicMachine:
    
    def __init__(self):
        self.tokens = 0
        self.total_games = 0
        self.total_wins = 0
        self.max_lines = 5
        
    def deposit_tokens(self):
        while True:
            try:
                amount = int(input("How many tokens would you like to deposit? "))
                if amount > 0:
                    self.tokens += amount
                    print(f"You now have {self.tokens} tokens.")                    
                    break
                else:
                    print("Please enter a valid number of tokens.")
            except ValueError:
                print("Please enter a valid number of tokens.")
                
    def place_bet(self):
        while True:
            try:
                bet = int(input("How many tokens would you like to bet? "))
            if 0 < bet <= self.tokens:
                self.tokens -= bet
                print(f"")
