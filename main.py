import tkinter as tk
import pyglet
from tkinter import font

window = tk.Tk()
window.title("SGA Trainer")

pyglet.font.add_file('sga.ttf')

def check_answer():
    print(prompt == text_field.get())
    if prompt == text_field.get():
        prompt_label.config(text="WOOHOO")

prompt = "the quick brown fox jumps over the lazy dog"

label = tk.Label(window, text="What does this say?", font=("", 16))
prompt_label = tk.Label(window, text=prompt, font=("Enchantment Proper", 16))
text_field = tk.Entry(window, width=64)
button = tk.Button(window, text="Submit", command=check_answer)

label.pack(pady=10, padx=10)
prompt_label.pack(pady=10, padx=10)
text_field.pack(pady=10, padx=10)
button.pack(pady=10)

window.mainloop()