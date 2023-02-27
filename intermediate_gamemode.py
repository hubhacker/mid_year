from tkinter import *
import random

class Intermediate(Frame):

    def __init__(self, master):

        super(Intermediate, self).__init__(master)
        #self.place()
        self.create_widgets()
        self.file = ("midyear_5letterwords.txt")

    def choose_word(self, file): 

        fiveletter = open(file)

        self.fiveletterlist = []

        for word in fiveletter:
            self.fiveletterlist.append(word.strip())

        self.intword = self.fiveletterlist([random.randint(0, 1000)])

    
    def create_widgets(self):

        root.geometry("400x600")
        #root.maxsize(400, 600)
        root.config(bg = "#F8EDEB") # I'LL CHANGE BG LATER

        self.frame = Frame(root, width = 400, height = 600, bg = "#F9DCC4") # I'LL CHANGE BG LATER
        self.frame.place(x = 0, y = 0)

        Label(self.frame, text = "INTERMEDIATE MODE", font=("Consolas", 13), bg = "pink").place(relx = 0.5, rely = 0.05, anchor = N) # vivian i will change the color later, i can't rn bc i have no wifi

        rel_x = 0.1
        rel_y = 0.14
        for i in range(1,6):
            self.letter1 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
            self.letter1.place(relx = rel_x, rely = rel_y, anchor = N)

            self.letter2 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
            self.letter2.place(relx = rel_x * 3, rely = rel_y, anchor = N)
            self.letter3 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
            self.letter3.place(relx = rel_x * 5, rely = rel_y, anchor = N)
            self.letter4 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
            self.letter4.place(relx = rel_x *7, rely = rel_y, anchor = N)
            self.letter5 = Text(self.frame, width = 4, height = 2.4, font = ("Consolas"), bg = "#F8EDEB") # I'LL CHANGE BG LATER
            self.letter5.place(relx = rel_x * 9, rely = rel_y, anchor = N)

            rel_y += 0.14
        
    def guess_ent(self):
        pass
        
    def check_guess(self): # callback function
        
        guess = self.guess_ent.get()
        
        while guess != self.intword:
            pass
        
        word_single = []
        for i in guess:
            word_single.append(i)
        letter = Label[i] = i
        
        self.delete(0.0, END)
        self.letter1.insert(0.0, letter)

root = Tk() 
root.title("Intermediate Mode")
app = Intermediate(root)
root.mainloop()