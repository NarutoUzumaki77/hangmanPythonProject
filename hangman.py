'''
    Date: Sept 20, 2016
    Python Version: 2.7.10

'''

from Tkinter import *
from ttk import Frame, Button, Label, Style
from ttk import Entry
from random import randint
from tkMessageBox import *
import time

class Example(Frame):

    i = 0
    nn = 1
    chk = []

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):

        self.parent.title("Hang Man")
        self.pack(fill=BOTH, expand=True)

        ind = []
        text = []

        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)

        Style().configure("TButton", padding=(0, 10, 0, 10),
                          font='serif 10')

        WordMatrix = [
                      ['Z', 'I', 'G', 'Z', 'A', 'G'],
                      ['A', 'B', 'R', 'O', 'A', 'D'],
                      ['A', 'D', 'V', 'I', 'C', 'E'],
                      ['E', 'N', 'O', 'U', 'G', 'H'],
                      ['G', 'L', 'O', 'B', 'A', 'L'],
                      ['G', 'U', 'I', 'L', 'T', 'Y'],
                      ['F', 'I', 'S', 'C', 'A', 'L'],
                      ['F', 'O', 'U', 'R', 'T', 'H'],
                      ['L', 'U', 'C', 'E', 'N', 'T'],
                      ['M', 'A', 'R', 'I', 'N', 'E'],
                      ['R', 'E', 'P', 'O', 'R', 'T'],
                      ['U', 'N', 'I', 'T', 'E', 'D'],
                      ['W', 'R', 'I', 'T', 'E', 'R'],
                      ['B', 'E', 'A', 'U', 'T', 'Y'],
                      ['B', 'A', 'R', 'E', 'L', 'Y'],
                      ['F', 'O', 'R', 'M', 'A', 'T'],
                      ['M', 'Y', 'S', 'E', 'L', 'F'],
                      ['N', 'E', 'A', 'R', 'L', 'Y'],
                      ['S', 'I', 'M', 'P', 'L', 'Y'],
                      ]

        def helloCallBack(letter):
            if text.count(letter) >= 1:
                for nn, s in enumerate(text):
                    if s == letter:
                        dex = ind[nn]
                        break

                if self.guess1.cget("text") == '_' and dex==0:
                    self.guess1.config(text=letter)
                elif self.guess2.cget("text") == '_' and dex==1:
                    self.guess2.config(text=letter)
                elif self.guess3.cget("text") == '_' and dex==2:
                    self.guess3.config(text=letter)
                elif self.guess4.cget("text") == '_' and dex==3:
                    self.guess4.config(text=letter)
                elif self.guess5.cget("text") == '_' and dex==4:
                    self.guess5.config(text=letter)
                elif self.guess6.cget("text") == '_' and dex==5:
                    self.guess6.config(text=letter)
                self.chk.pop(0)
                if len(self.chk) <= 0:
                    showinfo('You Win', 'You Beat Hang Man')
                    reset()
            else:
                self.i += 1
                if self.i == 1:
                    firstTrial()
                elif self.i == 2:
                    secondTrial()
                elif self.i == 3:
                    thirdTrial()

        def wordSearch(q):
            word = []
            guess = []
            word = q[randint(0, len(q)-1)]
            print word
            i = 0
            while i < 3:
                index = randint(0, 5)
                for kk in guess:
                    if kk == index:
                        if index >= 5:
                            index -= 1
                        elif index <= 0:
                            index += 1
                guess.append(index)
                ind.append(index)
                i += 1
            self.guess1.config(text=word[0])
            self.guess2.config(text=word[1])
            self.guess3.config(text=word[2])
            self.guess4.config(text=word[3])
            self.guess5.config(text=word[4])
            self.guess6.config(text=word[5])
            guess.sort(key=int)
            ind.sort(key=int)
            print guess
            for ii in guess:
                text.append(word[ii])
            print text
            self.chk = list(text)

            for position in guess:
                if position == 0:
                    self.guess1.config(text='_')
                elif position == 1:
                    self.guess2.config(text='_')
                elif position == 2:
                    self.guess3.config(text='_')
                elif position == 3:
                    self.guess4.config(text='_')
                elif position == 4:
                    self.guess5.config(text='_')
                elif position == 5:
                    self.guess6.config(text='_')
            check = 0
            if self.guess1.cget('text') == '_':
                check += 1
            if self.guess2.cget('text') == '_':
                check += 1
            if self.guess3.cget('text') == '_':
                check += 1
            if self.guess4.cget('text') == '_':
                check += 1
            if self.guess5.cget('text') == '_':
                check += 1
            if self.guess6.cget('text') == '_':
                check += 1

            if check != 3:
                reset()
            return word

        def drawHangMan():
            self.entry.delete(1.0, 'end')
            self.entry.insert(END, "\n\t\t\t_______________") #Line 2
            self.entry.insert(END, "\n\t\t\t|")               #line 3
            self.entry.insert(END, "             |")          # 13 spaces, line 3
            self.entry.insert(END, "\n\t\t\t|")               #line4
            self.entry.insert(END, "\n\t\t\t|")               #line5
            self.entry.insert(END, "\n\t\t\t|")               #line6
            self.entry.insert(END, "\n\t\t\t|")               # line 7
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t-------------------")

        def firstTrial():
            self.entry.delete(1.0, 'end')
            self.entry.insert(END, "\n\t\t\t_______________") #Line 2
            self.entry.insert(END, "\n\t\t\t|")               #line 3
            self.entry.insert(END, "             |")          # 13 spaces, line 3
            self.entry.insert(END, "\n\t\t\t|")               #line4
            self.entry.insert(END, "             O")          # 13 spaces, line 4
            self.entry.insert(END, "\n\t\t\t|")               #line5
            self.entry.insert(END, "             |")          # 13 spaces, line 5
            self.entry.insert(END, "\n\t\t\t|")               #line6
            self.entry.insert(END, "\n\t\t\t|")               # line 7
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t-------------------")

        def secondTrial():
            self.entry.delete(1.0, 'end')
            self.entry.insert(END, "\n\t\t\t_______________")  # Line 2
            self.entry.insert(END, "\n\t\t\t|")  # line 3
            self.entry.insert(END, "             |")  # 13 spaces, line 3
            self.entry.insert(END, "\n\t\t\t|")  # line4
            self.entry.insert(END, "             O")  # 13 spaces, line 4
            self.entry.insert(END, "\n\t\t\t|")  # line5
            self.entry.insert(END, "             |")  # 13 spaces, line 5
            self.entry.insert(END, "\n\t\t\t|")  # line6
            self.entry.insert(END, "            /")  # 12 spaces, line 6
            self.entry.insert(END, "|")  # 0 space, line 6
            self.entry.insert(END, "\\")  # 0 space, line 6
            self.entry.insert(END, "\n\t\t\t|")  # line 7
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t-------------------")

        def thirdTrial():
            self.entry.delete(1.0, 'end')
            self.entry.insert(END, "\n\t\t\t_______________") #Line 2
            self.entry.insert(END, "\n\t\t\t|")               #line 3
            self.entry.insert(END, "             |")          # 13 spaces, line 3
            self.entry.insert(END, "\n\t\t\t|")               #line4
            self.entry.insert(END, "             O")          # 13 spaces, line 4
            self.entry.insert(END, "\n\t\t\t|")               #line5
            self.entry.insert(END, "             |")          # 13 spaces, line 5
            self.entry.insert(END, "\n\t\t\t|")               #line6
            self.entry.insert(END, "            /")           # 12 spaces, line 6
            self.entry.insert(END, "|")                       # 0 space, line 6
            self.entry.insert(END, "\\")                      # 0 space, line 6
            self.entry.insert(END, "\n\t\t\t|")               # line 7
            self.entry.insert(END, "            /")           # 12 spaces, line 7
            self.entry.insert(END, " \\")                     # 1 space, line 7
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t\t|")
            self.entry.insert(END, "\n\t\t-------------------")
            showinfo('Game Over', 'You Lost to Hang Man')
            reset()

        def reset():
            del text[:]
            del ind[:]
            self.i = 0
            self.nn = 0
            self.entry.delete(1.0, 'end')
            wordSearch(WordMatrix)
            drawHangMan()

        self.entry = Text(self)
        self.entry.grid(row=0, column=5, columnspan=6, rowspan=4, sticky=W + E)

        self.guess1 = Label(self, text='_', font='size, 40')
        self.guess1.grid(row=6, column=5, pady=10)
        self.guess2 = Label(self, text='_', font='size, 40')
        self.guess2.grid(row=6, column=6)
        self.guess3 = Label(self, text='_', font='size, 40')
        self.guess3.grid(row=6, column=7)
        self.guess4 = Label(self, text='_', font='size, 40')
        self.guess4.grid(row=6, column=8)
        self.guess5 = Label(self, text='_', font='size, 40')
        self.guess5.grid(row=6, column=9)
        self.guess6 = Label(self, text='_', font='size, 40')
        self.guess6.grid(row=6, column=10)
        reset()

        aButton = Button(self, text='A', command= lambda: helloCallBack('A')).grid(row=7, column=1)
        bButton = Button(self, text='B', command= lambda: helloCallBack('B')).grid(row=7, column=2)
        cButton = Button(self, text='C', command= lambda: helloCallBack('C')).grid(row=7, column=3)
        dButton = Button(self, text='D', command= lambda: helloCallBack('D')).grid(row=7, column=4)
        eButton = Button(self, text='E', command= lambda: helloCallBack('E')).grid(row=7, column=5)
        fButton = Button(self, text='F', command= lambda: helloCallBack('F')).grid(row=7, column=6)
        gButton = Button(self, text='G', command= lambda: helloCallBack('G')).grid(row=7, column=7)
        hButton = Button(self, text='H', command= lambda: helloCallBack('H')).grid(row=7, column=8)
        iButton = Button(self, text='I', command= lambda: helloCallBack('I')).grid(row=7, column=9)
        jButton = Button(self, text='J', command= lambda: helloCallBack('J')).grid(row=7, column=10)
        kButton = Button(self, text='K', command= lambda: helloCallBack('K')).grid(row=7, column=11)
        lButton = Button(self, text='L', command= lambda: helloCallBack('L')).grid(row=7, column=12)
        mButton = Button(self, text='M', command= lambda: helloCallBack('M')).grid(row=7, column=13)
        emptyspace = Label(self, text='      ').grid(row=7, column=14)
        newButton = Button(self, text='Reset', command=reset).grid(row=7, column=15)
        nButton = Button(self, text='N', command= lambda: helloCallBack('N')).grid(row=8, column=1)
        oButton = Button(self, text='O', command= lambda: helloCallBack('O')).grid(row=8, column=2)
        pButton = Button(self, text='P', command= lambda: helloCallBack('P')).grid(row=8, column=3)
        qButton = Button(self, text='Q', command= lambda: helloCallBack('Q')).grid(row=8, column=4)
        rButton = Button(self, text='R', command= lambda: helloCallBack('R')).grid(row=8, column=5)
        sButton = Button(self, text='S', command= lambda: helloCallBack('S')).grid(row=8, column=6)
        tButton = Button(self, text='T', command= lambda: helloCallBack('T')).grid(row=8, column=7)
        uButton = Button(self, text='U', command= lambda: helloCallBack('U')).grid(row=8, column=8)
        vButton = Button(self, text='V', command= lambda: helloCallBack('V')).grid(row=8, column=9)
        wButton = Button(self, text='W', command= lambda: helloCallBack('W')).grid(row=8, column=10)
        xButton = Button(self, text='X', command= lambda: helloCallBack('X')).grid(row=8, column=11)
        yButton = Button(self, text='Y', command= lambda: helloCallBack('Y')).grid(row=8, column=12)
        zButton = Button(self, text='Z', command= lambda: helloCallBack('Z')).grid(row=8, column=13)
        exitButton = Button(self, text='Quit', command=self.quit).grid(row=8, column=15)

        self.pack()

def main():

    root = Tk()
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()
