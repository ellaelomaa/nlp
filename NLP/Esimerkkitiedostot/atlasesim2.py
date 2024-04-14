import tkinter as tk
from tkinter import ttk


def create_segment(parent, label_text, button_text):
    frame = ttk.Frame(master=parent)

    # grid layout
    frame.rowconfigure(0, weight=1)
    frame.columnconfigure((0, 1, 2), weight=1, uniform="a")

    # widgets
    ttk.Label(frame, text=label_text).grid(row=0, column=0, sticky="nsew")
    ttk.Button(frame, text=button_text).grid(row=0, column=1, sticky="nsew")

    return frame


class Segment(ttk.Frame):
    def __init__(self, parent, label_text, button_text, exercise_text):
        super().__init__(master=parent)

        # grid layout
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1, uniform="a")
        ttk.Label(self, text=label_text).grid(row=0, column=0, sticky="nsew")
        ttk.Button(self, text=button_text).grid(row=0, column=1, sticky="nsew")
        self.box(exercise_text).grid(row=0, column=2, sticky="nsew")

        self.pack(expand=True, fill="both", padx=10, pady=10)

    def box(self, text):
        frame = ttk.Frame(master=self)
        ttk.Entry(frame).pack(expand=True, fill="both")
        ttk.Button(frame, text=text).pack(expand=True, fill="both")

        return frame


window = tk.Tk()
window.title("Atlas")
window.geometry("400x600")

# widgets
Segment(window, "label", "button", "test")
Segment(window, "label2", "button2", "test2")
Segment(window, "label3", "button3", "test3")
Segment(window, "label4", "button4", "test4")
Segment(window, "label5", "button5", "test5")

# create_segment(window, "label", "button").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label2", "button2").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label3", "button3").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label4", "button4").pack(expand=True, fill="both", padx=10, pady=10)
# create_segment(window, "label5", "button5").pack(expand=True, fill="both", padx=10, pady=10)

window.mainloop()
