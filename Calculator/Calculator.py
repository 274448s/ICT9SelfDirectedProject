# Modules
import tkinter as tk
from tkinter import ttk

# GUI
root = tk.Tk()
root.title("Better Calculator")
rootframe = ttk.Frame(root, padding=(3, 3, 12, 12))
root.geometry("400x600")
root.resizable(False,False)
# Style
style = ttk.Style(root)

root.mainloop()