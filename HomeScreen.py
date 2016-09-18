import tkinter as tk
from tkinter import filedialog
import File
import time
#import tkFileDialog

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__()
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        #tk.Entry(app).grid()
#        tk.grid(row=1,column =0)
        self.stmt = tk.Text(self,height=1, width =20)
        self.stmt.pack(side="left")
        self.hi_there = tk.Button(self)#.grid(row=0, column =0)
        #self.stmt["text"] = "Test"
        self.hi_there["text"] = "Browse"
        self.hi_there["command"] = self.fileop
        self.hi_there.pack(side="right")

        self.stmtocc = tk.Text(self,height = 10, width =50)
        self.stmtocc.pack(side="bottom")

        self.quit = tk.Button(self, text="QUIT", command=root.destroy)
        self.quit.pack(side="bottom")

    def fileop(self):
        start = time.time()
        file_name = filedialog.askopenfilename(initialdir = "F:/python",title ="Choose file",filetype=[('Text files', '*.txt'), ('All files', '*')])#
        if '.txt' in file_name and   File.checkSize(file_name):
            lineocc_count, wordocc_count = File.line(file_name)
            self.stmtocc.config(state= 'normal')
            self.stmtocc.delete(0.0,10.0)
            self.stmt.delete(0.0,2.0)
            self.stmt.insert(1.0,file_name)
            for x, y in lineocc_count.items():
                self.stmtocc.insert(1.0,x," ::: ",y,"\n")
            self.stmtocc.config(state= 'disable')
            #print(lineocc_count)
        else:
            print("file is not present or of size more than 2mb")

        print("Exicution time ",time.time()-start)

        #print("hi there, everyone!")
start = time.time()
root = tk.Tk()
root.geometry("500x500")
#tk.Entry(root).grid()
app = Application(master=root)
app.mainloop()
end = time.time()
#print("Exicution time",end-start)
