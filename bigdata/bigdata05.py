
from re import A
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

t = [0,1,2,3,4,5,6,7,8,9]
y = [9,8,7,9,8,3,2,4,3,4]

colormap = t
#colormap = y
plt.figure(figsize=(10,6))
plt.scatter(t,y, s=50, c=colormap, marker='>')   # color 가 그라데이션 생긴 거 처럼 보임 ...
#plt.scatter(t,y,marker='>')
plt.colorbar()
plt.show()

n = 1000
x = np.random.randn(n)
y = np.random.randn(n)
plt.figure(figsize=(5,5))
plt.scatter(x,y)
plt.show()

x1 = np.random.rand(50)
y1 = np.random.rand(50)
x2 = np.random.rand(50)+1
y2 = np.random.rand(50)+1
x3 = np.random.rand(50)+2
#y3 = np.random.rand(50)+2
y3 = np.random.rand(50)
plt.figure(figsize=(7,7))
plt.scatter(x1,y1,color='red')
plt.scatter(x2,y2,color='green')
plt.scatter(x3,y3,color='blue')
plt.show()

#plt.style.use('ggplot')
plt.style.use('seaborn')
plt.figure(figsize=(6,6))
plt.scatter([1,2,3,4],[10,30,20,40])
plt.show()

plt.style.use('ggplot')
plt.figure(figsize=(6,6))
#plt.scatter([1,2,3,4],[10,30,20,40],
#            s=[100,200,250,300],c=['red','green','blue','gold'])
plt.scatter([1,2,3,4],[10,30,20,40],
            s=[30,60,90,120],c=range(4), cmap='jet')
plt.colorbar()
plt.show()

plt.style.use('default')
countries = ['Brazil', 'Madagasgacar','S.Korea','United States','Ethiopia','Pakistan','China','Belize']
birth_rate = [16.4,33.5,9.5,14.2,38.6,30.2,13.5,23.0]
life_expectancy = [73.7,64.3,81.3,78.8,63.0,66.4,75.2,73.7]
GDP1 = np.array([4800,240,16700,37700,230,670,2640,3490])
color = range(len(countries))

plt.figure(figsize=(7,7))
plt.scatter(birth_rate,life_expectancy,c=color,s=GDP1/20)
plt.xlabel('Birth rate per 1000 population')
plt.ylabel(' Life expectancy at birth (year)')
plt.xlim(5,45)
plt.ylim(60,85)
plt.show()

plt.figure(figsize=(6,6))
plt.pie([10,20])
plt.show()

size = [2441,2312,1031,1233]
plt.figure(figsize=(6,6))
plt.axis('equal')
plt.pie(size,startangle=30,counterclock=True)  # counterclock : 시계 역 방향으로 그린다 ..
plt.show()

size = [2441,2312,1031,1233]
plt.figure(figsize=(6,6))
plt.axis('equal')
plt.pie(size,startangle=30,counterclock=False)  # counterclock : False 시계 방향으로 그린다 ..
plt.show()

size = [2441,2312,1031,1233,2441,2312,1031,1233,2441,2312,1031,1233,1233]
plt.figure(figsize=(6,6))
plt.axis('equal')
plt.pie(size)
plt.show()

plt.rc('font',family='AppleGothic') # Mac font 는 AppleGothic 으로 하면 됨..
size=[2441,2312,1031,1233]
label=['A형','B형','AB형','O형']
color = ['darkmagenta','deeppink','hotpink','pink']
plt.figure(figsize=(6,6))
wedgeprops={'width':1,'edgecolor':'w','linewidth':1,'linestyle':'--'}
plt.axis('equal')
plt.pie(size,labels=label,autopct='%.1f%%',explode=(0,0,0.1,0), colors=color, shadow=True, wedgeprops=wedgeprops)
plt.legend()
plt.show()

year = ['2018','2019','2020']
values = [100,400,900]
plt.figure(figsize=(10,6))
#plt.bar(year,values,align='edge',edgecolor='lightgray',linewidth=5)
plt.bar(year,values,align='edge',edgecolor='red',linewidth=5)
plt.show()

A = [5,30,45,22]
B = [5,25,50,20]
plt.figure(figsize=(10,6))
plt.bar(np.arange(4),A)
plt.bar(np.arange(4),B,bottom=A)
plt.show()

yaer = ['2018','2019','2020']
values = [100,400,900]
plt.figure(figsize=(6,6))
plt.barh(year,values,height=0.4)
plt.show()

A = [5,30,45,22]
B = [5,25,50,20]
plt.figure(figsize=(6,6))
plt.barh(np.arange(4),A)
plt.barh(np.arange(4),B,left=A)
plt.show()

