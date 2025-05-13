# main.py

import tkinter as tk
from gui_components import ToDoApp

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
