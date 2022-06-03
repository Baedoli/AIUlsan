# 9일차 파일 관련 실습 ...

f = open('hello2.txt', 'w')
f.write('Hello\n')
f.writelines(['Before\n','After\n'])
f.writelines('\n'.join(['BlockDMask','python','blog']))
print('Happy',file = f)
f.close()

with open('hello2.txt', 'a') as f:
    f.write('Hello222\n')
    print('Happy222',file=f)
    f.writelines(['Before!!!\n','After!!!\n'])
    f.writelines('\n'.join(['BlockDMask','python','blog']))

f = open('hello2.txt','r')
t = f.read()
print(t)
f.close()

with open('hello2.txt','r') as f:
    t = f.read()
    print(t)
    
fd = open('hello.txt','r')
while True :
    line = fd.readline()
    if not line : break
    print(line) 
fd.close()

with open('hello.txt','r') as fd:
    while True :
        line = fd.readline().rstrip('\n')
        if not line : break
        print(line)
    
with open('hello.txt','r') as fd:
    line = fd.readline().rstrip('\n')
    while line != "" :
        print(line)
        line = fd.readline().rstrip('\n')
        
fd = open('hello.txt','r')
line = fd.readlines()
print(line)
fd.close()

fd = open('hello.txt','r')
list1 = fd.readlines()
for list in list1 :
    print(list.rstrip('\n'))
fd.close()    

with open('hello.txt','r') as fd:
    list1 = fd.readlines()
    for list in list1:
        print(list.rstrip('\n'))
        
fd = open('hello.txt','r')
for line in fd :
    word_list = line.split()
    for word in word_list:
        print(word)
fd.close()                

with open('hello.txt','r') as fd:
    for line in fd:
        word_list = line.split()
        for word in word_list :
            print(word)

fd = open('hello.txt','r')
line = str(fd.readlines())
word_list = line.split()
for word in word_list:
    print(word)
fd.close()                

fd = open('hello.txt','r')
line = fd.readline()
word_list = line.split()
for word in word_list:
    print(word)
fd.close()                
                    