# Welcome to the Magical Token Machhine. Start the game in the terminal.
# Run the code.

import random

symbols = ["A", "B", "C", "D" "E"]
symbol_count = {"A": 4, "B": 10, "C": 14, "D": 12, "E": 1}
symbol_value = {"A": 10, "B": 5, "C": 2, "D": 1, "E": 0}


class MagicMachine:
    def __init__(self):
        self.tokens = 0
        self.total_games = 0
        self.total_wins = 0
        self.max_lines = 5
        self.free_spins = 0

    def deposit_tokens(self):
        while True:
            try:
                deposit_text = """
Welcome to the Magical Token Machine.
How many tokens would you like to deposit?\n
                """
                amount = int(input(deposit_text + '\n'))
                if amount > 0:
                    self.tokens += amount
                    print(f"""\nYou have deposited {amount} tokens.
                    You now have {self.tokens} tokens.\n""")
                    break
                else:
                    print("\nPlease enter a positive number.\n")
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
# Deposit tokens to play

    def check_bonus(self):
        if random.randint(1, 10) == 1:
            bonus_spins = random.randint(1, 5)
            print(f"\nYou have won {bonus_spins} free spins!\n")
            self.free_spins += bonus_spins
# Check if player gets bonus spins

    def place_bet(self):
        while True:
            try:
                bet_text = """
How many tokens would you like to bet?
"""
                bet = int(input(bet_text + '\n'))
                if 0 < bet <= self.tokens:
                    print(f"""\n{bet} Tokens have been bet.
                    You now have {self.tokens - bet} tokens.\n""")
                    return bet
                else:
                    print("""\nInvalid bet.
                    Please bet a number between 1
                    and your total token amount.\n""")
            except ValueError:
                print("\nInvalid bet. Please bet a number\n")
# Place bet and check if bet is valid

    def spin(self, bet, lines):
        if self.free_spins > 0:
            print(f"You have {self.free_spins} free spins left.")
            self.free_spins -= 1
        else:
            if self.tokens < bet:
                print(f"""{bet} tokens have been bet.
                You now have {self.tokens} tokens.""")
                return
            self.tokens -= bet
            print(f"""{bet} tokens have been bet.
            You now have {self.tokens} tokens.""")
            print("You have spun the machine!")
        results = []
        for _ in range(lines):
            spin_result = [random.choice(symbols)for _ in range(3)]
            print(" | ".join(spin_result))
            if "E" in spin_result:
                special_bonus = random.randint(1, 100)
                print(f"""\nSpecial symbol E appeared!
                You got {special_bonus} extra tokens!\n""")
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
# Spin the machine and check if player gets bonus tokens

    def payout_tokens(self):
        print(f"Payout: {self.tokens} Tokens")
        self.tokens = 0
# Payout tokens

    def show_statistics(self):
        if self.total_games > 0:
            print(f"Total Games: {self.total_games}")
            print(f"Total Wins: {self.total_wins}")
            print(f"Win Percentage: {self.total_wins/self.total_games*100}%")
        else:
            print("Invalid input. Please try again.")
# Show player statistics

    def request_payout_or_continue(self):
        while True:
            payout_text = """Would you like to payout or continue? P/C?\n"""
            choice = input(payout_text).upper()
            if choice == "C":
                return True
            elif choice == "P":
                return False
            else:
                print("Invalid input. Please try again.")
# Payout or continue Function

    def reading_rules(self):

        while True:
            rules = """
Welcome to the Magical Token Machine. Here some rules?
1.You need to deposit the tokens.
2.You can bet on max.5 lines.
3.Winning condition: Three identical letters in a row!
4.Wnning Condition Exmaple: A|A|A, B|B|B, C|C|C or D|D|D!
5.SPEICAL BONUS: E Letter for extra tokens or get a rare extra spin!
Do you agree or disagree? A/D
"""
            choice = input(rules + '\n').upper()
            if choice == "A":
                return True
            elif choice == "D":
                return False
            else:
                print("Invalid input. Please try again.")
# Reading rules function

    def play(self):
        if not self.reading_rules():
            print("Thank you for attention!")
            return
        self.deposit_tokens()
        while True:
            bet = self.place_bet()
            lines = int(input(f"""\nHow many lines would you like to play?
            Max. {self.max_lines}\n"""))
            if 1 <= lines <= self.max_lines:
                self.spin(bet, lines)
                if self.tokens <= 0:
                    print("""You have no tokens left.
                    Please deposit more tokens.""")
                    break
                if not self.request_payout_or_continue():
                    print("Thank you for playing!")
                    self.show_statistics()
                    self.payout_tokens()
                    break
            else:
                print(f"""\nInvalid number of lines.
                    You can set to 1 to {self.max_lines} lines.\n""")
# Play the game

if __name__ == '__main__':
    game = MagicMachine()
    game.play()