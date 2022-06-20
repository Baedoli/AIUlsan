import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

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
            m.append(int((row[i+3])))
            f.append(int(row[-(i+1)]))

f.reverse()

plt.figure(figsize=(6,4))
plt.barh(range(101),m)
plt.barh(range(101),f)
plt.show()





