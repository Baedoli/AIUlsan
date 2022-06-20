
from cProfile import label
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = 'False'
plt.rc('font',family = 'AppleGothic')

path = os.getcwd()
traffic_accident = pd.read_csv(path+'/bigdata/data/교통사고 통계_20201231.csv')
traffic_accident.head()

traffic_accident.index
traffic_accident.columns
traffic_accident.values
traffic_accident.info()
traffic_accident.describe()

traffic_accident.head()

columns = ['중상자수','경상자수','부상신고자수']
traffic_accident.drop(columns,axis=1,inplace=True)
df = traffic_accident
df.head()

df_day = df[(df.주야=='주')]
df_night = df[(df.주야=='야')]

df_day.head()
df_night.head()

n_data = len(df_night)
x = np.arange(n_data)
bar_width = 0.4
y1 = df_day['사고건수']
y2 = df_night['사고건수']
xticks_list = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']


plt.figure(figsize=(8,4))
plt.bar(x,y1,width=bar_width,label='주간')
plt.bar(x+bar_width,y2,width=bar_width,label='야간')
plt.title('월별 주야 사고 건수')
plt.xticks(x+0.2, xticks_list, fontsize=15)
plt.xlabel('월')
plt.ylabel('사고건수')
plt.legend()
plt.show()

df.head()
df['사망자비율'] = df['사망자수']/df['사고건수']*100
df_death_rate_day = df[df.주야=='주']
df_death_rate_night = df[df.주야=='야']

df_death_rate_day.head()
df_death_rate_night.head()

n_data = len(df_death_rate_night)
x = np.arange(n_data)
bar_width = 0.4
y1 = df_death_rate_day['사망자비율']
y2 = df_death_rate_night['사망자비율']
xticks_list = ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']

plt.figure(figsize=(8,4))
plt.bar(x,y1,width=bar_width,label='주간')
plt.bar(x+bar_width,y2,width=bar_width,label='야간')
plt.title('월별 주야 사망자 비율(%)')
plt.xticks(x+0.2,xticks_list, fontsize=15)
plt.xlabel('월')
plt.ylabel('사망자 비율(%)')
plt.legend()
plt.show()
