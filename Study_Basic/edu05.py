# 교육 5일 차 반복문 실습 ...

a = list(range(5))
b = list(range(1,5))

print(a,b)
print(list(range(1,10,2)))
print(list(range(10,1,-2)))
print(list(range(-3,6,2)))

for i in range(1,10,2) :
    print('i value : ',i)

for i in reversed (range(10)) :
    print(' i value : ',i)    
    
str1 = 'Ulsan'
for i in str1:
    print(' i value : ',i)
    
# Mission 1
dan = int(input('원하는 단 입력 : '))
for i in range(1,10) :
    print('%2d * %d = %2d'%(dan,i,dan*i))

i = 0
while i < 10:
    print('i value :',i)
    i += 1

i = 0
while True :
    print('i value :',i)
    i += 1
    if i==10 :
        break

while True:
    light = input('신호등 색깔을 입력 (red/green/yellow)')
    if light == 'green' :
        print('Go ~~~!!')
        break
    elif light == 'red' :
        print('Stop')
        continue
    elif light == 'yellow' :
        print('Stay')
        continue
    else :
        continue
    
i = 0
while i < 3 :
    print('%d 루프 안쪽 :'%i)
    i += 1
else :
    print('%d else 부문 '%i)
    
 # Mission 3   
import calendar
import random
cnt = 0
num1 = random.randint(1,10)
while True :
    num2 = int(input('1 ~ 10까지의 예측 숫자를 입력 하세요 : '))
    cnt += 1
    if num2 == num1 :
        print('축하 합니다 !! %d 번 도전하셨어요'%cnt)
    elif num2 > num1 :
        print('Up')
        continue
    elif num2 < num1 :
        print('Down')
        continue
        
for i in range(3) :
    for j in range(1,6) :
        print(j, end=" ")     
    print()    

for i in range(1,5) :
    for j in range(1, i+1) :
        print('*', end="")
    print()

# Mission 4    
s1 = ''
for  n1 in range(1,10) :
    s1 = ''
    for n2 in range(2,10) :
        s1 = s1+str('%2d * %d = %2d'%(n2,n1,n2*n1))     
    print(s1)    

import calendar
calendar.prmonth(2022,5)

import calendar as cal
cal.prmonth(2022,5)    

from calendar import prmonth
prmonth(2022,5)

