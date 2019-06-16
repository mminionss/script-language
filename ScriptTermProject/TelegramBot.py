import telepot
bot = telepot.Bot('823805594:AAEmzhqP7MwvMp39Cq64SNYWejz6oSPWQ2w')
print(bot.getMe())

from urllib.request import  urlopen
url = 'http://openapi.animal.go.kr/openapi/service/rest/abandonmentPublicSrvc/abandonmentPublic?serviceKey=o%2FSVIGlGjsaX3DTs%2FjBgQH92mEtQTi9EpyoiRoR7RQe8VyfgwwFz8jKmS26J90tsGuVa6T0%2FIaZtF%2FkEUAhwAA%3D%3D'
response = urlopen(url).read()
print(response)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id,"난 텍스트 이외의 메세지는 처리하지 못해요.")
        