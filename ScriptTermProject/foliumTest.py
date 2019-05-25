#-*- coding: utf-8 -*-

import folium
import webbrowser

# 위도 경도 지정
#한국동물구조관리협회 37.870134, 126.983358
map_osm = folium.Map (location = [37.870134, 126.983358 ],zoom_start=16)
# 마커 지정
folium.Marker([37.870134, 126.983358]).add_to(map_osm)
# html 파일로 저장
map_osm.save('osm.html')

webbrowser.open("osm.html")