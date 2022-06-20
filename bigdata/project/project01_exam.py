
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams['axes.unicode_minus'] = 'False'
plt.rc('font',family='AppleGothic')

path = os.getcwd()

CCTV_Seoul = pd.read_csv(path+'/bigdata/data/01.CCTV_in_Seoul.csv')
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'},inplace=True)
CCTV_Seoul['최근증가율']=(CCTV_Seoul['2014년']+CCTV_Seoul['2015년']+CCTV_Seoul['2016년'])/CCTV_Seoul['2013년도 이전']*100

CCTV_Seoul.head()

pop_seoul = pd.read_excel(path+'/bigdata/data/01. population_in_Seoul.xls',header=2,usecols='B,D,G,J,N')
pop_seoul.head()

pop_seoul.rename(columns={pop_seoul.columns[0]:'구별',
                          pop_seoul.columns[1]:'인구수',
                          pop_seoul.columns[2]:'한국인',
                          pop_seoul.columns[3]:'외국인',
                          pop_seoul.columns[4]:'고령자'}, inplace=True)

pop_seoul.drop([0], inplace=True)
pop_seoul['구별'].unique()
pop_seoul[pop_seoul['구별'].isnull()]
pop_seoul.drop([26],inplace=True)
pop_seoul['비율_외국인'] = (pop_seoul['외국인']/pop_seoul['인구수'])*100
pop_seoul['비율_고령자'] = (pop_seoul['고령자']/pop_seoul['인구수'])*100

data_result = pd.merge(CCTV_Seoul,pop_seoul,on='구별')
data_result.head()

dColumn = ['2013년도 이전','2014년', '2015년', '2016년']
del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']

data_result.set_index('구별',inplace=True)

np.corrcoef(data_result['비율_고령자'],data_result['소계'])
np.corrcoef(data_result['비율_외국인'],data_result['소계'])
np.corrcoef(data_result['인구수'],data_result['소계'])

data_result['CCTV Rate'] = (data_result['소계']/data_result['인구수'])*100
data_result.head()

fp1 = np.polyfit(data_result['인구수'],data_result['소계'],1)
f1 = np.poly1d(fp1)
fx = np.linspace(100000,700000,100)

plt.figure(figsize=(8,6))
plt.scatter(data_result['인구수'],data_result['소계'],s=50)
plt.plot(fx,f1(fx),ls='dashed',lw=3,color='g')
plt.xlabel('인구수')
plt.ylabel('CCTV 대수')
plt.grid()
plt.show()

data_result['ERROR'] = np.abs(data_result['소계']-f1(data_result['인구수']))
df_sort = data_result.sort_values(by=data_result.columns[9],ascending=False)
df_sort.head()

plt.figure(figsize=(12,6))
plt.scatter(data_result['인구수'],data_result['소계'],c=data_result['ERROR'],s=50)
plt.plot(fx,f1(fx),ls='dashed',lw=3,color='g')
# 오차가 제일 큰 구 기준으로 타이틀 찍어 줌.
for n in range(10) :
    plt.text(df_sort['인구수'][n]*1, df_sort['소계'][n]*1,df_sort.index[n],fontsize=15)
plt.xlabel('인구수')
plt.ylabel('인구당 비율')
plt.colorbar()
plt.grid()
plt.show()


