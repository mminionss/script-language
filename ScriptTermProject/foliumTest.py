# #-*- coding: utf-8 -*-
#
import folium
import webbrowser
import requests
# import googlemaps
# import geocoder
# #
# # gmaps = googlemaps.client(key=)
# # geo = geocoder.google()
# # geo.l
# # 누리동물병원
# # 부산동물보호센터
# # 청조동물병원
# # 열린동물병원
# # 러브펫종합동물병원
# # 강동리본센터(reborn)
# # 강현림동물병원
# # 남산동물병원
# # 홍익동물병원
# # 한국동물구조관리협회
# # 고양시동물보호센터
# # 인천수의사회
# # 진천동물병원
# # 남양유기견보호센터
# # 한국야생동물보호협회
# # (사)한동보
# # 평택시유기동물보호소
# # 24시아이동물메디컬
# # 정동물병원
# # 광주동물보호소
# # 창원유기동물보호소
# # 자인동물보호소
# # 군산유기동물보호소
# # 박영재동물병원
# # 버디종합동물병원
# # 가나동물병원
# # 신영재동물병원
# # 청도동물보호소
#
# # 위도 경도 지정
# #한국동물구조관리협회 37.870134, 126.983358
# #
# # url='https://maps.googleapis.com/maps/api/geocode/json'
# # find_loc = '러브펫 동물병원'
# #
# # params = {'sensor':'false','address':find_loc}
# # r=requests.get(url,params=params)
# # results = r.json()['results']
# # location = results[0]['geometry']['location']
# # print(location['lat'])
# # import geocoder
# # location='러브 펫 동물병원'
# # g = geocoder.google('Mountain View,CA')
# # print(g.geojson)
#
# #부산
# # ['부산광역시 해운대구 송정2로13번길 46 (송정동) ', 35.194865,129.2057445
# # '부산광역시 해운대구 송정2로13번길 46 (송정동) 누리동물병원', 35.194865,129.2057445
# # '부산광역시 해운대구 송정동 81-5', 35.196526,129.2055535
# # '부산광역시 연제구 온천천남로 4 (연산동) ', 없음
# # '부산광역시 강서구 군라2길 206 (대저2동) 부산동물보호센터'] 35.1345653,128.9260548
#
# #서울
# # ['서울특별시 용산구 원효로2가 84-10', 37.535611, 126.961741
# # '서울특별시 관악구 남부순환로 1429 (신림동) ', 37.481147, 126.909561
# # '서울특별시 양천구 목동  657번지 16호', 37.544404,126.8622975
# # '서울특별시 용산구 후암동 244-60', 37.548395,126.9774505
# # '서울특별시 강동구 양재대로81길 73 (성내동) 강동구 유기동물 분양센터(reborn)', 37.5238281,127.1297011
# # '서울특별시 마포구 합정동 411-18'] 37.548032,126.9178165
#
# #인천
# # ['인천광역시 계양구 다남동 35-8', 37.566203, 126.719625
# # '인천광역시 계양구 장제로 923 (병방동) ', 37.548974, 126.743818
# # '인천광역시 중구 개항로 68 (경동) ', 37.472388, 126.634506
# # '인천광역시 부평구 부평동 431-15', 37.503273, 126.722079
# # '인천광역시 서구 가정동 517-32', 37.515592, 126.672966
# # '인천광역시 강화군 강화읍 강화대로 217 (강화읍, 린나이보일러) ', 37.740640, 126.504749
# # '인천광역시 계양구 다남로165번길 56 (다남동, 유기동물보호소) '] 37.566201, 126.719637
#
# #경기
# ['경기도 양주시 남면 감악산로 63-37 ',
# '경기도 고양시 덕양구 고양대로 1695 (원흥동, 고양시 농업기술센터) 고양시동물보호센터',
# '경기도 양주시 남면 감악산로 63-37 (남면) ',
# '경기도 양주시 남면 상수리 410-1',
# '경기도 화성시 남양읍 화성로 1483-27 (남양읍) ',
# '경기도 안산시 상록구 청곡길 50 (부곡동) 한국야생동물보호협회',
# '경기도 안산시 상록구 청곡길 50 (부곡동) 안산시 상록구 부곡동 231-5',
# '경기도 평택시 진위면 야막길 108-86 (진위면) ',
# '경기도 부천시 오정구 원종동 229-8',
# '경기도 수원시 팔달구 인계동 1135-7',
# '경기도 파주시 문산읍 문산역로 77 버디종합동물병원',
# '경기도 부천시 중동로 57 (송내동, 상가동) 117호',
# '경기도 안산시 상록구 청곡길 50 (부곡동) ',
# '경기도 양주시 남면 감악산로 63-37 (남면) 한국동물구조관리협회',
# '경기도 오산시 성호대로 36 (오산동) ',
# '경기도 수원시 영통구 인계로220번길 20 (매탄동) ',
# '경기도 수원시 팔달구 매산로3가 효원로 53 (매산로3가) ',
# '경기도 용인시 처인구 모현면 대지로 407 (모현면)  ',
# '경기도 성남시 분당구 불정로 266 (수내동, 유신제일조합) ',
# '경기도 수원시 팔달구 일월로22번길 15 (화서동) ',
# '경기도 여주시 능서면 능서공원길 34 (능서면) ',
# '경기도 군포시 산본동 213번지 9호 외 1필지 2층',
# '경기도 수원시 영통구 봉영로 1623 (영통동, 드림피아빌딩) 124호',
# '경기도 수원시 영통구 영통동 986-7',
# '경기도 수원시 팔달구 매교동 141-5',
# '경기도 수원시 장안구 영화동 127-39',
# '경기도 파주시 문산읍 방촌로 1636 (문산읍, 강산설렁탕) ',
# '경기도 수원시 팔달구 중부대로42번길 9 (인계동) 한성동물병원',
# '경기도 화성시 우정읍 3.1만세로 29 (우정읍) ',
# '경기도 수원시 권선구 서수원로577번길 341 (금곡동, 수원모아미래도센트럴타운1단지) 상가동 1층 B127호',
# '경기도 안성시 봉남동 326-2',
# '경기도 부천시 소향로 246 (중동, 새롬프라자6차) ',
# '경기도 수원시 장안구 정자동 874-2 롯데프라자 206호',
# '경기도 남양주시 금곡로 44 (금곡동, 성원빌딩) 1층',
# '경기도 파주시 중앙로 241 (금촌동, 한샘파주키친프라자) 행복한동물병원']
#
# rocationList=[0]
# def FindRocation(rocationList):
#     #rocationList=[35.1345653,128.9260548]
#     map_osm = folium.Map (location = rocationList,zoom_start=16)
#     # 마커 지정
#     folium.Marker(rocationList).add_to(map_osm)
#     # html 파일로 저장
#     map_osm.save('osm.html')
#
#     webbrowser.open("osm.html")

global rocationDic
rocationDic = {'부산광역시 강서구 군라2길 206 (대저2동) 부산동물보호센터': [35.1345653, 128.9260548],
                          '부산광역시 해운대구 송정2로13번길 46 (송정동) 누리동물병원': [35.194865, 129.2057445],
                          '부산광역시 해운대구 송정2로13번길 46 (송정동) ': [35.194865, 129.2057445]}

#
# from tkinter import *
# import folium
#
# import geocoder
#
# ''' This program can only geocode cities in the United States
#
#
#
#     Makes a HTML document in the same directory as this script
#
#
#
# '''
#
# basemaps = ["OpenStreetMap", "MapQuest Open", "MapQuest Open Aerial",
#
#             "Mapbox Bright", "Mapbox Control Room", "CartoDB dark_matter",
#
#             "CartoDB positron", "Stamen Terrain", "Stamen Toner",
#
#             "Stamen Watercolor"]
#
# states = ["AL",
#
#           "AK",
#
#           "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
#
#           "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
#
#           "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
#
#           "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
#
#           "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
#
# master = Tk()
#
# master.title("Make me a Map!")
#
# Label(master, text="Pick a map").grid(row=0)
#
# Label(master, text="City").grid(row=1)
#
# Label(master, text="State").grid(row=2)
#
# # e1 = Entry(master)
#
# userCity = Entry(master)
#
# # e1.grid(row=0, column=1)
#
# userCity.grid(row=1, column=1)
#
# var1 = StringVar(master)
#
# var1.set(basemaps[8])  # initial value
#
# # option1 = apply(OptionMenu, (master, var1) + tuple(basemaps))
# #
# # option1.grid(row=0, column=1)
#
# var2 = StringVar(master)
#
# var2.set(states[0])  # initial value
#
# # option2 = apply(OptionMenu, (master, var2) + tuple(states))
# #
# # option2.grid(row=2, column=1)
#
#
# #
#
# # test stuff
#
#
# def makeMap(city, state, basemap):
#     userPlace = city + ", " + state
#
#     g = geocoder.google(userPlace)
#
#     x = g.lat
#
#     y = g.lng
#
#     xxx = geocoder.google([x, y], method='reverse')
#
#     cityName = xxx.city
#
#     mappy = folium.Map(location=[x, y],
#
#                        tiles=basemap,
#
#                        zoom_start=13)
#
#     folium.Marker([x, y], popup=cityName).add_to(mappy)
#
#     mappy.save('YourMap.html')
#
#
# def ok():
#     print
#     "Basemap: ", var1.get()
#
#     print
#     "City: ", userCity.get()
#
#     print
#     "State: ", var2.get()
#
#     base = var1.get()
#
#     city = userCity.get()
#
#     state = var2.get()
#
#     makeMap(city, state, base)
#
#
# button = Button(master, text="OK", command=ok)
#
# button.grid(row=5, column=0)
#
# mainloop()