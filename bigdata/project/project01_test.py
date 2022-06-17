
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

path = os.getcwd()

CCTV_Seoul = pd.read_csv(path+'/bigdata/data/01.CCTV_in_Seoul.csv')
CCTV_Seoul.head()
CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'},inplace=True)  # 하단 처럼 이름을 재정의 하여 할 필요 없이 바로 칼럼 변경 하고 저장 함...

CCTV_Seoul2 = CCTV_Seoul.rename(columns={CCTV_Seoul.columns[0]:'구별'}) # inplace = True 옵션을 주지 않고 할 경우 rename 하여 재 지정 필요 ...
CCTV_Seoul2.head()

def get_calc(df) :
    return (df['2014년']+df['2015년']+df['2016년'])/df['2013년도 이전']*100

CCTV_Seoul.sort_values(by=CCTV_Seoul.columns[1],ascending=True).head(5)
CCTV_Seoul.sort_values(by=CCTV_Seoul.columns[1],ascending=False).head(5)
CCTV_Seoul['최근증가율'] = get_calc(CCTV_Seoul)

CCTV_Seoul['최근증가율'] = (CCTV_Seoul['2014년']+CCTV_Seoul['2015년']+CCTV_Seoul['2016년'])/CCTV_Seoul['2013년도 이전']*100
CCTV_Seoul.head()

CCTV_Seoul.sort_values(by=CCTV_Seoul.columns[6],ascending=False).head()

# 엑셀을 읽을 때 행 타이틀 칼럼을 읽고, 특정 열만 읽어 들인다 ...
pop_seoul = pd.read_excel(path+'/bigdata/data/01. population_in_Seoul.xls',header=2,usecols='B,D,G,J,N')
pop_seoul.head()
# 각 칼럼의 타이틀을 변경 한다 ...
pop_seoul.rename(columns={pop_seoul.columns[0]:'구별'},inplace=True)
pop_seoul.rename(columns={pop_seoul.columns[1]:'인구수'},inplace=True)
pop_seoul.rename(columns={pop_seoul.columns[2]:'한국인'},inplace=True)
pop_seoul.rename(columns={pop_seoul.columns[3]:'외국인'},inplace=True)
pop_seoul.rename(columns={pop_seoul.columns[4]:'고령자'},inplace=True)

pop_seoul.rename(columns={pop_seoul.columns[0]:'구별',
                          pop_seoul.columns[1]:'인구수',
                          pop_seoul.columns[2]:'한국인',
                          pop_seoul.columns[3]:'외국인',
                          pop_seoul.columns[4]:'고령자'
                          },inplace=True)
pop_seoul.head()

# 첫번째 총개 행을 제거한다 ...
pop_seoul.drop([0],inplace=True)
pop_seoul.head()
# 구별 레코드 값이 null 인것을 검색 ..
pop_seoul['구별'].unique()
# 구별 레코드 값이 null 인 index 검색 ..
pop_seoul[pop_seoul['구별'].isnull()]
# 검색된 row index 확인 후 해당 레코드 삭제 ..
pop_seoul.drop([26],inplace=True)

#인구수 대비 외국인, 고령자 비율 추가
pop_seoul['비율_외국인'] = (pop_seoul['외국인']/pop_seoul['인구수'])*100
pop_seoul['비율_고령자'] = (pop_seoul['고령자']/pop_seoul['인구수'])*100
pop_seoul.head()

pop_seoul.sort_values(by=pop_seoul.columns[1],ascending=False).head()
pop_seoul.sort_values(by=pop_seoul.columns[1],ascending=True).head()

# 두개의 data frame 을 합친다. merge 이용... ( 구별 칼럼을 key 칼럼으로 활용 )
data_result = pd.merge(CCTV_Seoul,pop_seoul,on='구별')
data_result.head()

del data_result['2013년도 이전']
del data_result['2014년']
del data_result['2015년']
del data_result['2016년']
data_result.head()

# 기존의 index 는 정수형이 지만 index 를 구별로 변환 ...
data_result.set_index('구별',inplace=True)
data_result.head()

np.corrcoef(data_result['비율_고령자'],data_result['소계'])
np.corrcoef(data_result['비율_외국인'],data_result['소계'])
np.corrcoef(data_result['인구수'],data_result['소계'])
np.corrcoef(data_result['한국인'],data_result['소계'])
np.corrcoef(data_result['외국인'],data_result['소계'])
np.corrcoef(data_result['고령자'],data_result['소계'])

data_result.sort_values(by=data_result.columns[0],ascending=False).head()
data_result.sort_values(by=data_result.columns[2],ascending=False).head()

plt.rcParams['axes.unicode_minus'] = 'False'
plt.rc('font',family = 'AppleGothic')

# dataFrame 에서 바로 plot 해서 차트 그리기...
data_result['소계'].plot(kind='barh',grid=True,figsize=(10,7))
# dataFrame 에서 Sort 후 plot 해서 차트 그리기...
data_result['소계'].sort_values().plot(kind='barh',grid=True,figsize=(10,7))
plt.show()

data_result['CCTV RATE'] = data_result['소계']/data_result['인구수']*100
data_result.head()
data_result['CCTV RATE'].sort_values().plot(kind='barh',grid=True,figsize=(10,7))
plt.show()

plt.figure(figsize=(8,6))
plt.scatter(data_result['인구수'],data_result['소계'])
plt.xlabel('인구수')
plt.ylabel('CCTV 대수')
plt.grid()
plt.show()

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
data_result.head()
df_sort = data_result.sort_values(by=data_result.columns[9],ascending=False)
df_sort.head()

df_sort.to_csv(path+'/bigdata/data/'+'cctv_pop.csv',encoding='utf-8-sig')
cctv_pop = pd.read_csv(path+'/bigdata/data/'+'cctv_pop.csv')
cctv_pop

data_result.head()

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





df = pd.read_csv(path+'/bigdata/data/dataframe01.csv')

df.drop([1,2],inplace=True)
df.drop([1,2],axis=0,inplace=True)
df.drop(['A','B'],axis=1,inplace=True)
df.drop(columns=['A','B'],axis=1,inplace=True)
df.head()

df3 = pd.read_csv(path+'/bigdata/data/dataframe03.csv')

df3.head()
df3.index = ['A','B','C','D']
df3.drop(['A'],axis=0,inplace=True)
