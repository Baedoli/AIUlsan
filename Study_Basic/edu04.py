# 교육 4일 차 조건문 실습 ...

num = 10
if num == 10:
    print('True')
else:
    print('False')

num = int(input('정수 입력 :'))
if num%2 == 0:
    print('짝수')
else:
    print('홀수') 

x = int(input(' First Input :'))
y = int(input(' Second Input :'))

max1 = (x if x > y else y )
min1 = (y if x > y else x )

print(' big = %d, small = %d ' %(max1, min1) )

# Mission 1
score = int(input('성적을 입력하세요 :'))
if score >= 90:
    print(' score is A')
elif score >= 80:
    print(' score is B')
elif score >= 70:
    print(' Scroe is C')
elif score >= 60:
    print(' Score is D')
else :
    print(' Score is F')

# Mission 2
PI = 3.14
r1 = 20; r2 = 30
a1 = (PI*r1**2)*2; a2 = PI*r2**2
if a1>a2:
    print('small size is Best Choice!!')
elif a1==a2:
    print('Big Small is equal size !!!')
else :
    print('Big size is Best Choice!!')
print('small size :',a1,' Big size :',a2)

# Mission 3
age = int(input('나이를 입력 하세요 :'))

if age >= 8 :
    height = int(input('키를 입력하세요 :'))
    if height >= 140 :
        print('고속 롤러코스트 입장 !!')
    else :
        print('저속 롤러코스트 입장 !!')
else :
    print('입장 불가')

# Mission 4
a = [38, 21, 53, 62, 19, 67, 99, 123, 23, 300] 
small1 = a[0]
large1 = a[0]
for i in range(0,len(a)) :
    if large1 < a[i] :
        large1 = a[i]
    if small1 > a[i] :
        small1 = a[i] 

print(f'max : {large1} min : {small1}')           

a, b = map(int, input('숫자 두개를 입력하세요 :').split() )
print(a+b)

# Mission 5
num = int(input('약수를 구할수 있는 수 입력 : '))
list1 = [x for x in range(1,num+1)]
list2 = []
print(list1)
for x in range(0,len(list1)):
    if num%list1[x]==0 :
       list2.append(list1[x])
print(list2)

# Mission 6
a,b,c = map(int,input('세변의 결이 입력').split())
if a+b<=c or b+c<=a or c+a<=b :
    if a==0 or b==0 or c==0 :
        print('삼각형이 아님')
elif a**2+b**2==c**2 :
    print('직각 삼각형')
elif a==b==c :
    print('정 삼각형')
elif a==b or b==c or c==a :
    print('이등변 삼각형')
else :
    print('일반 삼각형')
        
# Mission 7
import random
computer = random.randint(0,2)
 user = int(input('하나를 선택 ?(0:가위 1:바위 2:보'))
print(f'컴퓨터 :{computer} 사용자 :{user}')
differ = computer-user
if computer==0 and user==2 :
    differ *= -1
elif computer==2 and user==0 :
    differ *= -1

if differ==0 :
    print('무승부')
elif differ < 0 :
    print('패배')
else :
    print('승리') 

# Mission 8
import random
import sys
computer = random.randint(0,2)
 user = int(input('하나를 선택 ?(0:가위 1:바위 2:보'))
if user != 0 and user != 1 and user != 2 :
   user = int(input('하나를 선택 ?(0:가위 1:바위 2:보')) 

print(f'컴퓨터 :{computer} 사용자 :{user}')
differ = computer-user
if computer==0 and user==2 :
    differ *= -1
elif computer==2 and user==0 :
    differ *= -1

if differ==0 :
    print('무승부')
elif differ < 0 :
    print('패배')
else :
    print('승리') 

# Mission 9
jumin = input('주민번호 입력 (200101-4) :')
year = int(jumin[0:3])
sex = int(jumin[8:])
print(year, sex)
if year >= 50 and year <= 99 :
    if sex == 1 :
        print('남자')
    elif sex == 2 :
        print('여자') 
else :
    if sex == 3 :
        print('남자') 
    else :
        print('여자')
print(year,sex)    
                        
jumin = input('주민 번호를 입력하세요. (221011-4) : ')
year = int(jumin[0:2])
pre_year = int(jumin[0:2])
sex = int(jumin[7:])
if sex%2==0 :
    pre_year = (19 if sex == 2 else 20)
    print(f'출생년도 : {pre_year}{year} 년 인 여성 입니다.') 
else :
    pre_year = (19 if sex == 1 else 20)
    print(f'출생년도 : {pre_year}{year} 년 인 남성 입니다.')          

id1_ = 'bae123'; pass1_ = 'p123'
id2_= input('아이디를 입력하세요.')
pass2_ = input('비밀번호를 입력하세요.')
pass_cnt = 0
while True :
    if pass_cnt == 3 :
        id2_= input('아이디를 입력하세요.')
        pass2_ = input('비밀번호를 입력하세요.')
        pass_cnt = 0
    if id1_ == id2_ :
        if pass1_ == pass2_ :
            print('로그인 성공')
            break
        else :
            pass_cnt += 1
            print(f'비밀번호를 {pass_cnt}번 잘못 입력 하셨습니다.')
            pass2_ = input('비밀번호를 입력하세요.')        
    else :
        print('아이디가 틀렸습니다.')
        id2_= input('아이디를 입력하세요.')
        
