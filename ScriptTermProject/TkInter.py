#-*- coding: utf-8 -*-

import tkinter
from tkinter import *
#from tkinter import Tk, Label, PhotoImage
import http.client
import requests
import urllib
from xml.dom.minidom import parse, parseString
from xml.etree import ElementTree
from PIL import ImageTk
from tkinter import ttk
import folium
import webbrowser

server = "openapi.animal.go.kr"
conn = None
global searchOption

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

global kindNm

kindNm="417000"


global selection

class Animals:
    def getData(self):  # search에서 호출
        global server, conn, kindNm
        if conn == None:
            connectServer()
        # 정보 가져올 url 생성
        # http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?
        # serviceKey=o%2FSVIGlGjsaX3DTs%2FjBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0%2FIaZtF%2FkEUAhwAA%3D%3D
        # &bgnde=20140601
        # &endde=20140630
        # &upkind=417000 고양이 =422400
        # &pageNo=1
        # &numOfRows=10
        # &neuter_yn=Y
        uri = userURIBuilder("/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic",
                             serviceKey="o/SVIGlGjsaX3DTs/jBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0/IaZtF/kEUAhwAA==",
                             bgnde="20140601", endde="20190501", upkind=kindNm, pageNo="1", numOfRows="481",
                             neuter_yn="Y",
                             upr_cd="", org_cd="", care_reg_no="", state="")
        conn.request("GET", uri, None)
        req = conn.getresponse()
        print(req.status)  # 200
        if int(req.status) == 200:
            print("Data Downloading complete ! ")
            # print(req.read().decode('utf-8')) #여기서 에러.->고침
            return self.extractData(req.read().decode('utf-8'))  # 잘 연결되었다면 extractData 호출
        else:
            print("Failed! Retry.")
            return None

    def extractData(self, strXml):  # getData에서 호출
        tree = ElementTree.fromstring(strXml)
        # print(strXml)

        # 엘리먼트 가져오기
        itemElements = tree.getiterator("item")
        return itemElements

    # 주소, 보호소이름, 보호소 전화번호, 동물 정보(나이, 종, 털 색깔, 성별, 특징, 상태)
    # 종+나이+성별, 털색깔+특징 ,상태, 보호소 이름, 전화번호, 주소
    def Search(self):  # 검색버튼을 눌렀을 때 실행
        self.searchlist.clear()

        self.GetRadio()
        keyword = Entry.get(self.searchEntry)
        print(keyword)
        # 검색 키워드가 주소일 경우
        if self.variable.get() == "주소":
            self.SearchAddr(keyword)

        # 검색 키워드가 종 이름 #아이디어노트: tkInter 탭하나 만들어서 종 이름 쭈루룩 출력해서 참고가능하게.
        if self.variable.get() == "품종":
            self.SearchKind(keyword)
        # 검색 키워드가 보호소 이름
        if self.variable.get() == "보호소 이름":
            self.SearchCenter(keyword)

    def SearchAddr(self,keyword):  # 주소로 검색
        for item in self.getData():
            careAddr = item.find("careAddr")
            if (careAddr.text.find(keyword)) >= 0:  # 내용이 존재하면
                self.searchlist.append(
                    (item.find("kindCd").text + " " + item.find("age").text + " " + item.find("sexCd").text + " ",
                     "유기날짜 : " + item.find("happenDt").text,
                     "털 색 : " + item.find("colorCd").text + " ",
                     "특징 : " + item.find("specialMark").text,
                     "진행상태 : " + item.find("processState").text,
                     item.find("careNm").text,
                     item.find("careTel").text,
                     careAddr.text,
                     item.find("filename").text))
        self.PrintList()

    def SearchCenter(self,keyword):  # 센터 이름으로 검색
        for item in self.getData():
            careNm = item.find("careNm")
            if (careNm.text.find(keyword)) >= 0:  # 내용이 존재하면
                self.searchlist.append(
                    (item.find("kindCd").text + " " + item.find("age").text + " " + item.find("sexCd").text + " ",
                     "유기날짜 : " + item.find("happenDt").text,
                     "털 색 : " + item.find("colorCd").text + " ",
                     "특징 : " + item.find("specialMark").text,
                     "진행상태 : " + item.find("processState").text,
                     careNm.text,
                     item.find("careTel").text,
                     item.find("careAddr").text,
                     item.find("filename").text))
        self.PrintList()

    def SearchKind(self,keyword):  # 종 이름으로 검색
        for item in self.getData():
            kindCd = item.find("kindCd")
            if (kindCd.text.find(keyword)) >= 0:  # 내용이 존재하면
                self.searchlist.append(
                    (kindCd.text + " " + item.find("age").text + " " + item.find("sexCd").text + " ",
                     "유기날짜 : " + item.find("happenDt").text,
                     "털 색 : " + item.find("colorCd").text + " ",
                     "특징 : " + item.find("specialMark").text,
                     "진행상태 : " + item.find("processState").text,
                     item.find("careNm").text,
                     item.find("careTel").text,
                     item.find("careAddr").text,
                     item.find("filename").text))
        self.PrintList()

    def PrintList(self):  # 리스트에 추가된 데이터를 출력
        self.listbox.delete(0, 'end')
        # # 화면에 출력해보기
        # for i in range(len(self.searchlist)):
        #     for j in range(8):
        #         print(self.searchlist[i][j])
        #     print()
        # 리스트 박스에 출력
        for i in range(len(self.searchlist)-1,-1,-1):
            # self.listbox.insert(0, self.searchlist[i][0] + "\n" + self.searchlist[i][1] + "\n" + self.searchlist[i][2] + "\n" +self.searchlist[i][3] + "\n" +
            #                     self.searchlist[i][4] + "\n" + self.searchlist[i][5] + "\n" + self.searchlist[i][6] + "\n" + self.searchlist[i][7])
            self.listbox.insert(0, self.searchlist[i][0] + "\n" + self.searchlist[i][1] + "\n")

    def PrintInfo(self):
        self.infoLabel.forget() #내용 싹 지우고 다시 출력
        infoString=""
        for i in range(7):  # 메일은 전체 내용 출력
            infoString += self.searchlist[self.selection][i] + "\n"
        self.infoLabel.config(text=infoString)

    def SortDate(self):
        self.searchlist = sorted(self.searchlist, key=lambda date:self.searchlist[1])
        self.PrintList()

    def SortName(self):#가나다 내림차순

        self.PrintList()
        self.searchlist.sort(reverse=False)

    def SortNameReverse(self):

        self.PrintList()
        self.searchlist.sort(reverse=True)

    def GetSelection(self): #상세정보 눌렀을 때
        selectionlist = list(self.listbox.curselection()) # 튜플 형식으로 반환해줌
        self.selection = selectionlist[0]
        print(self.selection) #선택 값이 안들어와
        # assert len(selection)==1
        # z = selection[0]
        # if z=='0':
        #     print('0')

        # filename = searchlist[selection][7]
        # return filename
        self.GetImage()
        self.PrintInfo()

    def GetRadio(self):
        global kindNm
        if self.v.get() == 1:
            kindNm = "417000"
        elif self.v.get() == 2:
            kindNm = "422400"
        elif self.v.get() == 3:
            kindNm = "429900"

    def GetImage(self):
        filename = self.searchlist[self.selection][8]

        # load library
        import urllib.request
        from PIL import ImageTk
        import os

        # image url to download
        url = filename

        # file path and file name to download
        outpath = "C:/Users/tiuri/Documents/GitHub/script-language/ScriptTermProject/"
        outfile = "test.jpg"

        # # Create when directory does not exist
        # if not os.path.isdir(outpath):
        #     os.makedirs(outpath)

        # download
        urllib.request.urlretrieve(url, outpath + outfile)
        print("complete!")

        img = ImageTk.PhotoImage(file=outfile)
        self.imgLabel.configure(image=img)
        self.imgLabel.image = img

    def SendMail(self):
        # selectionlist = list(self.listbox.curselection())  # 튜플 형식으로 반환해줌
        # selection = selectionlist[0]
        searchstring=""
        for i in range(7): #메일은 전체 내용 출력
            searchstring += self.searchlist[self.selection][i] + "\n"
        import smtplib
        from email.mime.text import MIMEText

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login('jinsy2098@gmail.com', 'dapfiukbpfiiilcm')

        msg = MIMEText(searchstring)
        msg['Subject'] = '유기동물 상세정보 조회 !'

        s.sendmail("jinsy2098@gmail.com", "tiurit12@naver.com", msg.as_string())

        s.quit()

    def FindRocation(self):
        # 위도 경도 지정
        # 한국동물구조관리협회 37.870134, 126.983358
        map_osm = folium.Map(location=[37.870134, 126.983358], zoom_start=16)
        # 마커 지정
        folium.Marker([37.870134, 126.983358]).add_to(map_osm)
        # html 파일로 저장
        map_osm.save('osm.html')

        webbrowser.open("osm.html")
    def __init__(self):
        window = tkinter.Tk()
        window.title("유기 동물 조회 서비스")
        window.geometry("400x600")
        window.resizable(False, False)
        self.searchlist = []
        # 노트북으로 탭 만들기
        notebook = ttk.Notebook(window, width=400, height=600)
        notebook.place(x=0, y=0)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)
        tab3 = Frame(notebook)
        notebook.add(tab1, text="검색")     #메인
        notebook.add(tab2, text="즐겨찾기") #즐찾 즐겨찾기 한거 메일로 보내기 즐찾리스트, 메일 주소 입력 엔트리, 메일 보내기 버튼
        notebook.add(tab3, text="통계")     # 강아지 품종 통계 그래프, 날짜 통계 그래프

        self.v=IntVar()
        Label(tab1, text="검색옵션").place(x=60,y=20)
        Radiobutton(tab1, text = "강아지", variable=self.v, value = 1).place(x=120,y=20)
        Radiobutton(tab1, text = "고양이", variable = self.v, value = 2).place(x=180,y=20)
        Radiobutton(tab1, text="기타", variable=self.v, value=3).place(x=240,y=20)

        #롤다운 리스트
        OPTIONS = [
            '주소',
            '품종',
            '보호소 이름'
        ]  # etc

        self.variable = StringVar(tab1)
        self.variable.set(OPTIONS[0])  # default value
        optionMenu = OptionMenu(tab1, self.variable, *OPTIONS)
        optionMenu.place(x=50,y=55)

        #검색 엔트리
        self.searchEntry = Entry(tab1)
        self.searchEntry.place(x=135, y=60)
        searchButton=Button(tab1,text="검색",command=self.Search)
        searchButton.place(x=285,y=55)

        Label(tab1, text="정렬").place(x=110,y=95)
        # sortDate = Button(window, text="날짜순",command=self.SortDate)
        # sortDate.place(x=65,y=90)
        sortName = Button(tab1, text="이름순(내림차순)",command=self.SortName)
        sortName.place(x=150,y=95)
        sortNameReverse = Button(tab1, text="이름순(오름차순)", command=self.SortNameReverse)
        sortNameReverse.place(x=260, y=95)

        #리스트박스
        frame7 = Frame(tab1)
        frame7.place(x=10,y=120)
        scrollbar = tkinter.Scrollbar(frame7)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tkinter.Listbox(frame7, yscrollcommand=scrollbar.set,width='50',selectmode='SINGLE')
        self.listbox.pack(side="left")
        scrollbar["command"] = self.listbox.yview

        #상세정보 버튼 추가
        #만약 버튼을 눌렀다면 --> command = GetSelection
        buttonInfo = Button(tab1,text="상세정보",command=self.GetSelection)
        buttonInfo.place(x=20,y=300)

        #버튼 클릭->GetSelection -> GetImage

        #이미지 uri -> 파일로 저장하는 코드
            #

        #

        # global imgfile
        # import os
        # image_url = self.GetImageUrl()
        # image = requests.get(image_url).content
        # filename = os.path.basename(image_url)
        # with open(filename,'wb') as f:
        #     f.write(image)

        #상세정보 출력
        self.infoLabel = tkinter.Label(tab1, width=30, height=10, relief="groove",text="")
        self.infoLabel.place(x=20, y=340)

        # 사진
        photo = ImageTk.PhotoImage(file="grapes.gif")
        self.imgLabel = Label(tab1, image=photo)
        self.imgLabel.place(x=250, y=360)

        #하단 버튼
        emailButton = Button(tab2, text="이메일", command=self.SendMail)
        emailButton.place(x=100, y=300)
        rocationButton = Button(tab1, text="보호소 위치보기",command=self.FindRocation)
        rocationButton.place(x=100, y=300)
        starButton = Button(tab1, text="☆")
        starButton.place(x=210,y=300)




        #frame4.place(x=150, y=360)





        window.mainloop()

Animals()
