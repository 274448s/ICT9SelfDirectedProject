# Modules
import tkinter as tk
from tkinter import ttk
# Functions
def guiscienific():
    if scientific.get():
        root.geometry("900x600")
        NumberDisplay.config(width="900")
    else:
        root.geometry("280x473")
        NumberDisplay.config(width="400")
def switch():
    scientific.set(not scientific.get())
    guiscienific()

def inputchar(char):
    pass

# Root
root = tk.Tk()
# Variables
scientific = tk.BooleanVar(value=False)
NumberDisplayNumbers = tk.Variable(value="")
# GUI
root.title("Better Calculator")
rootframe = ttk.Frame(root, padding=(3, 3, 12, 12))
root.resizable(False,False)
togglescientific = ttk.Button(root, text="Scientific Mode",command=switch, width='900')
togglescientific.pack()
NumberDisplay = ttk.Label(root, text="0", width="900")
NumberDisplay.config(font=("Arial", 60))
NumberDisplay.pack()
guiscienific()

# Layout for Numpad
btns_frame = ttk.Frame(root)
btns_frame.pack(side="left", fill="y")
a_Board = [["CE", "Backspace", "=", ""], [7, 8, 9, "÷"], [4, 5, 6, "×"], [1, 2, 3, "+"], [".", 0, "-/+", "-"]]
for row in range(len(a_Board)):
    for col in range(len(a_Board[row])):
        i = a_Board[row][col]
        b = ttk.Button(btns_frame, text=str(i), command=lambda x=i: inputchar(x), width="10")
        b.grid(row=row + 1, column=col, ipady="20")

# Style
style = ttk.Style(root)

root.mainloop()