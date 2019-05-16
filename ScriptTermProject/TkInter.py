import tkinter
from tkinter import*
from tkinter import Tk, Label, PhotoImage


class Animals:
    def __init__(self):
        window = tkinter.Tk()
        window.title("유기 동물 조회 서비스")
        window.resizable(False, False)

        frame1 = Frame(window)
        frame1.pack()
        self.v=IntVar()
        Label(frame1, text="검색옵션").grid(row=0, column=0,sticky="W")
        Radiobutton(frame1, text = "강아지", variable=self.v, value = 1).grid(row=1, column=0,sticky="W")
        Radiobutton(frame1, text = "고양이", variable = self.v, value = 2).grid(row=1, column=1,sticky="W")
        Radiobutton(frame1, text="전체", variable=self.v, value=3).grid(row=1, column=2,sticky="W")

        OPTIONS = [
            '전체',
            '서울',
            '인천',
            '경기'
        ]  # etc

        variable = StringVar(window)
        variable.set(OPTIONS[0])  # default value

        w = OptionMenu(frame1, variable, *OPTIONS)
        w.grid(row=2, column=0,sticky="W")
        frame2 = Frame(window)
        frame2.pack()
        e1=Entry(frame2)
        e1.pack(side=LEFT)
        b1=Button(frame2,text="검색")
        b1.pack(side=LEFT)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="정렬").grid(row=0, column=0, sticky="W")
        b2 = Button(frame3, text="날짜순")
        b2.grid(row=0, column=1,sticky="E")
        b3 = Button(frame3, text="지역순")
        b3.grid(row=0, column=2, sticky="E")

        frame7 = Frame(window)
        frame7.pack()
        scrollbar = tkinter.Scrollbar(frame7)
        scrollbar.pack(side="right", fill="y")
        listbox = tkinter.Listbox(frame7, yscrollcommand=scrollbar.set)

        listbox.pack(side="left")
        scrollbar["command"] = listbox.yview

        frame4 = Frame(window)
        frame4.pack()
        b4 = Button(frame4, text="이메일")
        b4.grid(row=0, column=1, sticky="E")
        b5 = Button(frame4, text="☆")
        b5.grid(row=0, column=5, sticky="E")

        frame5 = Frame(window)
        frame5.pack()
        b6 = Button(frame5, text="보호소 위치보기")
        b6.grid(row=0, column=3, sticky="E")

        imgObj = PhotoImage(file="ex.gif")

        imgLabel = Label(window)
        imgLabel.config(image=imgObj)
        imgLabel.pack()


        window.mainloop()




Animals()

