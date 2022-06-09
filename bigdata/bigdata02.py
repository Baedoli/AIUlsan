
import pandas as pd
import numpy as np

dates = pd.date_range('20210301',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])
df.head()

df.describe()
df.sort_values(by='B',ascending=False)
df.index
df.columns
df.values
df.info()
df.describe()
df.sort_values(by='C',ascending=True)

df['A'] # 칼럼은 선언 가능 ..
df[0:3] # 슬라이싱은 index ( 행 ) 의 경우 가능
df['A':'B'] # 슬라이싱은 column 은 되지 않음 ..
df[['A','B','C']] # Column 의 여러개의 경우 리스트를 하나 더 만들어서 언급 ...
df['20210301':'20210303'] # 슬라이싱은 행의 경우 index 가능 ..

df2 = pd.DataFrame(np.random.randn(6,6),index=dates,columns=dates)
df3 = pd.DataFrame(np.random.randn(6,4),index=dates,columns=[1,2,3,4])
df4 = pd.DataFrame(np.random.randn(6,6),index=[1,2,3,4,5,6],columns=[1,2,3,4,5,6])
df5 = pd.DataFrame(np.random.randn(6,4),index=[1,2,3,4,5,6],columns=['A','B','C','D'])

df.loc[dates[0]]
df.loc[:,['A','B']]
df.loc['20210301':'20210302',['A','B']]
df.loc['20210301',['A','B']]
df.loc[dates[0],['A','B']]
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]

# practice 1
df.loc[dates[0]]
df.loc[:,['A','B']]
df.loc['20210301':'20210303',['A','B']]
df.loc['20210301',['A','B']]
df.loc[dates[0],['A']]
df.iloc[3]
df.iloc[3:5,0:2]
df.iloc[[1,2,4],[0,2]]
df.iloc[1:3,:]
df.iloc[:,1:3]

# practice 2
dates = pd.date_range('20210301',periods=31)
df = pd.DataFrame(np.random.randn(31,26),index=dates,columns=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])

df

df.loc[dates[30]]
df.loc[:,['k','l','m','n','o','p']]
df.loc['20210302':'20210328',['k','l','m','n','o','p']]
df.loc['20210302',['k','l','m','n','o','p']]
df.loc[dates[30],'k']
df.iloc[15]
df.iloc[10:20,5:15]
df.iloc[[1,3,5,7,9],[2,4,6,8,9]]
df.iloc[7:9,:]
df.iloc[:,7:9]

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

pd.set_option('display.max_columns',60)
pd.set_option('display.max_rows',20)

# question 1
raw_data = {'first_name' :['Jason','Moily','Tina','Jake','Amy'], \
            'last_name' :['Miller','Jacobson','Ali','Milner','Andrew'], \
            'age' :[42,52,36,24,73], \
            'city' :['San Fransisco', 'Balimore', 'Miami', 'Douglas', 'Boston']}

df = pd.DataFrame(raw_data,index=['a','b','c','d','e'])

df.loc[['b'],['city']]
df.iloc[1,3]

# question 2
jpl_data = {'Team': ['Riders','Riders','Devils','Devils','kings','Kings','Kings','Riders','Royals','Kings','Rovals','Riders'], \
            'Rank': [1,2,2,3,3,4,1,1,2,4,1,2], \
            'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014, 2015,2017], \
            'Points': [876, 789,863, 673, 741,812, 756, 788, 694, 701 ,804, 690] }

df = pd.DataFrame(jpl_data)
df
df.iloc[5]['Year']
df.iloc[5,2]

# question 3
data = [['Choi', 29], ['Kim',32], ['Jung', 27], ['Lee', 25]]
df = pd.DataFrame(data,columns=['Name','Age'],index=[1,2,3,4])
df
df.iloc[2]['Age']
df.loc[3]['Age']

# question 4
data = [['Kim','A0','B0','B+'],
        ['Lee','B+','A0','B0'],
        ['Choi','B0','B+','A0'],
        ['Jung','A0','B0','A+']]

df = pd.DataFrame(data, columns=['Family Name','Python','Java','C++'], index=['A','B','C','D'])
df
df.transpose()

dates = pd.date_range('20210301',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['A','B','C','D'])

df[df.A > 0]
df[df > 0]

df['E'] = ['one','one','two','three','four','three']
df['E'].isin(['two','four'])
df[df['E'].isin(['two','four'])]

bank_client_df = {'Bank_Client_ID': [111,222,383,44,555, 666,777,608],
                  'Bank_Client_Nane' : ['Willian', 'Steve', 'Vanes', 'Ryan', 'Henry', 'Dinel', 'Jackson', 'John'],
                  'New_North [$]' :[100, 200,1000, 15000, 300, 1500,5000, 3500],
                  'With_bank' : [1,3,5,10,7,2,5,6]}

df = pd.DataFrame(bank_client_df)

# 1. 5년 이상 고객 만 추림 ... 
df[df.With_bank>=5]
# 2. 위의 항목 결과 값을 bank_client5_df 이름으로 재정의 하세요.
bank_client5_df = df[df.With_bank>=5]
# 재정의 후 index 재정의 ...
bank_client5_df = bank_client5_df.reset_index()
# 3. bank_client5_df 에 10년된 고객의 정보를 True, False 로 반환 ..
bank_client5_df['With_bank'].isin([10])
# 4. 10년된 고객만 보이게 데이터 프레임을 만드세요.
bank_client5_df[bank_client5_df['With_bank'].isin([10])]