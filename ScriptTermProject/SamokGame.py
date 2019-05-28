from tkinter import *
import tkinter.messagebox

class SamokGame:
    def pressed(self, Col):
        if not self.endgame: #trun ==true면 o차례
            if self.turn and self.buttonList[self.Row[Col] * 7 + Col]["text"] == " ":  # 0차례
                self.buttonList[self.Row[Col] * 7 + Col].configure(text="O", image=self.imageList[0])
                self.label.configure(text="X 차례")
                self.Row[Col] -= 1
                print(self.Row[Col])
            elif not self.turn and self.buttonList[self.Row[Col] * 7 + Col]["text"] == " ":  # x차례
                self.buttonList[self.Row[Col] * 7 + Col].configure(text="X", image=self.imageList[1])
                self.label.configure(text="O 차례")
                self.Row[Col] -= 1
                print(self.Row[Col])


            self.turn = not self.turn
            self.Check(Col)

    def Check(self,Col):
        self.CountX=0
        self.CountO=0
        for i in range(self.Row[Col],self.Row[Col]-7,-1):
            if self.buttonList[i*7+Col]["text"] == "O":
                self.CountO+=1
            elif self.buttonList[i*7+Col]["text"] == "X":
                self.CountX+=1
            if self.CountO == 4:
                tkinter.messagebox.askokcancel("END!","O WIN !")
                break
            elif self.CountX == 4:
                tkinter.messagebox.askokcancel("END!","X WIN !")
                break

    def __init__(self):
        window = Tk()
        self.turn = True
        self.imageList = []
        self.imageList.append(PhotoImage(file="o.gif"))  # 사진 경로
        self.imageList.append(PhotoImage(file="x.gif"))  # 사진 경로
        self.imageList.append(PhotoImage(file="empty.gif"))
        self.buttonList = []
        self.endgame = False
        frame1 = Frame(window)
        frame1.pack()
        for r in range(7):  # r=0,1,2
            for c in range(7):  # c=0,1,2
                self.buttonList.append(Button(frame1, text=" ", image=self.imageList[2],
                                              command=lambda Col=c: self.pressed(Col)))  # random
                self.buttonList[r * 7 + c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        self.label = Label(frame2, text="O 차례")
        self.label.pack()
        self.Row = [6 for i in range(7)]
        window.mainloop()


SamokGame()
