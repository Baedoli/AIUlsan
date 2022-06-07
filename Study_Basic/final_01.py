
# Mission 1
s1 = input("문자열(문장)을 입력하세요 : ")
print("입력된 문자열 : ",s1)
s2 = input('반복 개수를 알고자 하는 문자를 입력 하세요 : ')  
print(f'{s1} : {s2} 글자는 {s1.count(s2)} 번 나타남. 처음 인덱스 위치는 {s1.find(s2)} 이다.')

# Mission 2
str1 = "Park(ulsan), Lee(ulsan), Cho(ulsan)"
src = input("수정 전 문자열 : ")
target = input("수정 후 문자열 : ")
new_str = str1.replace(src,target)
count1 = str1.count(src)

print("주어진 문자열 :{} \n".format(str1))
print("수정된 문자열 :{} ".format(new_str))
print('{} 문자열은 모두 {} 번 수정 했습니다.'.format(target,count1))

# Mission 3
def removeMarks(str1) :
    sep1 = ['.',',','!','?',':',';']
    for mark in sep1 :
        str1 = str1.replace(mark," ")
    return str1

str1 = input("여러 단어로 이루어진 문자열을 입력 하세요 : ")
str1 = removeMarks(str1).lower()
print("구두점 분리 후 ",str1)
words = str1.split()
print("분리된 단어 리스트 ",words)
words.sort()
print("정렬 후 ",words)
words.sort(reverse=True)
print(" 내림차순 정렬 후 ",words)

# Mission 4
sales = [100,121,120,130,140,120,122,123,190,125]
drop = 0
for i in range(len(sales)-1) :
    if sales[i] > sales[i+1] :
        drop += 1
print('일일 매출 기록 : ',sales)
print('지난 {} 일 동안 전일대비 매출이 감소한 날은 {} 입니다.'.format(len(sales), drop))

# Mission 5
str1 = "sky hello hi good morning"
str1 = str1.upper()
print(str1)
dic1 = {}  # dictionary 로 활용 ...

for ch in str1 :
    if 'A' <= ch and ch <= 'Z' :
        if ch in dic1 :
            dic1[ch] += 1
        else :
            dic1[ch] = 1

for k in dic1.keys() :
    print('%s -> %s'%(k, dic1[k]))

# Mission 6
from operator import itemgetter
from random import random
str1 = "sky hello hi good morning"
str1 = str1.upper()
print(str1)
dic1, list1 = {},[]  # dictionary 로 활용 ...

for ch in str1 :
    if 'A' <= ch and ch <= 'Z' :
        if ch in dic1 :
            dic1[ch] += 1
        else :
            dic1[ch] = 1

list1 = list(dic1.items())
list1.sort(key=itemgetter(1), reverse=True)   # import 활용 할 경우 ..
list1.sort(key=lambda x : x[1], reverse=True) # import 하지 않고 lambda (람다) 뢀용할 경우 ..

for char1, count1 in list1 :
    print('%s -> %s'%(char1, count1))
    
# Mission 7
A_city = (100,150,230,120,180,100,140,95,81,21,4)
B_city = (300,420,530,420,400,300,40,5,1,1,1)

p_A = sum(A_city[2:])
p_B = sum(B_city[2:])

print('마을 A 와 B에 보낼 투표함의 개수는 {}, {} 입니다.'.format(p_A,p_B))

A_city = (100,150,230,120,180,100,140,95,81,21,4)
B_city = (300,420,530,420,400,300,40,5,1,1,1)

oldA = sum(A_city[7:])
oldB = sum(B_city[7:])


# Mission 8
scores = (('이순신',88,95,90),('김유신',85,90,95),('홍길동',70,90,80),('허생원',90,90,95))
student_dic = {}

for val in scores:
    avg = (val[1]+val[2]+val[3])/3
    student_dic[val[0]] = avg

print('이름     평균성적')
print('--------------')
for k in student_dic.keys() :
    print('{}   {:10.2f}'.format(k,student_dic[k]))

scores = (('이순신',88,95,90),('김유신',85,90,95),('홍길동',70,90,80),('허생원',90,90,95))
student_dic = {}
name, kor, math, science = zip(*scores)

for i in range(len(scores)) :
    student_dic[name[i]] = (kor[i]+math[i]+science[i])/3

print('이름     평균성적')
print('--------------')
for name in student_dic:
    print('{:3} {:13.2f}'.format(name, student_dic[name]))    

# tuple 로 구성된 내용을 평균을 구하고 
# 리스트로 변환 후 정렬 하고 출력 한다 ..
scores = (('이순신',88,95,90),('김유신',85,90,95),('홍길동',70,90,80),('허생원',90,90,95))
student_dic = {}
student_list = []
name, kor, math, science = zip(*scores)

for i in range(len(scores)) :
    student_dic[name[i]] = (kor[i]+math[i]+science[i])/3

student_list = list(student_dic.items())
student_list.sort(key=lambda x:x[1],reverse=True)

print('이름     평균성적')
print('--------------')
for name, average in student_list:
    print('{:3} {:13.2f}'.format(name, average))    

# Mission 9
import random
s ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?" 
n_digit = int(input("몇자리의 비밀번호를 원하십니까?"))
otp = "".join(random.sample(s,n_digit))
print("생성된 암호 : ",otp)

# Mission 10
def cursor_string(txt, lst, char1) :
    for word in lst :
        txt = txt.replace(word, char1*len(word))
    return txt

t1 = input("문자열을 입력 하세요 : ")
d1 = input("금칙어를 입력 하세요 : ").split()

print(cursor_string(t1, d1, "*"))

# Mission 11
import re
tweet = input("메세지를 입력 하세요 :")
tweet = re.sub('RT','',tweet)
print(tweet)
tweet = re.sub('#\S+','',tweet)
tweet = re.sub('@\S+','',tweet)
print(tweet)

# Mission 12
while True :
    try :
        fname = input("파일명을 입력사헤요.").strip()
        infile = open(fname, 'r')
        break
    except IOError :
        print("파일 : ",fname," 을 열수가 없습니다. 다시 입력 하세요.")

print("파일이 성공적으로 열렸습니다.")
infile.close()

# Mission 13
# 반크는 4일 “판소리는 한 명의 소리꾼이 북 치는 사람의 장단에 맞추어 창, 말, 몸짓을 섞어가며 긴 이야기를 엮어가는 한국의 전통 소리”라며 “그 역사는 신라 때까지 올라갈 만큼 오래됐으며, 1964년 한국 국가무형문화재, 2008년 유네스코 인류무형문화유산 목록에 등재됐다”고 밝혔다.
in_file = open("tt4.txt",'w',encoding="utf-8")
tweet = input("문자열을 입력 하세요 : ")
in_file.write(tweet)
in_file.close()
        
f = open("tt4.txt",'r',encoding='utf-8')
words = f.read().split()
print(max(words))
print(max(words,key=len))
print(len(max(words,key=len)))
max_len = len(max(words,key=len))
print([word for word in words if len(word) == max_len ])
f.close()





