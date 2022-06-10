import pandas as pd
import numpy as np

dates = pd.date_range('20220301',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])

df.apply(np.cumsum)
df.apply(lambda x:x.max()-x.min())

df.apply(np.cumsum,axis=0)
df.apply(np.cumsum,axis=1)

df.apply(lambda x:x.max() - x.min(), axis=0)
df.apply(lambda x:x.max() - x.min(), axis=1)

# exam 1
df = pd.DataFrame({'A':[1,8,25,12,19],
                   'B':[16,17,4,6,23],
                   'C':[9,21,13,20,2],
                   'D':[18,5,7,24,11],
                   'E':[22,14,16,3,10]})
m_df = df.apply(np.cumsum,axis=0)
m_df
m_df = df.apply(np.cumsum,axis=1)
m_df

# exam 2
df = pd.DataFrame({'A':[1,6,11,16,21],
                   'B':[2,7,12,17,22],
                   'C':[3,8,13,18,23],
                   'D':[4,9,14,19,24],
                   'E':[5,10,15,20,25]})
m_df = df.apply(np.square)
m_df
# numpy 의 square 는 제곱을 구하는 거 같습니다.

# exam 3
df = pd.DataFrame({'A':[1,39,121,266,441],
                   'B':[4,46,144,289,484],
                   'C':[9,64,169,324,529],
                   'D':[16,81,196,361,576],
                   'E':[25,100,225,400,625]})
m_df = df.apply(np.sqrt) # 제곱근 구하는 함수 ..
m_df.astype(int) # as type : 정수형 type 으로 형변환 ...
m_df
# sqrt : 제곱근

df1 = pd.DataFrame({'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']},
                   index=[0,1,2,3])

df2 = pd.DataFrame({'A':['A4','A5','A6','A7'],
                   'B':['B4','B5','B6','B7'],
                   'C':['C4','C5','C6','C7'],
                   'D':['D4','D5','D6','D7']},
                   index=[4,5,6,7])

df3 = pd.DataFrame({'A':['A8','A9','A10','A11'],
                   'B':['B8','B9','B10','B11'],
                   'C':['C8','C9','C10','C11'],
                   'D':['D8','D9','D10','D11']},
                   index=[8,9,10,11])

df4 = pd.DataFrame({'B':['B2','B3','B6','B7'],
                   'D':['D2','D3','D6','D7'],
                   'F':['F2','F3','F6','F7']},
                   index=[2,3,6,7])

result = pd.concat([df1,df2,df3])
result = pd.concat([df1,df2,df3],keys=['x','y','z'])
result.index
result.index.get_level_values(0)
result.index.get_level_values(1)

result = pd.concat([df1,df4],axis=1)
result 

result = pd.concat([df1,df4],axis=0)
result 

result = pd.concat([df1,df4],axis=1,join='inner')
result

result = pd.concat([df1,df4],axis=0,join='inner')
result

result = pd.concat([df1,df4],axis=1,join='outer')
result

result = pd.concat([df1,df4],axis=0,join='outer')
result

result = pd.concat([df1,df4],ignore_index=True)
result 

left = pd.DataFrame({'key':['K0','K4','K2','K3'],
                   'A':['A0','A1','A2','A3'],
                   'B':['B0','B1','B2','B3']})

right = pd.DataFrame({'key':['K0','K1','K2','K3'],
                   'C':['C0','C1','C2','C3'],
                   'D':['D0','D1','D2','D3']})

pd.merge(left,right,how='left', on='key')
pd.merge(left,right,how='right',on='key')
pd.merge(left,right,how='outer',on='key')
pd.merge(left,right,how='inner',on='key')
pd.merge(left,right,on='key')



