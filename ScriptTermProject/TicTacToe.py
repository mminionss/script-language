#TicTacToe
from tkinter import *

class TicTacToe:

    def pressed(self, Row, Col):
        if not self.endgame:
            if self.turn and self.buttonList[Row * 3 + Col]["text"] == " ":  # 0차례
                self.buttonList[Row * 3 + Col].configure(text="O", image=self.imageList[0])
                self.label.configure(text="X 차례")
            elif not self.turn and self.buttonList[Row * 3 + Col]["text"] == " ":  # x차례
                self.buttonList[Row * 3 + Col].configure(text="X", image=self.imageList[1])
                self.label.configure(text="O 차례")
            self.turn = not self.turn
            self.check()

    def check(self): #012 #345 #678 #036   #147 #258 #048 #246
        if self.buttonList[0]["text"] == self.buttonList[1]["text"] == self.buttonList[2]["text"]:
            if self.buttonList[0]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[3]["text"] == self.buttonList[4]["text"] == self.buttonList[5]["text"]:
            if self.buttonList[3]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[6]["text"] == self.buttonList[7]["text"] == self.buttonList[8]["text"]:
            if self.buttonList[6]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[0]["text"] == self.buttonList[3]["text"] == self.buttonList[6]["text"]:
            if self.buttonList[0]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[1]["text"] == self.buttonList[4]["text"] == self.buttonList[7]["text"]:
            if self.buttonList[1]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[2]["text"] == self.buttonList[5]["text"] == self.buttonList[8]["text"]:
            if self.buttonList[2]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[0]["text"] == self.buttonList[4]["text"] == self.buttonList[8]["text"]:
            if self.buttonList[0]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True
        if self.buttonList[2]["text"] == self.buttonList[4]["text"] == self.buttonList[6]["text"]:
            if self.buttonList[2]["text"] == "O":
                self.label.configure(text=" O 승리 ! 게임 끝 !")
                self.endgame = True
            elif self.buttonList[0]["text"] == "X":
                self.label.configure(text=" X 승리 ! 게임 끝 !")
                self.endgame = True

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
        for r in range(3):  # r=0,1,2
            for c in range(3):  # c=0,1,2
                self.buttonList.append(Button(frame1, text=" ", image=self.imageList[2],
                                              command=lambda Row=r, Col=c: self.pressed(Row, Col)))  # random
                self.buttonList[r * 3 + c].grid(row=r, column=c)
        frame2 = Frame(window)
        frame2.pack()
        self.label = Label(frame2, text="O 차례")
        self.label.pack()

        window.mainloop()


TicTacToe()
