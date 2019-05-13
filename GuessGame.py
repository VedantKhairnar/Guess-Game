from tkinter import *
import random
from tkinter import messagebox

class GuessGame:
    def protocolhandler(self):
        if messagebox.askyesno("Exit", "Really Wanna stop Guessing?"):
            if messagebox.askyesno("Exit", "Are you sure?"):
                self.root.destroy()

    def result(self):
        print (" You have ran out of guesses :( i was thinking of the number: ",self.n)
        lose = Label(self.root, text=" You have run out of chances :(\nand I was thinking of the number: "+str(self.n),bg='black',fg='cyan',font=5)
        lose.place(x = 140,y = 500)

    def check(self):
        print("Checking the number provided...")
        self.flag = 0
        self.turn += 1

        if self.flag == 0 and self.turn == 10:
            self.result()
            return

        print("Entered number is "+ str(self.m.get()))

        if self.m.get()<1 or self.m.get()>100:
            print("Invalid number..")
            self.invalid = Label(self.root, text="Invalid number entered..                    ",bg='black',fg='cyan',font=5)
            self.invalid.place(x = 140,y = 503)

        elif self.m.get()==self.n:
            print("Bravos,You guessed it right!!! in " +str(self.turn)+" turns")
            self.flag=1
            self.win = Label(self.root, text="Bravos,You guessed it right!!! in " +str(self.turn)+" turns",bg='black',fg='cyan',font=5)
            self.win.place(x=130,y=503)

        elif self.m.get()<self.n:
            print ("Too low! You have ",10-self.turn, "guesses left!")
            self.less = Label(self.root, text="Too low! You have "+str(10-self.turn)+ " guesses left!",bg='black',fg='cyan',font=5)
            self.less.place(x=135,y=503)

        elif self.m.get()>self.n:
            print ("Too high! You have ",10-self.turn, "guesses left!")
            self.more = Label(self.root, text="Too high! You have "+str(10-self.turn)+ " guesses left!",bg='black',fg='cyan',font=5)
            self.more.place(x=135,y=503)
        else:
            print("There's some problem!!!")
            self.root.destroy()

    def __init__(self):
        self.root = Tk()
        self.root.geometry('800x600')
        self.root.config(bg='black')
        self.root.title('Guess Game')
        self.m = IntVar()
        self.status = ""
        self.flag = 0
        self.turn=0
        self.n = random.randint(1,101)

   #     self.root.protocol("WM_DELETE_WINDOW", self.protocolhandler)

        photo = PhotoImage(file="pythonlogoneonf.png")
        label = Label(self.root, image=photo,border=0)
        label.place(x=300, y=300)

        self.win = Label(self.root, text="Bravos,You guessed it right!!! in " +str(self.turn)+" turns",bg='black',fg='cyan')
        self.more = Label(self.root, text="Too high! You have "+str(10-self.turn)+ "guesses left!",bg='black',fg='cyan')
        self.less = Label(self.root, text="Too low! You have "+str(10-self.turn)+ "guesses left!",bg='black',fg='cyan')
        self.invalid = Label(self.root, text="Invalid number entered..                    ",bg='black',fg='cyan')

        status = Label(self.root,text = "Status: ",bg='black',fg='cyan')
        status.config(font=("magneto", 20))
        status.place(x=17,y=495)

        title_g = Label(self.root, text="G",bg='black',fg='cyan')
       # title_g.config(font=("mexicanero", 50))
        title_g.config(font=("prometheus", 80))
        title_g.place(x=250,y=70)

        title_1 = Label(self.root, text="uess",fg='cyan',bg='black')
        title_1.config(font=("prometheus", 38))
        title_1.place(x=350,y=70)

        title_2 = Label(self.root, text="ame",fg='cyan',bg='black')
        title_2.config(font=("prometheus", 38))
        title_2.place(x=370,y=125)

        instructions = Label(self.root, text="Instruction: I am thinking of a number from 1-100..\nGuess it with the directions I'll provide.\nYou have 10 chances in total\nGood Luck\n:)",bg='black',fg='cyan')
        instructions.config(font=("calibri", 13))
        instructions.place(x=220,y=350)

        guess = Label(self.root, text="Enter Your Guess here:",bg='black',fg='cyan')
        guess.config(font=("fragmentcore", 13))
        guess.place(x=23,y=290)

        self.entry = Entry(self.root,textvariable=self.m,bg='black',fg='cyan')
        self.entry.place(x=205,y=293)

        button_push = Button(self.root, text="Check",bd=4,bg='black',fg='cyan', command=self.check)
        button_push.place(x=350,y=285)

        self.root.mainloop()

s = GuessGame()

