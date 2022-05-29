# 교육 1일 차 ...
# 교육 준비 잘 합시다 ..
from unicodedata import name


print(1,2,3)
print(1,2,3, sep=',')
print(1,2,3, sep='\n')
print('Program')
print('\n줄바끔\n연습')
print('\t탭\t연습')
print('"강조"효과')
print("\"강조\"효과")
print('우리는','파이썬','프로그램을 좋아합니다.')
print('우리는'+'파이썬'+'프로그램을 좋아합니다.')
print("우리는","파이썬","프로그램을 좋아합니다.",sep='/')
who = "울산정보산업진행원"
what = "인공 지능 교육 과정"
where = "울산정보산업진흥원 컴퓨터실"
when = "2022년 5월 23일 오후 6시"
print("=================================")
print("=                               =")
print("=           파이썬 교육            =")
print("=                               =")
print("=================================")
print('')
print(who,' 에서 ',what,' 을 진행 합니다.')
print('장소는 ',where,' 입니다.')
print('날짜와 시간은 ',when,' 입니다.')

print('이름은 %s 입니다' %'배성호')
print('이름은 %s 나이는 %d 입니다.'%('배성호',49))
print('%d' %123)
print('%5d' %123)
print('%05d' %123)
print('%d%%' %30)

print('Hello {0} '.format('ulsan'))
print('hello {0} hi {1}'.format('ulsan','sungho'))
print('hello {0} {1} {2}'.format('bae','sung','ho'))

print('당산의 나이는 {} 입니다'.format(49))
print('당신의 이름은 {} 이고 나이는 {} 입니다.'.format('bae',49))
print('당신의 이름은 {name} 이고 나이는 {age} 입니다'.format(name='bae',age=49))

for a in range(2,4):
    for b in range(1,10):
        print('{0} * {1} = {2}'.format(a,b,a*b))

for a in range(2,4):
    for b in range(1,10):
        print('{0} * {1} = {2:2}'.format(a,b,a*b))        

print('[{0:05d}] [{1:05d}] [{2:05d}]'.format(1,-2,3))
print('[{0:✶<5d}] [{1:✶<5d}] [{2:✶<5d}]'.format(1,-2,3))
print('[{0:✶>5d}] [{1:✶>5d}] [{2:✶>5d}]'.format(1,-2,3))
print('[{0:✶^5d}] [{1:✶^5d}] [{2:✶^5d}]'.format(1,-2,3))

