import tkinter as tk
from tkinter import filedialog
import File
#import tkFileDialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        tk.grid(row=1,column =0)
        self.hi_there = tk.Button(self).grid(row=0, column =0)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="yellow",
                              command=root.destroy)
        self.quit.pack(side="top")

    def say_hi(self):
        file_name = filedialog.askopenfilename(initialdir = "F:/python",title ="Choose file",filetype=[('Text files', '*.txt'), ('All files', '*')])#
        if '.txt' in file_name and   File.checkSize(file_name):
            File.line(file_name)
        else:
            print("file is not present or of size more than 2mb")

        #print("hi there, everyone!")

root = tk.Tk()
root.geometry("500x500")
app = Application(master=root)
app.mainloop()
