# Copyright (c) 2024 Logan Dhillon

import tkinter as tk
from tkextrafont import Font
import words, sys

# init window first so `tkextrafont` doesn't freak out
window = tk.Tk()
window.title("SGA Trainer")

# word list stuff
selected_word_list = tk.StringVar(window)
selected_word_list.set("Default")
word_list = words.WordList(words.word_lists[selected_word_list.get()])

word_count = 3

# actions run from GUI
def set_word_count():
    global word_count
    print(f"Updating word count from {word_count} to {int(word_count_spinbox.get())}")
    word_count = int(word_count_spinbox.get())
    
def update_word_list(value):
    global word_list
    word_list = words.WordList(words.word_lists[value])

def check_answer(event):
    if prompt.cget("text") == text_field.get():
        regen_prompt()
        score.config(text=score.cget("text") + 1)
        
def regen_prompt():
    prompt.config(text=word_list.pick(word_count))
    text_field.delete(0, tk.END)

# init SGA font
sga_font = Font(file="resources/sga.ttf", family="Enchantment Proper")
if len(sys.argv) > 1 and sys.argv[1] == "--debug":
    sga_font = ("", 16)

# init tkinter elements
score = tk.Label(window, text=0, font=("", 14))
prompt = tk.Label(window, text=word_list.pick(word_count), font=sga_font)

text_field = tk.Entry(window, width=64)
text_field.bind("<KeyRelease>", check_answer)

word_count_spinbox = tk.Spinbox(window, from_=1, to=20, value=word_count, width=5, command=set_word_count)

# place tkinter elements
tk.Label(window, text="Score").place(x=10, y=10)
score.place(x=10, y=30)

tk.Label(window, text="Word Count").place(relx=1.0, x=-10, y=10, anchor="ne")
word_count_spinbox.place(relx=1.0, x=-10, y=32, anchor="ne")

tk.Label(window, text="What does this say?", font=("", 16)).pack(pady=20)
prompt.pack(padx=10)

text_field.pack(pady=(30, 0), padx=20)
tk.Button(window, text="Give Up", command=regen_prompt).pack(pady=10)

tk.OptionMenu(window, selected_word_list, *words.word_lists, command=update_word_list).pack()

window.mainloop()