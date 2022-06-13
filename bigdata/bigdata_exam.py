import pandas as pd
import numpy as np

s = pd.Series([1,3,5,np.nan,6,8])

dates = pd.date_range('20220301',periods=6)
dates
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
df
df.head()
df.head(-3)
df.index
df.columns
df.values
df.info
df.describe()
df.sort_values(by="A",ascending=False)
df['A']
df[0:3]
df['20220301':'20220303']
df['A']
df[['A','B']]
df['20220301':'20220302']
df.loc[dates[0]]
df
df.loc[:,['A','B']]
df.loc['20220301':'20220302',['B','C']]
df.loc[dates[0],['C']]
df.iloc[3]
df
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[2,3]]
df.iloc[:,1:3]

raw_data = {'first_name' :['Jason','Moily','Tina','Jake','Amy'], \
            'last_name' :['Miller','Jacobson','Ali','Milner','Andrew'], \
            'age' :[42,52,36,24,73], \
            'city' :['San Fransisco', 'Balimore', 'Miami', 'Douglas', 'Boston']}

df = pd.DataFrame(raw_data,index=['a','b','c','d','e'])
df
df.loc['b']['city']

jpl_data = {'Team': ['Riders','Riders','Devils','Devils','kings','Kings','Kings','Riders','Royals','Kings','Rovals','Riders'], \
            'Rank': [1,2,2,3,3,4,1,1,2,4,1,2], \
            'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014, 2015,2017], \
            'Points': [876, 789,863, 673, 741,812, 756, 788, 694, 701 ,804, 690] }

df = pd.DataFrame(jpl_data)
df.iloc[5]['Year']

data = [['Choi', 29], ['Kim',32], ['Jung', 27], ['Lee', 25]]
df = pd.DataFrame(data,columns=['Name','Age'],index=[1,2,3,4])
df.iloc[2]['Age']

# question 4
data = [['Kim','A0','B0','B+'],
        ['Lee','B+','A0','B0'],
        ['Choi','B0','B+','A0'],
        ['Jung','A0','B0','A+']]

df = pd.DataFrame(data, columns=['Family Name','Python','Java','C++'], index=['A','B','C','D'])
df.transpose()

df[df.A > 0]
df[df > 0]
df['E'] = [1,2,3,4,5,6]
df['E'].isin([2,4])
df[df['E'].isin([2,4])] # 전체 DataFrame 에서 E열어세 2,4 가 True 인 행을 다 보여준다..

bank_client_df = {'Bank_Client_ID': [111,222,383,44,555, 666,777,608],
                  'Bank_Client_Nane' : ['Willian', 'Steve', 'Vanes', 'Ryan', 'Henry', 'Dinel', 'Jackson', 'John'],
                  'New_North [$]' :[100, 200,1000, 15000, 300, 1500,5000, 3500],
                  'With_bank' : [1,3,5,10,7,2,5,6]}
df = pd.DataFrame(bank_client_df)
bank_client5_df = df[df['With_bank']>=5]
bank_client5_df[bank_client5_df['With_bank'].isin([10])]

df.apply(np.cumsum)
df.apply(lambda x :x.max()-x.min())
df.apply(np.cumsum,axis=0)
df.apply(np.cumsum,axis=1)
df.apply(lambda x:x.max()-x.min(),axis=1)

df = pd.DataFrame({'A':[1,8,25,12,19],
                   'B':[16,17,4,6,23],
                   'C':[9,21,13,20,2],
                   'D':[18,5,7,24,11],
                   'E':[22,14,16,3,10]})
df.apply(np.sum,axis=0)
df.apply(np.sum,axis=1)

dates = pd.date_range('20220301',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
df[df['A']>0]
df['E'] = ['A','B','C','D','E','F']
df
df['E'].isin(['A'])
df[df['E'].isin(['A'])]

df.apply(lambda x:x.max()-x.min(),axis=1)

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

result = pd.concat([df1,df4],ignore_index=True)
result