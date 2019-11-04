import tkinter as tk
from tkinter import filedialog
import percentCalc

_root = tk.Tk()
_txt_box = tk.Text(_root, height=3, width=30)
_choose_btn = tk.Button(_root, text='Choose a File', height=2, width=30, command=lambda: choose_file())
_calc_btn = tk.Button(_root, text="Calculate Whitespace", height=2, width=30,
                      command=lambda: percentCalc.calc(_root.filename))

def start_ui():
    _root.title("Whitespace Detector")
    _txt_box.insert(tk.END, "Please choose a file first")
    _txt_box.pack()
    _choose_btn.pack()
    _calc_btn.pack()
    # Causes window to stay open until close
    _root.mainloop()


def choose_file():
    # Opens file selection dialogue
    # Variable store the full path of the image
    _root.filename = filedialog.askopenfilename(initialdir="/",
                                             title="Select file",
                                             filetypes=(("jpeg files", "*.jpg"),
                                                        ("pdf files", "*.pdf"),
                                                        ("png files", "*.png"),
                                                        ("all files", "*.*"))
                                             )
    print(_root.filename)
    _txt_box.insert('1.0', ("File chosen: " + _root.filename))


def update_text(s):
    _txt_box.insert('1.0', s)

