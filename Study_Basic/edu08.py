# 8일차 함수 ..

def isprime(num) :
    for y in range(2,num) :
        if num%y==0 :
            return False
    return True

def main() :
    num = int(input('2~ 소수를 구할 수 입력:'))
    cnt1 = 0
    for x in range(2, num+1) :
        if isprime(x) == True:
            cnt1 += 1
            #print(x,end=" ")
            
    print(f'소수의 개수는 {cnt1} 입니다.')

main()

n=100000
number = [False, False]+[True]*(n-1)
print(number)
primes = []
cnt = 0
for i in range(2, n+1): 
    if number[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            number[j] = False 
            cnt += 1
print(f'소수의 개수는 {cnt} 입니다.')
#print(primes)

def main() :
    n = int(input("1부터 소수를 구할 개수를 입력 : "))
    print(f'1 부터 {n} 까지의 소수의 개수는 {prime_ear(n)}')

def prime_ear(n) :
    number = [False, False]+[True]*(n-1)
    primes = []
    for i in range(2, n+1): 
        if number[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                number[j] = False 
    return len(primes)

main()

def greet(name, msg='반갑습니다') :
    print('Hi !',name,msg)

greet('kim')
greet('kim', 'good morning')

def sub(x,y,z) :
    print('x = ',x,'y = ',y,'z = ',z)

sub(x=10,y=20,z=30)
sub(x=10,z=30,y=20)

def add(*num1) :
    sum1 = 0
    for n in num1:
        sum1 += n
    return sum1

print(add(10,20))
print(add(10,20,30))

def fun1() :
    x = 100
    print(x)

def fun2() :
    x = 200
    print(x)

fun1()
fun2()

x = 100
def fun1() :
    global x
    x = 200
    print(x)

fun1()
print(x)

# Mission 4
def main() :
    a, b, c = map(int, input('세 변의 길이 입력:').split())
    sharp_ = check_triangle(a,b,c)
    print(sharp_)

def check_triangle(a,b,c) :    
    if(a+b<=c or a+c<=b or b+c<=a):
        return '삼각형이 아님'
    elif(a==b and b==c):
        return '정삼각형'
    elif(a==b or a==c or b==c):
        return '이등변 삼각형'
    elif(a**2+b**2 ==c**2 or a**2+c**2 ==b**2 or b**2+c**2 ==a**2):
        return '직각삼각형'
    else:
        return '일반삼각형'

main()    

g = lambda x,y : x+y
print(g(10,20))

g = lambda x:x**2
print(g(3))

def sub(a,b) :
    return a-b

print('{} - {} = {}'.format(200,100,sub(200,100)))

print('{} - {} = {}'.format(200,100,(lambda x,y:x-y)(200,100)))

a = [1,2,3,4,5,6,7]
square_a = []
for n in a :
    square_a.append(n**2)

print(square_a)

def square(x) :
    return x**2

a = [1,2,3,4,5,6,7]
square_a = list(map(square,a))

print(square_a)

a = [1,2,3,4,5,6,7]
square_a = list(map(lambda x: x**2,a))
print(square_a)

a = [1,2,3,4,5,6,7]
[x**2 for x in a]
#print([x**2 for x in a])

a = [1,2,3,4,5]
f = lambda x,y : x+y
list(map(f,a,a))

a = [1,2,3,4,5]
list(map(lambda x:x**2 if x%2==0 else x, a))

a = [1,2,3,4,5]
[x**2 if x%2==0 else x for x in a]

# Mission 5 _ 1
list1 = ['a','b','c','d','e','f']
print('upper list1 =',str(list1).upper())

def to_upper(x) :
    return str(x).upper()
list1 = ['a','b','c','d','e','f']
print('upper list1 =',to_upper(list1))

def to_upper(x) :
    return x.upper()

list1 = ['a','b','c','d','e','f']
upper_list = list(map(to_upper,list1))
print(upper_list)

# Mission 5 _ 2
list1 = ['a','b','c','d','e','f']
upper_list = list(map(lambda x : x.upper() ,list1))
print(upper_list)

list1 = [1,2,3,4,5,6,7,8,9,10]
even_list1 = []

for n in filter(lambda x : x%2==0, list1) :
    even_list1.append(n)

print('even_list = ',even_list1)    

def adult_func(c) : 
    if c >= 19 :
        return True
    else :
        return False

ages = [34,39,20,18,13,54]
print('성년 리스트')
for i in filter(adult_func,ages) :
    print(i,end=" ")

ages = [34,39,20,18,13,54]
print('성년 리스트')
for a in filter(lambda x : x >= 19, ages) :
    print(a, end=" ")
    
n_list = [-30,45,-5,-90,20,53,77,-36]
minus_list = []
for n in filter(lambda x: x < 0, n_list) :
    minus_list.append(n)

print('음수 리스트 :',minus_list)    

n_list = [-30,45,-5,-90,20,53,77,-36]
minus_list = list(filter(lambda x:x<0,n_list))
print('음수 리스트 :',minus_list)

from functools import reduce

from Study_Basic.edu08_ext import sub_ext08_1, sub_ext08_2
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

x = 0
for y in [1,2,3,4,5] :
    x += y

print(x)    

from functools import reduce
x = reduce(lambda x,y : x+y, range(1,101))
print('1에서 100까지 합 : ',x)

from functools import reduce
x = reduce(lambda x,y : x*y, range(1,11))
print('1에서 100까지 곱 : ',x)

import math as ma
print(f'12,18 두수의 최대공약수 :{ma.gcd(12,18)}')
print(f'pow(2,5) :{ma.pow(2,5)}')
print(f'sqrt(9) :{ma.sqrt(9)}')

import math as ma
for n in range(1,11) :
    print('{:2d} ** {:2d} = {:9.1f}'.format(4,n,ma.pow(4,n)))
    
from math import *
print(f'12,18 두수의 최대공약수 :{gcd(12,18)}')
print(f'pow(2,5) :{pow(2,5)}')
print(f'sqrt(9) :{sqrt(9)}')

import edu08_ext;

print(sub_ext08_1(3,4))
print(sub_ext08_2(4,3))


