# Welcome to the Magical Token Machhine. Start the game in the terminal. Run the code.

import random

symbols = ["A", "B", "C", "D", "E"]
symbol_count = {"A":4, "B":10, "C":14, "D":12, "E":1}
symbol_value = {"A":10, "B":5, "C":2, "D":1, "E":0}
class MagicMachine:    
    def __init__(self):
        self.tokens = 0
        self.total_games = 0
        self.total_wins = 0
        self.max_lines = 5
        self.free_spins = 0

#Deposit tokens to play       
    def deposit_tokens(self):
        while True:
            try:
                amount = int(input("How many tokens would you like to deposit?\n "))
                if amount > 0:
                    self.tokens += amount
                    print(f"You have deposited {amount} tokens. Total: {self.tokens} tokens")
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                    print("Invalid input. Please enter a number.")
                    
#Check if player gets bonus spins                   
    def check_bonus(self):
        if random.randint(1,10) == 1:
            bonus_spins = random.randint(1,5)
            print(f"You have won {bonus_spins} free spins!")
            self.free_spins += bonus_spins

#Place bet and check if bet is valid               
    def place_bet(self):
        while True:
            try:
                bet = int(input("How many tokens would you like to bet?\n "))
                if 0 < bet <= self.tokens:
                    print(f"{bet} Tokens have been bet. You now have {self.tokens - bet} tokens.")
                    return bet
                else:
                    print("Invalid bet. Please bet a number between 1 and your total token amount.")
            except ValueError:
                print("Invalid bet. Please bet a number")
                               
#Spin the machine and check if player gets bonus tokens                
    def spin(self,bet,lines):
        if self.free_spins > 0:
            print(f"You have {self.free_spins} free spins left.")
            self.free_spins -= 1
        else:
            if self.tokens < bet:
                print(f"{bet} tokens have been bet. You now have {self.tokens} tokens.")
                return
            self.tokens -= bet
            print(f"{bet} tokens have been bet. You now have {self.tokens} tokens.")
            
            
            print("You have spun the machine!")
        results = []
        for _ in range(lines):
            spin_result = [random.choice(symbols)for _ in range(3)]
            print(" | ".join(spin_result))
            if "E" in spin_result:
                special_bonus = random.randint(1,100)
                print(f"Special symbol E appeared! You got {special_bonus} extra tokens!")
                self.tokens += special_bonus
            if all(s == spin_result[0] for s in spin_result):
                win = symbol_value[spin_result[0]]*bet
                print(f"You won! You won {win} tokens!")
                self.tokens += win
                self.total_wins += 1
                self.check_bonus()
            else:
                print("You lost.")
                results.append(spin_result)
            self.total_games += 1
            print(f"You have {self.tokens} tokens.")
        return results
    
#Payout tokens    
    def payout_tokens(self):
        print(f"Payout: {self.tokens} Tokens")
        self.tokens = 0
        
#Show player statistics    
    def show_statistics(self):
        if self.total_games > 0:
            print(f"Total Games: {self.total_games}")
            print(f"Total Wins: {self.total_wins}")
            print(f"Win Percentage: {self.total_wins/self.total_games*100}%")
        else:
            print("Invalid input. Please try again.")
            
#Payout or continue Function
    def request_payout_or_continue(self):
        while True:
            choice = input("Would you like to payout or continue? P/C?\n  ").upper()
            if choice == "C":
                return True
            elif choice == "P":
                return False
            else:
                print("Invalid input. Please try again.")

# #Reading rules function                
    def reading_rules(self):
        while True:
            text = """Welcome to the Magical Token Machine. Here some rules?\n 
            1.You need to deposit the tokens.\n 
            2.You can bet on max.5 lines.\n 
            3.Winning condition: Three identical letters in a row!\n
            4.Wnning Condition Exmaple: A|A|A, B|B|B, C|C|C or D|D|D!\n
            5.SPEICAL BONUS: E Letter for extra tokens or get a rare extra spin!\n   
            Do you agree or disagree? A/D \n"""
            choice = input(text).upper()
            if choice == "A":
                return True
            elif choice == "D":
                return False
            else:
                print("Invalid input. Please try again.")
                
#Play the game        
    def play(self):
        if not self.reading_rules():
                print("Thank you for attention!")
                return 
            
        self.deposit_tokens()
        while True:
            bet = self.place_bet()
            lines = int(input(f"How many lines would you like to play? Max. {self.max_lines}\n "))
            if 1 <= lines <= self.max_lines:
                self.spin(bet, lines)
                if self.tokens <= 0:
                    print("You have no tokens left. Please deposit more tokens.")
                    break
                if not self.request_payout_or_continue():
                    print("Thank you for playing!")
                    self.show_statistics()
                    self.payout_tokens()
                    break
            else:
                    print(f"Invalid number of lines. You can set to 1 to {self.max_lines} lines.")
                           
if __name__ == '__main__':
    game = MagicMachine()
    game.play()