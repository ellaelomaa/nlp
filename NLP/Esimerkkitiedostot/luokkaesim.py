import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.username = "tahmatassu"

        frame_main = ttk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)

        btn_show_username = ttk.Button(frame_main, 
                                       text="Show username",
                                       command=self.show_username)
        
        btn_show_username.pack(padx=10, pady=10)
    
    def show_username(self):
        username_window = UsernameWindow(self, 
                                         username=self.username)

class UsernameWindow(tk.Toplevel):
    def __init__(self, parent, username): # incoming
        """
        Super().__init__ is outgoing to the class constructor, e.g. tk.Toplevel.
        DON'T put your own parameters here - like username - as tk.Toplevel doesn't
        know what to do with them. It only needs to know the parent.
        """
        super().__init__(parent) 
        self.username = username

        self.frame_main = ttk.Frame(self)
        self.frame_main.pack(fill=tk.BOTH, expand=True)

        label_username = ttk.Label(self.frame_main,
                                   text=f"My username is:  {self.username}")

        label_username.pack(padx=50, pady=50)

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.mainloop()