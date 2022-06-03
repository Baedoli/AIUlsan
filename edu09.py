# 9일차 파일 관련 실습 ...

f = open('hello2.txt', 'w')
f.write('Hello\n')
print('Happy',file = f)
f.close()

with open('hello2.txt', 'w') as f:
    f.write('Hello222\n')
    print('Happy222',file=f)
    

