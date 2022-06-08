import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8]) # np.nam : numpy 의 라이브러리 활용.. 숫자가 아니다 .. 의미 NoN : not a number
s

dates = pd.date_range('20210301',periods=6)
dates
dates1 = pd.date_range(start='2021-01-01',end='2022-12-31',freq='Q')
dates1

df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=['A','B','C','D'])
df.head()

df.index
df.columns
df.values 
df.info()
df.describe()

df.sort_values(by='B',ascending=False)
df['A']
df['A':'B']

df[0:3]
df['2021-03-01':'2021-03-02']

