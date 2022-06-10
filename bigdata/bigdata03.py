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

# exam1
raw_data1 = {'subject_id':['1','2','3','4','5','7','8','9','10','11'],
            'test_score':[51,15,15,61,16,14,15,1,61,16]}
df_left = pd.DataFrame(raw_data1,columns=['subject_id','test_score'])

raw_data2 = {'subject_id':['4','5','6','7','8'],
             'first_name':['Billy','Brian','Bran','Bryce','Betty'],
             'last_name':['Bonder','Black','Balwner','Brice','Btisan']}
df_right = pd.DataFrame(raw_data2,columns=['subject_id','first_name','last_name'])
df_right

result1 = pd.merge(df_left,df_right,how='inner',on='subject_id')
result2 = pd.merge(df_left,df_right,how='left',on='subject_id')
result3 = pd.merge(df_left,df_right,how='right',on='subject_id')
result4 = pd.merge(df_left,df_right,how='outer',on='subject_id')

# exam2
data1 = {'국어':[100,78,78,99],
        '영어':[80,95,88,77],
        '수학':[100,85,89,90],
        '사회':[100,77,77,100],
        '과학':[70,87,60,79]}

df = pd.DataFrame(data1,index=['홍길동','고길동','임꺽정','유관순'])
df['평균'] = df.apply(np.mean,axis=1)  # dataframe 칼럼 추가 ...
df['합격여부'] = df['평균'] > 80         # dataframe 칼럼 추가 하여 평균이 80 이상이면 True 아니면 False ...
df

True_df = df[df['합격여부'].isin([True])]  # 합격여부가 합격인 사람 (True) 만 추려서 dataframe 만들기 ..
True_df
False_df = df[df['합격여부'].isin([False])] # 합격여부가 불합격인 사람 (False) 만 추려서 dataframe 만들기 ..
False_df

True_df = True_df.sort_values(by='평균',ascending=False)
True_df

# exam3
data2 = {'구단명':['전북현대','FC서울','울산현대','포항스틸러스','제주유나이티드'],
         '현감독':['김상식','안익수','홍명보','김기동','남기일'],
         '준우승 횟수':[2,5,10,4,5],
         '우승횟수':[9,6,2,5,1]}

data3 = {'구단명':['전북현대','FC서울','울산현대','포항스틸러스','제주유나이티드'],
         '홈구장':['전주','서울','울산','포항','제주'],
         '수용인원':[42477,66704,44102,25000,29791],
         '스폰서':['현대자동차','GS그룹','현대중공업','포스코','SK에너지']}

df1 = pd.DataFrame(data2)   # 첫번째 dataframe ..
df1
df2 = pd.DataFrame(data3)   # 두번째 dataframe ..
df2
key_df = pd.merge(df1,df2,on='구단명',how='right')   # 두개 merge ..
key_df
key_df['Total'] = key_df['준우승 횟수']+key_df['우승횟수']   # 총계수 구하기 : 준우승 횟수 + 우승 횟수 ( 방법 1 )
key_df['Total2'] = key_df.iloc[:,2:4].sum(axis=1)       # 총계수 구하기 : 준우승 횟수 + 우승 횟수 ( 방법 2 )
total_df = key_df.sort_values(by='Total',ascending=False)  # 총 횟수 별로 정렬 ...
total_df = total_df.reset_index(drop=True)   # 정렬 결과값 기준으로 index 재생성 ..
total_df
over_40000 = total_df[total_df['수용인원']>=40000]
over_40000
over_60000 = total_df[total_df['수용인원']>=60000]
over_60000

