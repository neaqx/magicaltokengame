# Welcome to the Magical Token Machhine. Start the game in the terminal. Run the code.

import random

symbols = ["A", "B", "C", "D"]
symbol_count = {"A":4, "B":5, "C":10, "D":12}
symbol_value = {"A":10, "B":5, "C":2, "D":1}

class MagicMachine:    
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
                    print(f"You have deposited {amount} tokens. Total: {self.tokens} tokens")
                    break
                else:
                    print("Please enter a positive number.")
            except ValueError:
                    print("Invalid input. Please enter a number.")

                
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
            self.total_games += 1
            print(f"You have {self.tokens} tokens.")
        return results
    
    def payout_tokens(self):
        print(f"Payout: {self.tokens} Tokens")
        self.tokens = 0
    
    def show_statistics(self):
     if self.total.games > 0:
        print(f"Total Games: {self.total_games}")
        print(f"Total Wins: {self.total_wins}")
        print(f"Win Percentage: {self.total_wins/self.total_games*100}%")
     else:
        print("Invalid input. Please try again.")
        
    
        
    def play(self):
        self.deposit_tokens()
        while True:
            bet = self.place_bet()
            while True:
                lines = int(input("How many lines would you like to play? Max. 5 "))
                if 1 <= lines <= self.max_lines:
                    break
                else:
                    print(f"Invalid number of lines. You can set to 1 to {self.max_lines} lines.")

            self.spin(bet, lines)

            if self.tokens <= 0:
                print("You have no tokens left. Please deposit more tokens.")
                break

        self.show_statistics()
        cont = input("Would you like to play again? Y/N ")
        if cont.lower() != "Y":
            sure = input("Are you sure? Y/N ")
            if sure.lower() == "N":
                print("Thank you for playing!")
                self.payout_tokens()
                return


if __name__ == '__main__':
    game = MagicMachine()
    game.play() 
         
