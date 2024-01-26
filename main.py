import tkinter as tk
import pyglet
from tkinter import font

window = tk.Tk()
window.title("SGA Trainer")

pyglet.font.add_file('sga.ttf')

def on_button_click():
    label.config(text="Hello, " + text_field.get())

label = tk.Label(window, text="What does this say?", font=("", 16))
prompt = tk.Label(window, text="the quick brown fox jumps over the lazy dog", font=("Enchantment Proper", 16))
text_field = tk.Entry(window)

label.pack(pady=10, padx=10)
prompt.pack(pady=10, padx=10)
text_field.pack(pady=10, padx=10)

window.mainloop()