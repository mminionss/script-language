# #-*- coding: utf-8 -*-

import folium
import webbrowser
import requests
import json

# 네이티브 앱 키
# f04c74adfc7f52935732eb312d3c98f5
# REST API 키
# 83bee4a2cc30ecb8dc09921b53417214
# JavaScript 키
# d945efe23d65b9cba53d60375315617c
# Admin 키
# 708ecd59aca5f4c51908a7a2b8bd98fc


def getLatLng(addr):
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + addr

    headers = {"Authorization": "KakaoAK 83bee4a2cc30ecb8dc09921b53417214"}

    result = json.loads(str(requests.get(url, headers=headers).text))

    match_first = result['documents'][0]['address']

    return float(match_first['y']), float(match_first['x'])


def FindRocation(rocationAddr):
    #rocationList=[35.1345653,128.9260548]

    rocationList = getLatLng(rocationAddr)
    map_osm = folium.Map (location = rocationList, zoom_start=16)
    # 마커 지정
    folium.Marker(rocationList).add_to(map_osm)
    # html 파일로 저장
    map_osm.save('osm.html')

    webbrowser.open("osm.html")