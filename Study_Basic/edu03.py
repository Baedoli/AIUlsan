# 교육 3일차 ... 
# 교육 준비 잘 합시다 ..

from audioop import avg

from sklearn.feature_selection import f_classif


print('# 리스트 만들기 ')
list1 = [10,20,30,40,50]
list2 = ['A','B','C','D','E']
list3 = [100, 'python', [1,2,3]]
list4 = [list1, list2]

print(list1)
print(list2)
print(list3)
print(list4)

print('# 리스트 슬라이싱 #')
list1 = [10,20,30,40,50,60,70,80]

print(list1[1:5])
print(list1[2:])
print(list1[:])
print(list1[-7:-2])
print(list1[-7:])
print(list1[:-2])
print(list1[0:8:3])
print(list1[::-1])

list1 = [10,20,30,40]; list2 = [50,60]
print(list2+[70])
print(list1+list2)
print(list2*2)
print(list1==list2)
print(f'list1 size : {len(list1)}')
print(f'list2 size : {len(list2)}')
print(list1>list2)

name = ['김유신','이순신','홍길동','최하나','한나리']
check = input('이름 입력?')
print(check in name)
if (check in name):
    print('출석')
else:
    print('결석')
print(' 출석인원 : ', len(name))    

list1 = list('ulsan city')
t1 = ('one','two','three')
list2 = list(t1)
print(list1)
print(list2)    

d1 = ['coffee','donut']; d2 = ['ice', 'cream']
s1 = '&'.join(d1)
s2 = ''.join(d2)

print('&'.join(d1))
print(''.join(d2))
print(type(s1), type(s2))
print(s1,s2)

list1 = [10,20,30]
print(list1)
list1.append('add')
print(list1)
list1.append(['A', 'B'])
print(list1)
list1.append(('A','B'))
print(list1)
list1.append({'one','two'})
print(list1)
list1.insert(2,'sub')
print(list1)
print(list1[6])
list1.insert(8,'sub')
print(list1)

list1 = [10,20,30]; list2 = []
print(list1)
list1.extend('Hi')
print(list1)
list1.extend(['mul','div'])
print(list1)
list1.extend(('one','two'))
print(list1)
list2.extend(range(1,5))
print(list2)
list2.extend({'on','off'})
print(list2)

num1 = ['one','two','three','four','five']
num1.pop()
print(num1)
num1.pop(0)
print(num1)

num1 = ['one','two','three','four','five']
num1.remove('two')
print(num1)
num1.remove('five')
print(num1)

num1 = ['one','two','three','four','five']
num2 = [100,90,90,80,70]
num1.clear()
print(num1)
num1.append('add')
print(num1)
print(num2.count(90))

num1 = ['one','two','three','four','five']
del(num1)
print(num1)

num1 = [1,2,3] 
num2 = num1
print(id(num1), id(num2))
print(num1, num2)
num1.insert(1,20)
print(num1, num2)
num3 = num1.copy()
print(id(num1), id(num3))
print(num1, num3)
num3.insert(1,200)
print(num1, num3)

jumsu = [34,78,100,68,99,67,88,60,50,44]
print(jumsu.index(100))
print(jumsu.index(99,3))
print(jumsu.index(100,1,5))

jumsu = [34,78,100,68,99,67,88,60,50,44]
print(jumsu)
jumsu.sort()
print(jumsu)
print('-'*10)
jumsu.sort(reverse=True)
print(jumsu)
print('-'*10)
jumsu.reverse()
print(jumsu)

jumsu = [34,78,100,68,99,67,88,60,50,44]
print(jumsu)
print(sorted(jumsu))
print(jumsu)
print(sorted(jumsu,reverse=True))
print(jumsu)

jumsu = [34,78,100,68,99,67,88,60,50,44]
a_jumsu = sorted(jumsu)
d_jumsu = sorted(jumsu,reverse=True)
print(jumsu)
print(a_jumsu)
print(d_jumsu)

s1 = ['name', 'age', 'address']
s2 = ['kim', 30, 'ulsan']

for i in range(3):
    t1 = (s1[i], s2[i])
    print(t1)

print(type(t1))
print(t1)

list1 = [10,20,30,40]; i = 0
for n in list1:
    list1[i] = n * 10
    i = i + 1
print(list1)

list1 = [10,20,30,40]
list1 = [ n * 10 for n in list1]
print(list1)

num_list1 = [num for num in range(1,6)]
print(num_list1)

num_list2 = [num for num in range(1,6) if num % 2 == 0]
print(num_list2)

numb1 = [10,20,30,40,50] ; num2 = 123.456
print(' 합 = ',sum(numb1))
print(' 최대값 = ', max(numb1))
print(' 최소값 = ',min(numb1))
print(' 반올림 = %7.1f' % round(num2,2))
print(' 반올림 = %7.1f' % round(num2))

# MY Mission 1
scores = [10.0, 9.0, 8.3, 7.1, 3.0, 9.0, 8.9, 10, 0]
print("제거 전 ",scores)
scores = [num for num in scores if num != max(scores)]
scores = [num for num in scores if num != min(scores)]
print('제거 후 ',scores)
print(f' 심사점수 합: {sum(scores)} 심사 점수 평균 : {sum(scores)/len(scores):5.2f}')

tu1 = ()
tu2 = (1,)
tu3 = (1,2,3,4,5)
tu4 = 1,2,3,4,5
tu5 = tuple(range(1,5))
tu6 = tuple([1,2,3,4,5])

tu1 = (10,20,30,40,50)
tu2 = ('one', 'two', 'three')
print(tu1*2)
print(tu2*2)
print(tu1+(50,))
print(tu2+('four','five'))
print(len(tu1))
print('one' in tu2)

tu1 = ('one', 'two', 'three')
tu2 = ('four',)

tu1 += tu2;
print(tu1)

# MY Mission 2
t_fruits = ('apple','mango','chrery')
print('변경 전 : ',t_fruits)
list1 = list(t_fruits)
list1[0] = 'kiwwi'
t_fruits = tuple(list1)
print(t_fruits)

t_day = (2022,6,1)
year, month, day = t_day
print('%d 년 %d 월 %d 일은 지방 선거일 입니다.' %(year,month,day))
print('{} 년 {}월 {}일은 지방 선거일 입니다.'.format(year,month,day))
print(f'{year}년 {month}월 {day}일은 지방 선거일 입니다.')

a = 90; b = 98
print('swap 전 a =',a,' b = ',b)
a, b = b, a
print('swap 후 a =',a,' b =',b)

eng = ['baby', 'sky', 'cloud', 'tree']
kor = ['아기', '하늘', '구름', '나무']
t1 = list(zip(eng,kor))
print(t1, type(t1))

eng = ['baby', 'sky', 'cloud', 'tree']
kor = ['아기', '하늘', '구름', '나무']
for dic1 in zip(eng,kor):
    print(dic1)
print(type(dic1))

for num1, str1 in zip('12345','ABCDE'):
    print(num1, str1)    
