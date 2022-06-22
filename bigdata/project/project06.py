import pandas as pd
import numpy as np
import os
import googlemaps

path = os.getcwd()
path = path+'/bigdata/data/'

crime_analysis_police = pd.read_csv(path+'02. crime_in_Seoul2.csv')
crime_analysis_police.head()

gmaps_key = 'AIzaSyAH4lBEZbvwvC5d7ecKroaJLisu7Ub4yxA'
gmaps = googlemaps.Client(key=gmaps_key)

gmaps.geocode('서울중부경찰서',language='ko')

station_name = []
for name in crime_analysis_police['관서명'] :
    station_name.append('서울'+str(name[:-1])+'경찰서')

station_address = []
station_lat = []
station_lng = []
for name in station_name :
    tmp = gmaps.geocode(name,language='ko')
    station_address.append(tmp[0].get('formatted_address'))
    tmp_loc = tmp[0].get('geometry')
    station_lat.append(tmp_loc['location']['lat'])
    station_lng.append(tmp_loc['location']['lng'])
    print(name+' --> '+tmp[0].get('formatted_address'))
    
gu_name = []
for name in station_address :
    tmp = name.split()
    tmp_gu = [gu for gu in tmp if gu[-1]=='구'][0]
    gu_name.append(tmp_gu)
    
crime_analysis_police['구별'] = gu_name
crime_analysis_police.head()

crime_analysis_police[crime_analysis_police['관서명']=='금천서']
# 현재 구글에서는 변경된 이후 이므로 아래와 같이 변경할 필요가 없음. ( 만약 이전 주소인 관악구로 되어 있다면 아래와 같이 변경 해야함. )
# crime_analysis_police.loc[crime_analysis_police['관서명']=='금천서',['구별']] = '금천구'

crime_analysis_police.to_csv(path+'02. crime_in_Seoul_include_gu_name2.csv',encoding='utf-8-sig')
crime_analysis_police.head()