import tkinter as tk
from tkinter import filedialog
from FaceDrawer2 import FaceDrawer

class GUI():
    def __init__(self, master):
        self.master = master
        master.title("Computer Vision Object Recognition")
        master['bg'] = "#49A"

        self.stack = []

        self.description = tk.Label(master, text = "Click the 'Select File' button and select an image file. \n Check the boxes for the objects you would like to detect and hit 'Run' \n "
                                                   "Note that some Cascades work better than others. Also red background plus check denotes a box being 'ticked'",
                        font="Consolas 12", bg = "#49A", fg = "white", justify = "center").grid(row = 0, column = 1)

        self.version = tk.Label(master, text = "Developed by Monsoon, version: 1.0", font = "Consolas 12", bg = "#49A", fg = 'white').grid(row = 10, column = 2, sticky = "E")

        self.fileExplorerButton = tk.Button(master, text = "Select File", command = self.fileExplorer).grid(row = 9, column = 1, sticky = "W")
        self.runButton = tk.Button(master, text = "Run", command = self.run).grid(row = 9, column = 2, sticky = "W")

        self.variables = [tk.StringVar() for i in range(15)]

        names = ["Eye", "Eye Tree Glasses", "Frontal Cat Face", "Frontal Cat Face Extended", "Frontal Face Alt",
                 "Frontal Face Alt Tree", "Frontal Face Alt 2", "Frontal Face Default", "Full Body",
                 "Left Eye (2 Splits)", "Right Eye (2 Splits)", "Lower Body", "Upper Body", "Profile Face", "Smiles"]

        for i in range(len(names)):
            self.tickBox(names[i], i, i%5 + 1, i%3)


    def fileExplorer(self):
        self.filepath = filedialog.askopenfilename(initialdir='C:/../Pictures',
                                                   title="Select an Image File")

        self.path = tk.Label(self.master, text=f"Selected path of File:%s" % str(self.filepath), font="Consolas 12",
                             bg="#49A", fg="white").grid(row=8, column=1, sticky = "E")

    def run(self):
        self.stack = []
        for i in self.variables:
            if i.get():
                print(i.get())
                self.stack.append(i.get())

        print(f"self stack: {self.stack}")

        if self.filepath:
            fd = FaceDrawer(self.filepath, self.stack)
            fd.drawFace()

    def tickBox(self, text, index, row, column):
        tk.Checkbutton(self.master, text = str(text), state = "normal", variable = self.variables[index], onvalue = text,  selectcolor = 'red', fg = "white" ,bg = '#49B').grid(row = row, column = column, sticky = "N")


root = tk.Tk()
window = GUI(root)
root.mainloop()