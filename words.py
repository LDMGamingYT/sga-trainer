import random

DEFAULT = "words/default.txt"
SHORT = "words/short.txt"
MEDIUM = "words/medium.txt"
LONG = "words/long.txt"

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
