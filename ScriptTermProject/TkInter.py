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
kindNm="417000"

def getData(): # search에서 호출
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
                         bgnde="20140601", endde="20190501", upkind=kindNm, pageNo="1", numOfRows="481", neuter_yn="Y",
                         upr_cd="",org_cd="",care_reg_no="",state="")
    conn.request("GET", uri, None)
    req = conn.getresponse()
    print(req.status) #200
    if int(req.status) == 200:
        print("Data Downloading complete ! ")
        #print(req.read().decode('utf-8')) #여기서 에러.->고침
        return extractData(req.read().decode('utf-8')) #잘 연결되었다면 extractData 호출
    else:
        print("Failed! Retry.")
        return None

def extractData(strXml): #getData에서 호출
    tree = ElementTree.fromstring(strXml)
    #print(strXml)

    #엘리먼트 가져오기
    itemElements = tree.getiterator("item")
    return itemElements

#주소, 보호소이름, 보호소 전화번호, 동물 정보(나이, 종, 털 색깔, 성별, 특징, 상태)
#종+나이+성별, 털색깔+특징 ,상태, 보호소 이름, 전화번호, 주소
def Search(keyword): #검색버튼을 눌렀을 때 실행
    #검색 옵션이 강아지일 경우

    #검색 키워드가 주소일 경우
    SearchAddr(keyword)
    #검색 키워드가 종 이름 #아이디어노트: tkInter 탭하나 만들어서 종 이름 쭈루룩 출력해서 참고가능하게.
    #SearchKind(keyword)
    #검색 키워드가 보호소 이름
    #SearchCenter(keyword)

global searchlist
searchlist=[]

def SearchAddr(keyword): #주소로 검색
    for item in getData():
        careAddr = item.find("careAddr")
        if (careAddr.text.find(keyword)) >= 0:  # 내용이 존재하면
            searchlist.append((item.find("kindCd").text +" "+ item.find("age").text +" "+ item.find("sexCd").text+" ",
                               "털 색 : "+item.find("colorCd").text +" ",
                               "특징 : "+ item.find("specialMark").text,
                               "진행상태 : " + item.find("processState").text,
                               item.find("careNm").text,
                               item.find("careTel").text,
                               careAddr.text,
                               item.find("filename").text))
    PrintList()

def SearchCenter(keyword): #센터 이름으로 검색
    searchlist=[]
    for item in getData():
        careNm = item.find("careNm")
        if (careNm.text.find(keyword)) >= 0:  # 내용이 존재하면
            searchlist.append(careNm.text)
    return searchlist

def SearchKind(keyword): #종 이름으로 검색
    searchlist=[]
    for item in getData():
        kindCd = item.find("kindCd")
        if (kindCd.text.find(keyword)) >= 0:  # 내용이 존재하면
            searchlist.append(kindCd.text)
    return searchlist

def PrintList(): #리스트에 추가된 데이터를 출력

    #만약 정렬 버튼을 눌렀다면
    SortList()
    #화면에 출력해보기
    for i in range(len(searchlist)):
        for j in range(7):
            print(searchlist[i][j])
        print()

def SortList():
    searchlist.sort(reverse=True)

global selection

class Animals:
    def GetSelection(self):

        selectionlist = list(self.listbox.curselection()) # 튜플 형식으로 반환해줌
        selection = selectionlist[0]
        print(selection) #선택 값이 안들어와
        # assert len(selection)==1
        # z = selection[0]
        # if z=='0':
        #     print('0')

        # filename = searchlist[selection][7]
        # return filename
        self.GetImage(selection)

    def GetImage(self,selection):
        filename = searchlist[selection][7]

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


    def __init__(self):
        window = tkinter.Tk()
        window.title("유기 동물 조회 서비스")
        window.geometry("400x600")
        window.resizable(False, False)

        self.v=IntVar()
        l1=Label(window, text="검색옵션").place(x=60,y=0)
        Radiobutton(window, text = "강아지", variable=self.v, value = 1).place(x=120,y=0)
        Radiobutton(window, text = "고양이", variable = self.v, value = 2).place(x=180,y=0)
        Radiobutton(window, text="전체", variable=self.v, value=3).place(x=240,y=0)

        OPTIONS = [
            '주소',
            '품종',
            '보호소 이름'
        ]  # etc

        variable = StringVar(window)
        variable.set(OPTIONS[0])  # default value
        w = OptionMenu(window, variable, *OPTIONS)
        w.place(x=100,y=25)

        #검색 엔트리
        e1 = Entry(window)
        e1.place(x=100,y=60)
        b1=Button(window,text="검색")
        b1.place(x=250,y=60)

        Label(window, text="정렬").place(x=110,y=90)
        b2 = Button(window, text="날짜순")
        b2.place(x=150,y=90)
        b3 = Button(window, text="지역순")
        b3.place(x=200,y=90)

        #리스트박스
        frame7 = Frame(window)
        frame7.place(x=10,y=120)
        scrollbar = tkinter.Scrollbar(frame7)
        scrollbar.pack(side="right", fill="y")
        self.listbox = tkinter.Listbox(frame7, yscrollcommand=scrollbar.set,width='50',selectmode='SINGLE')
        self.listbox.pack(side="left")
        scrollbar["command"] = self.listbox.yview
        # 리스트 박스에 출력
        for i in range(len(searchlist)):
            self.listbox.insert(0,searchlist[i][0]+"\n"+searchlist[i][1]+"\n"+searchlist[i][2]+"\n"+searchlist[i][3]+"\n"+searchlist[i][4]+"\n"+searchlist[i][5]+"\n"+searchlist[i][6])


        #상세정보 버튼 추가
        #만약 버튼을 눌렀다면 --> command = GetSelection
        buttonInfo = Button(window,text="상세정보",command=self.GetSelection)
        buttonInfo.place(x=300,y=290)

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

        photo = ImageTk.PhotoImage(file="ex.gif")
        self.imgLabel = Label(window,image=photo)
        self.imgLabel.place(x=10,y=310)

        frame4 = Frame(window)
        frame4.place(x=150,y=360)
        b4 = Button(window, text="이메일")
        b4.place(x=210,y=360)

        b5 = Button(window, text="☆")
        b5.place(x=360,y=360)

        b6 = Button(window, text="보호소 위치보기")
        b6.place(x=260,y=360)

        window.mainloop()

Search('인천') #Entry.get(Animals().e1) 해서 가져올 예정
Animals()
