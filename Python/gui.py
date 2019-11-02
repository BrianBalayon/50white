import tkinter as tk
from tkinter import filedialog

# Starts
root = tk.Tk()

root.title = "Whitespace Detector"

# Opens file selection dialogue
# Variable store the full path of the image
root.filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select file",
                                        filetypes = (("jpeg files","*.jpg"),
                                                     ("pdf files","*.pdf"),
                                                     ("png files","*.png"),
                                                     ("all files","*.*"))
                                        )
print(root.filename)
# button = tk.Button(r, text='Stop', width=25, command=r.destroy)
# button.pack()

# Causes window to stay open until cose
root.mainloop()