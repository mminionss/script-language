import telepot
bot = telepot.Bot('823805594:AAEmzhqP7MwvMp39Cq64SNYWejz6oSPWQ2w')
print(bot.getMe())

from urllib.request import  urlopen
url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?serviceKey=sea100UMmw23Xycs33F1EQnumONR%2F9ElxBLzkilU9Yr1oT4TrCot8Y2p0jyuJP72x9rG9D8CN5yuEs6AS2sAiw%3D%3D&LAWD_CD=11110&DEAL_YMD=201712'
response = urlopen(url).read()
print(response)

