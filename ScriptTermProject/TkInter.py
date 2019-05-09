import tkinter
from tkinter import*

class Animals:
    def __init__(self):
        window = Tk()
        window.title("유기 동물 조회 서비스")

        frame1 = Frame(window)
        frame1.pack()
        self.v=IntVar()
        Label(frame1, text="검색옵션").grid(row=0, column=0,sticky="W")
        Radiobutton(frame1, text = "강아지", variable=self.v, value = 1).grid(row=1, column=0,sticky="W")
        Radiobutton(frame1, text = "고양이", variable = self.v, value = 1).grid(row=1, column=1,sticky="W")
        Radiobutton(frame1, text="전체", variable=self.v, value=1).grid(row=1, column=2,sticky="W")

        OPTIONS = [
            'Jan',
            'Feb',
            'March',
            'April'
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

        window.mainloop()


Animals()