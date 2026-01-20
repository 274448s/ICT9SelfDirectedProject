# Calendar

import tkinter as tk
from tkinter import ttk
import os
import json
import time

script_path = os.path.dirname(__file__)
# Event JSON
print("Script dir: " + script_path)
if os.path.exists(script_path + r'\CalendarEvents.json'):
    print("file exists")
else:
    print("File created")