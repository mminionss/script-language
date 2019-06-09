#-*- coding: utf-8 -*-

import folium
import webbrowser
import requests
import googlemaps
import geocoder
from geocoder import latlng
gmaps = googlemaps.client(key=)
geo = geocoder.google()
geo.la
# 누리동물병원
# 부산동물보호센터
# 청조동물병원
# 열린동물병원
# 러브펫종합동물병원
# 강동리본센터(reborn)
# 강현림동물병원
# 남산동물병원
# 홍익동물병원
# 한국동물구조관리협회
# 고양시동물보호센터
# 인천수의사회
# 진천동물병원
# 남양유기견보호센터
# 한국야생동물보호협회
# (사)한동보
# 평택시유기동물보호소
# 24시아이동물메디컬
# 정동물병원
# 광주동물보호소
# 창원유기동물보호소
# 자인동물보호소
# 군산유기동물보호소
# 박영재동물병원
# 버디종합동물병원
# 가나동물병원
# 신영재동물병원
# 청도동물보호소

# 위도 경도 지정
#한국동물구조관리협회 37.870134, 126.983358
#
# url='https://maps.googleapis.com/maps/api/geocode/json'
# find_loc = '러브펫 동물병원'
#
# params = {'sensor':'false','address':find_loc}
# r=requests.get(url,params=params)
# results = r.json()['results']
# location = results[0]['geometry']['location']
# print(location['lat'])
# import geocoder
# location='러브 펫 동물병원'
# g = geocoder.google('Mountain View,CA')
# print(g.geojson)

# map_osm = folium.Map (location = [37.870134, 126.983358 ],zoom_start=16)
# # 마커 지정
# folium.Marker([37.870134, 126.983358]).add_to(map_osm)
# # html 파일로 저장
# map_osm.save('osm.html')
#
# webbrowser.open("osm.html")