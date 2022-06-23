import pandas as pd
import numpy as np
import os
import googlemaps
import matplotlib.pyplot as plt
import seaborn as sns 

plt.rc('font',family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

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

crime_analysis_raw = pd.read_csv(path+'02. crime_in_Seoul_include_gu_name2.csv',index_col=0)
crime_analysis_raw.head()

crime_analysis = pd.pivot_table(crime_analysis_raw,index='구별',aggfunc=np.sum)
crime_analysis.head()

crime_analysis['강간검거율'] = crime_analysis['강간 검거']/crime_analysis['강간 발생']*100
crime_analysis['강도검거율'] = crime_analysis['강도 검거']/crime_analysis['강도 발생']*100
crime_analysis['살인검거율'] = crime_analysis['살인 검거']/crime_analysis['살인 발생']*100
crime_analysis['절도검거율'] = crime_analysis['절도 검거']/crime_analysis['절도 발생']*100
crime_analysis['폭력검거율'] = crime_analysis['폭력 검거']/crime_analysis['폭력 발생']*100

del crime_analysis['강간 검거']
del crime_analysis['강도 검거']
del crime_analysis['살인 검거']
del crime_analysis['절도 검거']
del crime_analysis['폭력 검거']

crime_analysis.head()

con_list = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
for column in con_list :
    crime_analysis.loc[crime_analysis[column]>100, column] = 100
    
crime_analysis.rename(columns={'강간 발생':'강간',
                               '강도 발생':'강도',
                               '살인 발생':'살인',
                               '절도 발생':'절도',
                               '폭력 발생':'폭력'}, inplace=True)    

from sklearn import preprocessing
col = ['강간','강도','살인','절도','폭력']
x = crime_analysis[col].values
x

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x.astype(float))
x_scaled


col2 = ['강간검거율','강도검거율','살인검거율','절도검거율','폭력검거율']
crime_analysis_norm = pd.DataFrame(x_scaled,columns=col,index=crime_analysis.index)
crime_analysis_norm.head()
crime_analysis_norm[col2] = crime_analysis[col2]

result_CCTV = pd.read_csv(path+'01. CCTV_result2.csv',index_col='구별')
result_CCTV.head()

crime_analysis_norm[['인구수','CCTV']] = result_CCTV[['인구수','소계']]
crime_analysis_norm['범죄'] = np.sum(crime_analysis_norm[col],axis=1)
crime_analysis_norm['검거'] = np.sum(crime_analysis_norm[col2],axis=1)

crime_analysis_norm.head()

sns.pairplot(crime_analysis_norm,vars=['강도','살인','폭력'],kind='reg',height=3)
plt.show()
