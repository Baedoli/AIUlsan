print('happy ML')

x = {'a':10, 'b':20, 'c':30, 'd':40}
print(x)
x.update(a = 90) 
x.update(e = 50)
x.update(a=900, f=60)

y = {1:'one', 3:'three'}
y.update([[2,'TWO'],[4,'Four']])
print(y)
y.update(([6,'fix'],[7,'seven']))
print(y)

z = {3:'three',4:'four'}
z.update(zip([1,2],['one','two']))
print(z)

person1 = {'이름':'이순신','나이':30,'몸무게':65}
for key in person1 :
    print('{} : {}'.format(key, person1[key]))
    print(key)

person1 = {'이름':'이순신','나이':30,'몸무게':65}
for key in person1 :
    print('{} : {}'.format(key, person1.get(key)))

person1 = {'이름':'이순신','나이':30,'몸무게':65}
for key1, value1 in person1.items() :
    print(key1, value1)
    
person1 = {'이름':'이순신','나이':30,'몸무게':65}
for key1 in person1.keys() :
    print(key1)

word = 'UlsanCity'
word_count = {uc:word.count(uc) for uc in word}    
print(word_count)

dic1 = {'kim':99, 'lee':88, 'park':66}
dic2 = {}
dic2 = {name:score for name, score in dic1.items() if score > 70}
print(dic2)

arr = [6,5,6,4,4,1,1,3,3,4,5,6,9,8,9,7]
result1 = dict.fromkeys(arr)
print(result1)
result2 = list(result1)
print(result2)

arr = ['a','b','c','d']
x = dict.fromkeys(arr)
print(x)
y = dict.fromkeys(x,100)
print(y)

val = 100
for key in y.keys() :
    val += 100
    #y.update(key=val)
    
arr = [6,5,6,4,4,1,1,3,3,4,5,6,9,8,9,7]
result = []
for v in arr :
    if v not in result :
        result.append(v)
print(result)

# My Mission 1
persion1 = {}
for i in range(5) :
    nam_ = input('이름을 입력하세요 :')
    number_ = input('전화번호를 입력하세요 :')  
    persion1[nam_] = number_
else :
    print('입력완료') 

name = input('이름을 검색 하새요')
if name in person1 :
    print(name,' 학생의 번호는 ',persion1[name])
else :
    print('존재하지 않는 학생 입니다.')

planet = {
    'Mercury' : {
        'mean_radius' : 2439.7, 
         'mass':3.3022E+23, 
         'orbital_period':87.969
        },
    'Venus' : {
        'mean_radius' : 6051.8, 
        'mass':4.8676E+24, 
        'orbital_period':224.70069
    },
    'Earth' : {
        'mean_radius' : 6371.0, 
        'mass':5.97219E+24, 
        'orbital_period':365.25641
    },
    'Mars' : {
        'mean_radius' : 3389.5, 
        'mass':6.4185E+23, 
        'orbital_period':686.9600
    } }

for key, value in planet.items() :
    print(key)
    for key2, value2 in value.items() :
        print(key2, value2)

set0 = {}
set1 = {1,2,3,4,5}
tu1 = (1,2,3,4)
set2 = set(tu1)
lis1 = [1,2,3,4]
set3 = set(lis1)
print(set0, set1)
print(set2, set3)

num1 = {'one','two','three'}
print(num1, type(num1))
num2 = {1,2,3,1,2,3,4,5}
print(num2, type(num2))
num3 = {1,2,3,(1,2,3),4}
print(num3, type(num3))

num1 = {'one','two','three'}
num2 = {1,2,3}
print(num1)
num1.add('four')
num1.update({'five','six'})
num2.update({7,8,9})
print(num2)

num1 = {'one','two','three'}
num1.remove('two')
print(num1)

num1 = {'one','two','three'}
num1.clear()
print(num1)

num1 = {'one','two','three'}
num2 = num1.copy()
print(num2)

num1 = {'one','two','three'}
num1.discard('two')
print(num1)

num1 = {'one','two','three'}
num2 = {'four','five','three'}
num3 = num1.difference(num2)
print(num3)
num4 = num2.difference(num1)
print(num4)
print(num1)
print(num2)

num1 = {'one','two','three'}
num2 = {'four','five','three'}
num1.difference_update(num2)
print(num1)
print(num2)

t1 = input("입력 테스트")
w1 = t1.split(" ")
u1 = set(w1)

print('사용된 단어의 수 :',len(u1))
print(u1)

s1 = input(' Fist : ')
s2 = input(' Second : ')

list1 = list(set(s1) & set(s2))
list2 = sorted(list1)

print('\n 공통되는 글자 :', end=" ")
for i in list2 :
    print(i, end=" ")
    
