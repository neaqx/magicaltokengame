# Welcome to the Magical Token Machhine. Start the game in the terminal. Run the code.

import random


symbols = ["A", "B", "C", "D"]
symbol_count = {"A":4, "B":5, "C":10, "D":12}
symbol_value = {"A":10, "B":5, "C":2, "D":1}


class magic_machine:
    
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
                    print(f"{bet} Tokens have been bet. You now have {self.tokens} tokens.")
                    return bet
                else:
                    print("Invalid bet. Please bet a number between 1 and your total token amount.")
            except ValueError:
                print("Invalid bet. Please bet a number")
                
    def spin(self,bet,lines):
        print("You have spun the machine!")
        results = []
        for _ in range(lines):
            spin_result = [random.choice(symbols)for _ in range(3)]
            print(" | ".join(spin_result))
            if all( s == spin_result[0] for s in spin_result):
                win = symbol_value[spin_result[0]]*bet
                print(f"You won! You won {win} tokens!")
                self.tokens += win
                self.total_wins += 1
            else:
                print("You lost.")
                results.append(spin_result)
            self.total.games += 1
            print(f"You have {self.tokens} tokens.")
            return results
    
    def payout_tokens(self):
        print(f"Payout: {self.tokens} Tokens")