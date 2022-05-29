# 교육 2일 차 ...

a = 10; b=20; c=30
x, y = 10, 20
i = j = k = 10

print(a,b,c)
print(x,y)
print(i,j,k)

age = 49
name = 'Python'
print(age, name)
del age
print(name, age)

num1, num2, num3 = [ 10,20,30 ]
print(num1, num2, num3)

num4, num5, num6 = ( 40,50,60 )
print(num4, num5, num6)

PI=3.14; RATE=0.03
r=5; money=1000000

w=PI*r**2
print(' 원의 넓이 : %7.2f' % w)
print(f' 예금 이자 : {money*RATE:10,}')

a = 100; b = 32
print(' a + b =',a+b)
print('a - b = %d' %(a-b))
print('a * b = {0:>5,}'.format(a*b))
print('-'*10)
print('a / b = ',a/b)
print('a / b = {:.2f}'.format(a/b))
print(f'a / b = {a/b:.2f}')
print('a / b =',round(a/b,2))
print('-'*10)
print('a // b = ',a//b)
print('a % b =',a%b)
print('a ** b =',a**b)
print('a ** b = {0:e}'.format(a**b))

# Mission 1
num = int(input('세 자리 정수를 입력 하세요:'))
print(' 백의 자리 ',num//100)
num = num % 100
print(' 십의 자리 :',num//10)
print(' 일의 자리 :',num%10)

x = y = z = 0
x,y,z = 10,20,30
print(x,y,z)

x,y = y,x
print(x,y)

a = 100; b = '123'
print('정수형 a=',a, '실수형 a =',float(a),'문자열 b=',b)
print('b 의 자료형 : ',type(b))
b = int(b)
print('b 의 자료형 :',type(b))
print('a + b = ',a+b)

a = 100; b=123.456
print('a + b =',a+b) 

# Mission 2
num = int(input('정수를 입력하세요 : '))
print(num,'의 2진수 값 :',bin(num))
print(num,'의 2진수 비트단뒤 부정값 :',bin(~num))

#Mission 3
PI = 3.14
r1 = 20; r2 = 30
print('{0} cm 피자 2개의 크기는 {1:.1f} 입니다.'.format(r1,(r1*PI**2)*2))
print('{0} cm 피자 1개의 크기는 {1:.1f} 입니다.'.format(r2,r2*PI**2))

str1 = "Ulsan"; str2 = 'ICT'
print(str1, str2)
print(str1+str2)
print(str1*5)
print(str1[0], str1[1])
print(str1[-1],str1[-5])
print('T' in str2)
print(len(str1))

str1 = 'Ulsan ICT'
print(str1[0:3])
print(str1[6:])
print(str1[:5])
print(str1[-3:])
print(str1[-3:-1])
print(str1[::3])
print(str1[0:5:2])

# Mission 4
jumin_no = '740102-1******'
year = jumin_no[0:2]
month = jumin_no[2:4:1]
day = jumin_no[4:6]
print(f'출생년도 :{year}')
print(f'출생월 : {month}')
print(f'출생일자 : {day}')
print(f'{year} 년도 {month}월 {day}일은 당생 생일 입니다.')

s1 = 'python language'
print(s1)
print(s1.capitalize())
print(s1.upper())
print(s1.center(30))
print(s1.ljust(30,'*'))
print(s1.rjust(30,'*'))
print(s1.count('a'))
print(s1.count('a',0,7))
print(s1.count('a',7))
print(s1.index('a'))
print(s1.find('p'))
print(s1.find('lang'))
print(s1.startswith('python'))
print(s1.endswith('age'))

s1 = 'python language'; s2 = 'one-two-three'
print('-'.join(s1))
print(s1.split())
print(s2.split('-'))
print(s2.split('-',1))
print(s2.rsplit('-',1))

s1 = '  python  language'; s2 = 'one two three'
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())
print(s2.partition('two'))
print(s2.rpartition('one'))
print(s2.replace('two','둘'))
print(s2.zfill(30))

s1 = 'python'
list1 = list(s1)
tu1 = tuple(s1)

print(list1)
print(tu1)