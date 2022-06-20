
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

