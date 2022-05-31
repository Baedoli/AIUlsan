# Function Study
def main() :
    radius = int(input('원의 반지름을 입력 하세요 :'))
    result = get_area(radius)
    print(result)    

def get_area(radius) :
    area = 3.14*radius**2
    return area

main()

def get_area(val1) :
    PI = 3.14
    area = PI*val1**2
    return area

r1 = 20; r2 = 30
a1 = get_area(r1)
a2 = get_area(r2)
if a1>a2 :
    print(' 작은 피자가 유리 ')
else :
    print('동일 하거나 큰 피자가 유리 하다.')
print('큰 피자 크기는 %d 이고 작은 피자의 크기는 %d 이다.'%(a2,a1)) 

def get_yaksu(val1, val2) :
    if val1%val2 == 0 :
        print(val2,end=" ")

num = int(input('약수를 구할 값 입력 :'))
for x in range(1,num+1) :
    get_yaksu(num,x)

def multi(num1, num2) :
    list1 = []
    s1 = num1 + num2
    s2 = num1 * num2
    list1.append(s1)
    list1.append(s2)
    return list1

def main(val1, val2) :
    myList = []
    hap, mul = 0, 0
    myList = multi(val1, val2)
    hap = myList[0]
    mul = myList[1]
    print(' 첫번째 수 %d 두번째 수 %d 의 합은 %d 곱은 %d 입니다.'%(val1, val2, hap, mul) )
 
main(100,200)   
 
def calc_sosu(val1, val2) :
    for x in range(val1, val2) :
        p = True
        for y in range(val1,x) :
            if x%y == 0 :
                p = False
        if p==True :
            print(x, end=" ")

def main() :
    cnt1 = int(input('First input : '))
    cnt2 = int(input('Second input : '))
    calc_sosu(cnt1,cnt2)

main()    

def calc(num1, num2) :
    return num1+num2, num1-num2, num1*num2, num1/num2

def main() :
    n1 = int(input(' 숫자 1 입력 :'))
    n2 = int(input(' 숫자 2 입력 :'))
    add1, sub1, mul1, div1 = calc(n1, n2)
    print(f'덧셈 : {add1} 뺄셈 : {sub1} 곱셈 : {mul1} 나눗셈 : {div1:.2f}')

main()    

