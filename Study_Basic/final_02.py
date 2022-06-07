
# Mission 14
from matplotlib.pyplot import bar


def parse_file(path) :
    infile = open(path, encoding="utf-8")
    spaces = 0
    tabs = 0
    for line in infile :
        spaces += line.count(' ')
        tabs += line.count('\t')
    infile.close()
    
    return spaces, tabs

filename = input("파일 이름을 입력 하세요 : ")
spaces, tabs = parse_file(filename)
print("스페이스 수 = {} 탭의 수 = {} ".format(spaces, tabs))

# Mission 15
def process(w) :
    output = ""
    for ch in w:
        if ch.isalpha() :
            output += ch
    return output.lower()

words = set()

fname = input("파일명 입력 : ")
file = open(fname, 'r')

for line in file :
    linewords = line.split()
    for word in linewords :
        words.add(process(word))
file.close()        
print("사용된 단어의 개수 :",len(words))
print(words)
    
# Mission 16
with open('ymd.txt','r') as fd :
    w_count, m_count = 0, 0
    g1, g2 = "", ""
    while True :
        line = fd.readline().rstrip('\n')
        if not line : break
        
        jumin = list(line.strip())
        gender = int(jumin[7])
        
        if gender%2 == 0 :
            g1 = "여자"
            w_count += 1
        else :
            g2 = "남자"
            m_count += 1
    print(f'{g1}는 {w_count} 명 이고 {g2}는 {m_count} 명 이다.')
            
# Mission 17
def main() :
    with open('barcode.txt','r') as fd:
        while True:
            line = fd.readline().rstrip('\n')
            if not line : break
            bar_func(line)

def bar_func(line) :
    barcode = list(line.strip())
    e_sum, o_sum, total = 0,0,0
    
    for i in range(12) :
        if i%2==0 :
            o_sum += int(barcode[i])
        else :
            e_sum += int(barcode[i])
    total = o_sum + e_sum
    remainder = total%10
    
    if remainder==0 :
        barcode.append(0)
    else :
        barcode.append(10-remainder)
    
    print("바코드 + 검사 : ",end='')
    for i in range(12) :
        print(barcode[i],end='')
    print('     ',barcode[12])

main()

# Mission 18
import pickle
eng_kor_in={'apple':'사과','baby':'아기','sky':'하늘','tree':'나무'}

with open('eng_kor.p','wb') as fw:
    pickle.dump(eng_kor_in,fw)
with open('eng_kor.p','rb') as fr:
    eng_kor_out = pickle.load(fr)
print(eng_kor_out)    


while True :
    print("1 : 단어등록")
    print("2 : 단어검색")
    print("3 : 단어삭제")
    print("4 : 종료")
    
    sel = input("메뉴를 선택 하세요 .")
    if sel == "1" :
        eng = input("등록할 영어 단어 입력 : ")
        kor = input("영어 단어의 한글 의미 입력 : ")
        eng_kor_in[eng] = kor
        print("등록 완료 !!!")
    elif sel == "2" :
        key_search = input("검색할 영어 단어 입력 : ")
        found = 0
        if key_search in eng_kor_in :
            resul1 = eng_kor_in[key_search]
            print("검색한 영단어의 한글 의미는 ",resul1," 입니다.") 
        else : 
            print("검색하신 단어가 없습니다.")
    elif sel == "3" :
        key_del = input("삭제할 영단어를 입력 하세요.")
        if key_del in eng_kor_in :
            #del eng_kor_in[key_del]
            resul2 = eng_kor_in.pop(key_del)
            print(f'{key_del} 단어가 삭제 되었습니다.')
        else :
            print("삭제할 영단어가 없습니다.")
    elif sel == "4" :
        break
print(eng_kor_in)

# Mission 19
import pickle
eng_kor={'apple':'사과','baby':'아기','sky':'하늘','tree':'나무'}

with open('eng_kor1.p','wb') as fw:
    pickle.dump(eng_kor_in,fw)
with open('eng_kor1.p','rb') as fr:
    eng_kor_out = pickle.load(fr)
print(eng_kor_out)    


import pickle
eng_kor={}

def f_read() :
    with open('eng_kor1.p','rb') as fr:
        eng_kor = pickle.load(fr)
    print(eng_kor)
    
def menu() :
    while True :
        print("1 : 단어등록")
        print("2 : 단어검색")
        print("3 : 단어삭제")
        print("4 : 종료")
        
        sel = input("메뉴를 선택 하세요 .")
        if sel == "1" :
            eng = input("등록할 영어 단어 입력 : ")
            kor = input("영어 단어의 한글 의미 입력 : ")
            eng_kor[eng] = kor
            print("등록 완료 !!!")
        elif sel == "2" :
            key_search = input("검색할 영어 단어 입력 : ")
            found = 0
            if key_search in eng_kor :
                resul1 = eng_kor_in[key_search]
                print("검색한 영단어의 한글 의미는 ",resul1," 입니다.") 
            else : 
                print("검색하신 단어가 없습니다.")
        elif sel == "3" :
            key_del = input("삭제할 영단어를 입력 하세요.")
            if key_del in eng_kor :
                #del eng_kor_in[key_del]
                resul2 = eng_kor.pop(key_del)
                print(f'{key_del} 단어가 삭제 되었습니다.')
            else :
                print("삭제할 영단어가 없습니다.")
        elif sel == "4" :
            break
    
def f_write() :
    sel2 = input("파일에 저장 할까요?")
    if sel2 == "y" or sel2 == "Y" :
        with open('eng_kor1.p','wb') as fr:
            pickle.dump(eng_kor,fw)
    print(eng_kor)
    
def main() :
    f_read()
    menu()
    f_write()

main()