# Modules
import tkinter as tk
from tkinter import ttk
# Functions
def guiscienific():
    if scientific.get():
        root.geometry("900x600")
    else:
        root.geometry("400x600")
def switch():
    scientific.set(not scientific.get())
    guiscienific()

# Root
root = tk.Tk()
# Variables
scientific = tk.BooleanVar(value=False)
# GUI
root.title("Better Calculator")
rootframe = ttk.Frame(root, padding=(3, 3, 12, 12))
root.resizable(False,False)
togglescientific = ttk.Button(root, command=switch)
togglescientific.pack()
guiscienific()

# Style
style = ttk.Style(root)

root.mainloop()