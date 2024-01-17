#Welcome to the Magical Token Machhine. Start the game in the terminal. 

import random

MAX_TOKENS = 10000
MAX_SPIN = 5

symbols = ["A", "B", "C", "D"]
symbols_count = {"A":4, "B":5, "C":10, "D":12}
symbols_value = {"A":10, "B":5, "C":2, "D":1}


class magicMachine:
    
    def __init__(self):
        self.tokens = 0
        self.total_games = 0
        self.total_wins = 0
        
    def deposit_tokens(self):
        while True:
            try:
                