# Copyright (c) 2024 Logan Dhillon

import tkinter as tk
from tkextrafont import Font
import words, sys

def check_answer():
    if prompt.cget("text") == text_field.get():
        regen_prompt()
        score.config(text=score.cget("text") + 1)
        
def regen_prompt():
    prompt.config(text=word_list.pick(3))

word_list = words.WordList(words.DEFAULT)

# init window first so `tkextrafont` doesn't freak out
window = tk.Tk()
window.title("SGA Trainer")

# init SGA font
sga_font = Font(file="resources/sga.ttf", family="Enchantment Proper")
if sys.argv[1] == "--debug":
    sga_font = ("", 16)

# tkinter element stuff
score = tk.Label(window, text=0)
prompt = tk.Label(window, text=word_list.pick(3), font=sga_font)
text_field = tk.Entry(window, width=64)

score.pack()
tk.Label(window, text="What does this say?", font=("", 16)).pack(pady=10, padx=10)
prompt.pack(pady=10, padx=10)
text_field.pack(pady=10, padx=10)
tk.Button(window, text="Submit", command=check_answer).pack(pady=10)
tk.Button(window, text="Give Up", command=regen_prompt).pack(pady=10)

window.mainloop()