print("happy ML")

person1 = {'이름':'이순신','나이':30,'몸무게':65}
person2 = dict(이름='이순신',나이=30,몸무게=65)
person3 = dict(zip(['이름','나이','몸무게'],['이순신',30,65]))
person4 = dict([('이름','이순신'),('나이',30),('몸무게',65)])

print(person1)
print(person2)
print(person3)
print(person4)

b_dic1 = dict()
print(b_dic1)
p_dic1 = {'name':'kim','age':30}
print(p_dic1['name'])
p_dic1['addr'] = 'Ulsan'
print(p_dic1)
print(len(b_dic1),len(p_dic1))
print('name' in p_dic1)
print('name' not in p_dic1)

list1 = [[1,'one'],[2,'two'],[3,'three']]
dic1 = dict(list1)
print(dic1)
list3 = ['kim','lee','park']
list4 = [100,89,90]
dic3 = dict(zip(list3,list4))
print(dic3)

dic = {i:str(i) for i in [1,2,3,4,5]}
print(dic)

fruits = ['apple','kiwi','cherry']
dic = {f:len(f) for f in fruits}
print(dic)

num = [1,2,3,4,5,6]
dic = {x:x*2 for x in num if x%2!=0}
print(dic)

dic2 = {'num':(1,2,3),'grade':(1,2,3,4),'hak':('A','B','C')}
print(dic2)
print(dic2.keys())
print(dic2.values())
print(dic2.items())
print(dic2.get('num'))
print(dic2.pop('num'))
print(dic2)

dic2 = {'num':(1,2,3),'grade':(1,2,3,4),'hak':('A','B','C')}
print(dic2)
print(dic2.popitem())
print(dic2)

dic2 = {'num':(1,2,3),'grade':(1,2,3,4),'hak':('A','B','C')}
print(dic2)
print(dic2.clear())
print(dic2)

dic1 = {'red':'빨강','green':'초록', 'blue':'파랑'}
print(dic1)
del dic1['red']
print(dic1)
del dic1
print(dic1)


foods = {'떡볶이':'오뎅','짜장면':'단무지','라면':'김치','피자':'피클','맥주':'땅콩','치킨':'치킨무','삼겹살':'상추' }
while True :
    myfood = input(str(list(foods.keys())))
    if myfood in foods :
        print('<%s> 궁합 음식은 <%s> 입니다.'%(myfood, foods.get(myfood)))
    elif myfood == "끝" :
        break
    else :
        print("그런 음식이 없습니다.")

dic1 = {'red':'빨강','green':'초록', 'blue':'파랑'}
dic2 = dic1
print(dic1)
print(dic2)
print(dic1, id(dic1))
print(dic2, id(dic2))

dic1 = {'red':'빨강','green':'초록', 'blue':'파랑'}
dic2 = dic1.copy()
print(dic1)
print(dic2)
print(dic1, id(dic1))
print(dic2,id(dic2))

            