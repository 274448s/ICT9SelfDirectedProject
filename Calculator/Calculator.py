# Modules
import tkinter as tk
from tkinter import ttk
import Parser
# Functions
def inputchar(char):
    express = expres.get()
    print(express)
    if char in ["÷", "×", "+", "-"]:
        if char == express[-1] and num.get() == "":
            return
        else:
            expres.set(list(express) + [num.get()] + [char])
            num.set("")
            NumberDisplay.config(text=str(''.join(expres.get()) + num.get()))
    if char == "=":
        expres.set(list(express) + [num.get()])
        num.set(eval(''.join(expres.get())))
        expres.set([""])
    if str(char) in '9876543210':
        num.set(num.get() + str(char))
    if str(char) == "CE":
        num.set("")
        expres.set([""])
    NumberDisplay.config(text=str(''.join(expres.get()) + str(num.get())))

# Root
root = tk.Tk()
# Variables
scientific = tk.BooleanVar(value=False)
expres = tk.Variable(value=[""])
num = tk.Variable(value="")
# GUI
root.title("Better Calculator")
rootframe = ttk.Frame(root, padding=(3, 3, 12, 12))
root.resizable(False,False)
root.geometry("280x473")
NumberDisplay = ttk.Label(root, text="0", width="900")
NumberDisplay.config(font=("Arial", 60))
NumberDisplay.pack()

# Layout for Numpad
btns_frame = ttk.Frame(root)
btns_frame.pack(side="left", fill="y")
a_Board = [["CE", "Backspace", "=", "-/+"], [7, 8, 9, "÷"], [4, 5, 6, "×"], [1, 2, 3, "+"], [".", 0, "-/+", "-"]]
for row in range(len(a_Board)):
    for col in range(len(a_Board[row])):
        i = a_Board[row][col]
        b = ttk.Button(btns_frame, text=str(i), command=lambda x=i: inputchar(x), width="10")
        b.grid(row=row + 1, column=col, ipady="20")

# Style
style = ttk.Style(root)

root.mainloop()