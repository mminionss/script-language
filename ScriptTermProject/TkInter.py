#-*- coding: utf-8 -*-

import tkinter
from tkinter import *
from tkinter import Tk, Label, PhotoImage
import http.client
import urllib
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree

server = "openapi.animal.go.kr"
conn = None

def InitRenderText():
    global RenderText

def userURIBuilder(uri, **user):
    str = uri + "?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str

def connectServer():
    global conn, server
    conn = http.client.HTTPConnection(server)
    conn.set_debuglevel(1)

def getData():
    global server, conn
    if conn == None:
        connectServer()
    # 정보 가져올 url 생성
    # http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?
    # serviceKey=o%2FSVIGlGjsaX3DTs%2FjBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0%2FIaZtF%2FkEUAhwAA%3D%3D
    # &bgnde=20140601
    # &endde=20140630
    # &upkind=417000
    # &pageNo=1
    # &numOfRows=10
    # &neuter_yn=Y
    uri = userURIBuilder("/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic",
                         servicekey="o%2FSVIGlGjsaX3DTs%2FjBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0%2FIaZtF%2FkEUAhwAA%3D%3D",
                         bgnde="20140601", endde="20190501", upkind="417000", pageNo="1", numOfRows="10", neuter_yn="Y",
                         upr_cd="",org_cd="",care_reg_no="",state="")
    conn.request("GET", uri, None)
    req = conn.getresponse()
    print(req.status) #200
    if int(req.status) == 200:
        print("Data Downloading complete ! ")
        print(req.read().decode('utf-8')) #여기서 에러.
        #return extractData(req.read())
    else:
        print("Failed! Retry.")
        return None

def extractData(strXml):
    pass
    #tree = ElementTree.fromstring(strXml)
    #print(strXml)

    #엘리먼트 가져오기
    # itemElements = tree.getiterator("items")
    # #print(itemElements)
    # for item in itemElements:
    #     age = item.find("age")
    #     careAddr = item.find("careAddr")
    #     print(careAddr)
    #     if len(careAddr.text)>0:
    #         return {"age":age.text, "title":careAddr.text}


def SearchAge(keyword):
    pass

class Animals:

    def __init__(self):
        window = tkinter.Tk()
        window.title("유기 동물 조회 서비스")
        window.resizable(False, False)

        frame1 = Frame(window)
        frame1.pack()
        self.v = IntVar()
        Label(frame1, text="검색옵션").grid(row=0, column=0, sticky="W")
        Radiobutton(frame1, text="강아지", variable=self.v, value=1).grid(row=1, column=0, sticky="W")
        Radiobutton(frame1, text="고양이", variable=self.v, value=2).grid(row=1, column=1, sticky="W")
        Radiobutton(frame1, text="전체", variable=self.v, value=3).grid(row=1, column=2, sticky="W")

        OPTIONS = [
            '전체',
            '서울',
            '인천',
            '경기'
        ]  # etc

        variable = StringVar(window)
        variable.set(OPTIONS[0])  # default value

        w = OptionMenu(frame1, variable, *OPTIONS)
        w.grid(row=2, column=0, sticky="W")
        frame2 = Frame(window)
        frame2.pack()
        e1 = Entry(frame2)
        e1.pack(side=LEFT)
        b1 = Button(frame2, text="검색")
        b1.pack(side=LEFT)

        frame3 = Frame(window)
        frame3.pack()
        Label(frame3, text="정렬").grid(row=0, column=0, sticky="W")
        b2 = Button(frame3, text="날짜순")
        b2.grid(row=0, column=1, sticky="E")
        b3 = Button(frame3, text="지역순")
        b3.grid(row=0, column=2, sticky="E")

        frame7 = Frame(window)
        frame7.pack()
        scrollbar = tkinter.Scrollbar(frame7)
        scrollbar.pack(side="right", fill="y")
        listbox = tkinter.Listbox(frame7, yscrollcommand=scrollbar.set)

        # 리스트 박스
        listbox.pack(side="left")
        scrollbar["command"] = listbox.yview

        imgObj = PhotoImage(file="ex.gif")
        imgLabel = Label(window)
        imgLabel.config(image=imgObj)
        imgLabel.pack(side="left")

        frame4 = Frame(window)
        frame4.pack(side="left")
        b4 = Button(frame4, text="이메일")
        b4.grid(row=0, column=1, sticky="E")

        b5 = Button(frame4, text="☆")
        b5.grid(row=0, column=5, sticky="E")

        b6 = Button(frame4, text="보호소 위치보기")
        b6.grid(row=0, column=3, sticky="E")

        window.mainloop()


getData()
Animals()
