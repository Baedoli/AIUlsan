# Mission 1 : 자판기 프로그램 
menu = ['콜라','사이다','환타','커피','생수']
price = [500,500,600,600,400]

print('*** 자판기 메뉴 ***')
for i in range(5) :
    print(f'{i+1} : {menu[i]} {price[i]}')
    
print()
money = int(input('돈을 입력하세요 : '))
print()

while True :
    menu_choice = int(input('메뉴를 입력하세요.'))-1
    if menu_choice == -1 :
        print(f'자판기 종료 잔액 : {money} 반환 ')         
        break
    if (money-price[menu_choice]) >= 0 :
        print(f'메뉴 : {menu[menu_choice]} 구입 완료.')
        money = money - price[menu_choice]
        print(f'잔액 : {money}')
        if money == 0 :
            break
    else :
        print('잔액 부족')
        print(f'잔액 : {money}')

# Mission 2
# 미니 프로젝트 2 : 점수에 순위를 출력
score = [45, 92, 88, 34, 88, 95, 82, 59, 70, 76] 
rank = []
tmp_rank = 1
tmp_score = 0

for i in range(10) :
    tmp_score = score[i]
    tmp_rank = 1
    for j in range(10) :
        if i != j :
            if tmp_score < score[j] :
                tmp_rank += 1
    rank.append(tmp_rank)

print('No Score rank')
print('--------------')
for i in range(10) :
    print('%2d     %2d     %2d'%(i+1, score[i], rank[i]))

# Mission 3
# 미니 프로젝트 3 : 바코드 검사 수 계산 
barcode = [8,8,0,1,0,5,1,1,4,8,8,5]
e_sum = 0; o_sum = 0; total = 0
for i in range(0,12,2) :
    e_sum += barcode[i]
for i in range(1,12,2) :
    o_sum += barcode[i]
total = e_sum + (o_sum*3)
total = total % 10
print(total)         

# 두번째 옵션 ...
barcode = [8,8,0,1,0,5,1,1,4,8,8,5]
e_sum = 0; o_sum = 0; total = 0
for i in range(12) :
    if (i+1)%2==0 :
        o_sum += barcode[i]
    else :
        e_sum += barcode[i]    

total = e_sum + (o_sum*3)
total = total % 10
print(' 검사수 :',total)         
