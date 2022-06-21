from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv
import math

plt.rcParams['axes.unicode_minus'] = 'False'
plt.rc('font',family = 'AppleGothic')


path = os.getcwd()
f = open(path+'/bigdata/data/age1.csv', encoding='utf-8')
data = csv.reader(f)
result = []
for row in data :
    if '태화동' in row[0] :
        for i in row[3:] :
            result.append(int(i))
print(result)

plt.style.use('ggplot')
plt.figure(figsize=(6,4))
plt.plot(result)
plt.show()

f = open(path+'/bigdata/data/age2.csv')
data = csv.reader(f)
result = []

m_location = input('검색 하고자 하는 동 이름을 입력 하세요 : ')

for row in data :
    if m_location in row[0] :
        for i in row[3:] :
            result.append(int(i))

plt.style.use('ggplot')
plt.figure(figsize=(6,4))
plt.plot(result)
plt.title(m_location+' 의 인구 구조')
plt.show()

f = open(path+'/bigdata/data/age2.csv')
data = csv.reader(f)
result = []

for row in data :
    if '무거동' in row[0] :
        for i in row[3:] :
            result.append(int(i))

result

plt.figure(figsize=(6,4))
plt.bar(range(101),result)
plt.show()

f = open(path+'/bigdata/data/gender2.csv')
data = csv.reader(f)
m = []
f = []

for row in data :
    if '무거동' in row[0] :
        for i in range(0,101) :
            m.append(int((row[i+3]))*-1)
            f.append(int(row[-(i+1)]))

f.reverse()

plt.figure(figsize=(6,4))
plt.barh(range(101),m,label='남자')
plt.barh(range(101),f,label='여자')
plt.legend()
plt.show()

f = open(path+'/bigdata/data/gender2.csv')
data = csv.reader(f)
m = []
f = []

m_location = input('검색하고자 하는 지역을 입력하세요 : ')
for row in data :
    if m_location in row[0] :
        for i in row[3:104] :
            m.append(int(i)*-1)
        for j in row[106:] :
            f.append(int(j))

plt.style.use('ggplot')
plt.figure(figsize=(6,4))
plt.title(m_location+' 의 남녀 성별 인구 분포')
plt.barh(range(101),m,label='남성')
plt.barh(range(101),f,label='여성')
plt.legend()
plt.show()

# 남여 인구 성비 비율을 남자 여자 Pie 차트로 표시 하기 ..
f = open(path+'/bigdata/data/gender3.csv')
data = csv.reader(f)
size = []

m_location = input('검색하고자 하는 지역을 입력하세요 : ')
for row in data :
    m = 0
    f = 0
    if m_location in row[0] :
        for i in range(101) :
            m += int(row[i+3])
            f += int(row[i+106])
        break

size.append(m)
size.append(f)

plt.figure(figsize=(6,4))
color = ['crimson','darkcyan']
plt.axis('equal')
plt.pie(size,labels=['남','여'],autopct='%.1f%%',colors=color,startangle=90)
plt.title(m_location+' 지역의 남여 성비 비율')
plt.show()

# 인구구조를 남성 여성별로 꺽은선으로 구분해서 그리기 ..
f = open(path+'/bigdata/data/gender4.csv')
data = csv.reader(f)

m = []
f = []

m_name = input('원하는 동네 입력 : ')
for row in data :
    if m_name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
        break

plt.figure(figsize=(6,4))
plt.plot(m,label='남성')
plt.plot(f,label='여상')
plt.legend()
plt.show()

# 인구구조를 남성, 여성 막대바로 그리기 ..
f = open(path+'/bigdata/data/gender4.csv')
data = csv.reader(f)
ingu = []

m_name = input('원하는 동네 입력 : ')
for row in data :
    if m_name in row[0] :
        for i in range(3,104) :
            ingu.append(int(row[i])-int(row[i+103]))
        break

plt.figure(figsize=(6,4))
plt.bar(range(101),ingu)
plt.show()

# 남녀 연령대별 성비 현황을 scatter 로 표시 하기 ( 남여 성비 차이 .. )
f = open(path+'/bigdata/data/gender2.csv')
data = csv.reader(f)

m = []  # 남자
f = []  # 여자
size = []

m_name = input('원하는 동네 입력 : ')
for row in data :
    if m_name in row[0] :
        for i in range(3,104) :
            m.append(int(row[i]))
            f.append(int(row[i+103]))
            size.append(math.sqrt(int(row[i])+int(row[i+103])))
        break

plt.figure(figsize=(6,4), dpi=150)
plt.style.use('ggplot')
plt.scatter(m,f,s=size,c=range(101),alpha=0.5,cmap='jet')
plt.plot(range(max(m)),range(max(m)),color='g')
plt.colorbar()
plt.title(m_name+' 지역의 성별 인구 비율')
plt.xlabel('남성 인구수')
plt.ylabel('여성 인구수')
plt.show()
