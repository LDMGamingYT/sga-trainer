# Copyright (c) 2024 Logan Dhillon

import random

DEFAULT = "resources/words/default.txt"
SHORT = "resources/words/short.txt"
MEDIUM = "resources/words/medium.txt"
LONG = "resources/words/long.txt"

word_lists = {
    "Default": "resources/words/default.txt", 
    "Short": "resources/words/short.txt", 
    "Medium": "resources/words/medium.txt", 
    "Long": "resources/words/long.txt"
}

class WordList:
    def __init__(self, filename: str):
        with open(filename, 'r') as file:
            self.lines = file.readlines()
            self.lines = [line.strip() for line in self.lines]
        
    
    def pick(self, amount: int = 1) -> str:
        """
        Assemble sentence with `amount` amount of words, defaults to 1
        """
        out = ""
        for _ in range(amount):
            out += random.choice(self.lines) + " "
        return out.strip()
