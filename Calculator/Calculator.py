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
def cmd(i) -> None:
    if i == "CE":
        NumberDisplayNumbers.set("")
        NumberDisplay.config(text="0")
        pass
    else:
        new = NumberDisplayNumbers.get() + (str(i))
        NumberDisplayNumbers.set(new)
    NumberDisplay.config(text=NumberDisplayNumbers.get())

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
NumberDisplay.config(font=("Arial", 80))
NumberDisplay.pack()
guiscienific()

# Layout for Numpad
btns_frame = ttk.Frame(root)
btns_frame.pack()
a_Board = [[9, 8, 7, "CE"], [6, 5, 4, ""], [3, 2, 1], [".", 0, "-/+"]]
for row in range(len(a_Board)):
    for col in range(len(a_Board[row])):
        i = a_Board[row][col]
        b = ttk.Button(btns_frame, text=str(i), command=lambda x=i: cmd(x), width="10")
        b.grid(row=row + 1, column=col)

# Style
style = ttk.Style(root)

root.mainloop()