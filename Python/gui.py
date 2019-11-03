import tkinter as tk
from tkinter import filedialog
import percentCalc


def start_ui():
    root = tk.Tk()
    root.title = "Whitespace Detector"
    choose_btn = tk.Button(root, text='Choose File', command=choose_file(root))
    choose_btn.pack()
    # calc_btn = tk.Button(root, text="Calculate Whitespace", command=percentCalc.calc(root.filename))
    # calc_btn.pack()

    # Causes window to stay open until close
    root.mainloop()


def choose_file(ui):
    # Opens file selection dialogue
    # Variable store the full path of the image
    ui.filename = filedialog.askopenfilename(initialdir="/",
                                             title="Select file",
                                             filetypes=(("jpeg files", "*.jpg"),
                                                        ("pdf files", "*.pdf"),
                                                        ("png files", "*.png"),
                                                        ("all files", "*.*"))
                                             )