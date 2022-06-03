# 9일차 파일 관련 실습 ...

f = open('hello2.txt', 'w')
f.write('Hello\n')
f.writelines(['Before\n','After\n'])
f.writelines('\n'.join(['BlockDMask','python','blog']))
print('Happy',file = f)
f.close()

with open('hello2.txt', 'a') as f:
    f.write('Hello222\n')
    print('Happy222',file=f)
    f.writelines(['Before!!!\n','After!!!\n'])
    f.writelines('\n'.join(['BlockDMask','python','blog']))

f = open('hello2.txt','r')
t = f.read()
print(t)
f.close()

with open('hello2.txt','r') as f:
    t = f.read()
    print(t)
    
fd = open('hello.txt','r')
while True :
    line = fd.readline()
    if not line : break
    print(line) 
fd.close()

with open('hello.txt','r') as fd:
    while True :
        line = fd.readline().rstrip('\n')
        if not line : break
        print(line)
    
with open('hello.txt','r') as fd:
    line = fd.readline().rstrip('\n')
    while line != "" :
        print(line)
        line = fd.readline().rstrip('\n')
        
fd = open('hello.txt','r')
line = fd.readlines()
print(line)
fd.close()

fd = open('hello.txt','r')
list1 = fd.readlines()
for list in list1 :
    print(list.rstrip('\n'))
fd.close()    

with open('hello.txt','r') as fd:
    list1 = fd.readlines()
    for list in list1:
        print(list.rstrip('\n'))
        
fd = open('hello.txt','r')
for line in fd :
    word_list = line.split()
    for word in word_list:
        print(word)
fd.close()                

with open('hello.txt','r') as fd:
    for line in fd:
        word_list = line.split()
        for word in word_list :
            print(word)

fd = open('hello.txt','r')
line = str(fd.readlines())
word_list = line.split()
for word in word_list:
    print(word)
fd.close()                

fd = open('hello.txt','r')
line = fd.readline()
word_list = line.split()
for word in word_list:
    print(word)
fd.close()                

infilename = input('input file name :')
outfilename = input('output file name :')

ifile = open(infilename,'r',encoding='UTF-8')
ofile = open(outfilename,'w',encoding='UTF-8')

sum = 0
count = 0

line = ifile.readline()
while line != "" :
    s = int(line)
    sum += s
    count += 1
    line = ifile.readline()

ofile.write('Total Sales Amount = '+str(sum)+'\n')
ofile.write('Avg Daily Sales Amount = '+str(sum/count))

ifile.close()
ofile.close()

list1 = [1,2,3]
i = iter(list1)
print(next(i))
print(next(i))
print(next(i))
print(next(i))

list1 = [1,2,3,4,5]
i = iter(list1)
print(type(i))
try :
    while True :
        print(next(i))
except :
    None

# 한번 사용 하고 나면 다시 사용 불가 한게 이터레이터 이다. 
# 아래 예제에서 보면 한번 사용 후 다시 사용해 보면 사용 할 수가 앖다.    
list1 = [1,2,3,4,5]
ia = iter(list1)
for i in ia :
    print(i)
for i in ia :
    print(i)

list1 = [1,2,3,4,5]
ia = iter(list1)
for i in ia :
    print(i)
print('-'*10)
for i in list1 :
    print(i)

import random
for i in iter(lambda : random.randint(0,5), 2 ) :
    print(i,end=" ")

import random
while True :
    i = random.randint(0,5)
    if i==2 :
        break
    print(i, end=" ")
    
code = iter(['HTML','CSS','JS'])
for i in range(1,4) :
    x = next(code)
    print(x)
    
code = iter(['HTML','CSS','JS'])
for i in range(1,5) :
    x = next(code,'end')
    print(x)

import csv
f = open('weather.csv','r')
data = csv.reader(f)
header = next(data)
print(header)
temp = 1000
for row in data:
    if temp > float(row[3]) :
        temp = float(row[3])
print('가장 추운 날은 ',temp,' 입니다.')
f.close()
