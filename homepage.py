from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self, text = "W ♾ RDLE", font=("Helvetica", 20),
            width=20).grid(row=0, column=1, columnspan = 1)
        self.person_ent = Entry(self)
        self.person_ent.grid(row = 1, column =1, sticky = W) 
        
root = Tk()
root.title("Homepage")
app = Application(root)
root.mainloop()


