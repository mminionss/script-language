import telepot
import time
from datetime import date, datetime, timedelta
from urllib.request import  urlopen
import http.client
from xml.etree import ElementTree


TOKEN = '844048060:AAE_TTyBWtDUo6S6NR7eokOMck318rMCKds'
bot = telepot.Bot(TOKEN)
print(bot.getMe())
bot.sendMessage(754334493,'Welcome!')


url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=o%2FSVIGlGjsaX3DTs%2FjBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0%2FIaZtF%2FkEUAhwAA%3D%3D'
response = urlopen(url).read()
print(response)
#텔레그램 연동, 포털이랑 연결 OK 이제 xml자료를 보내주기만 하면돼 !


# def check( user ):
#     conn = sqlite3.connect('users.db')
#     cursor = conn.cursor()
#     cursor.execute('CREATE TABLE IF NOT EXISTS users( user TEXT, location TEXT, PRIMARY KEY(user, location) )')
#     cursor.execute('SELECT * from users WHERE user="%s"' % user)
#     for data in cursor.fetchall():
#         row = 'id:' + str(data[0]) + ', location:' + data[1]
#         noti.sendMessage( user, row )
server = "openapi.animal.go.kr"
conn = None

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


def GetData():  # search에서 호출
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
        return extractData(req.read().decode('utf-8'))  # 잘 연결되었다면 extractData 호출
    else:
        print("Failed! Retry.")
        return None


def extractData(strXml):  # getData에서 호출
    tree = ElementTree.fromstring(strXml)
    # print(strXml)

    # 엘리먼트 가져오기
    itemElements = tree.getiterator("item")
    return itemElements

def SearchKind(keyword):  # 종 이름으로 검색
    botResponse=''
    for item in GetData():
        kindCd = item.find("kindCd")
        if (kindCd.text.find(keyword)) >= 0:  # 맞는 내용이 존재하면
           botResponse += kindCd.text + " " + item.find("age").text + " " + item.find("sexCd").text + " "+"\n"\
                          +"유기날짜 : " + item.find("happenDt").text+"\n"+"털 색 : " + item.find("colorCd").text + " "+"\n"\
                          +"특징 : " + item.find("specialMark").text+"\n"+"진행상태 : " + item.find("processState").text\
                          +"\n"+item.find("careNm").text+"\n"+item.find("careTel").text+"\n"+item.find("careAddr").text+"\n"+"\n"
    return botResponse

def SearchAddr(keyword):  # 주소 이름으로 검색
    botResponse=''
    for item in GetData():
        careAddr = item.find("careAddr")
        if (careAddr.text.find(keyword)) >= 0:  # 맞는 내용이 존재하면
           botResponse += item.find("kindCd").text + " " + item.find("age").text + " " + item.find("sexCd").text + " "+"\n"\
                          +"유기날짜 : " + item.find("happenDt").text+"\n"+"털 색 : " + item.find("colorCd").text + " "+"\n"\
                          +"특징 : " + item.find("specialMark").text+"\n"+"진행상태 : " + item.find("processState").text\
                          +"\n"+item.find("careNm").text+"\n"+item.find("careTel").text+"\n"+careAddr.text+"\n"+"\n"
    return botResponse

def SearchCenter(keyword):  # 보호소 이름으로 검색
    botResponse=''
    for item in GetData():
        careNm = item.find("careNm")
        if (careNm.text.find(keyword)) >= 0:  # 맞는 내용이 존재하면
           botResponse += item.find("kindCd").text + " " + item.find("age").text + " " + item.find("sexCd").text + " "+"\n"\
                          +"유기날짜 : " + item.find("happenDt").text+"\n"+"털 색 : " + item.find("colorCd").text + " "+"\n"\
                          +"특징 : " + item.find("specialMark").text+"\n"+"진행상태 : " + item.find("processState").text\
                          +"\n"+careNm.text+"\n"+item.find("careTel").text+"\n"+item.find("careAddr").text+"\n"+"\n"
    return botResponse

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        bot.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ') # 받은 메세지 텍스트를 분리한게 args
    if text.startswith('품종') and len(args)>1:
        print('try to 품종', args[1])
        bot.sendMessage(chat_id,'품종 '+args[1]+' 기준으로 검색 중...')
        botResponse=SearchKind(args[1])
        if botResponse:
            bot.sendMessage(chat_id,botResponse)
        else:
            bot.sendMessage(chat_id,"해당 품종이 없습니다 !")

    # replyAptData( '201801', chat_id, args[1] )
    elif text.startswith('주소') and len(args)>1:
        print('try to 주소', args[1])
        bot.sendMessage(chat_id, '주소 ' + args[1] + ' 기준으로 검색 중...')
        botResponse = SearchAddr(args[1])
        if botResponse:
            bot.sendMessage(chat_id, botResponse)
        else:
            bot.sendMessage(chat_id, "해당 주소가 없습니다 !")

    elif text.startswith('보호소') and len(args)>1:
        print('try to 보호소', args[1])
        bot.sendMessage(chat_id, '보호소 ' + args[1] + ' 기준으로 검색 중...')
        botResponse = SearchCenter(args[1])
        if botResponse:
            bot.sendMessage(chat_id, botResponse)
        else:
            bot.sendMessage(chat_id, "해당 이름의 보호소가 없습니다 !")

    elif text.startswith('help') and len(args)>1:
        bot.sendMessage(''' ========  명령어 예시  =======\n
        지역으로 검색 : 지역 부산\n
        품종으로 검색 : 품종 포메라니안\n
        보호소이름으로 검색 : 보호소 펫''')

    elif text.startswith('ok bye') and len(args)>1:
        bot.sendMessage('bye!')

    else:
        bot.sendMessage(chat_id, '''모르는 명령어입니다.\n 
        ========  명령어 예시  =======\n
        지역으로 검색 : 지역 부산\n
        품종으로 검색 : 품종 포메라니안\n
        보호소이름으로 검색 : 보호소 펫''')

today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', TOKEN)

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)