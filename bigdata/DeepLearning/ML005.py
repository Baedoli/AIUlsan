import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

length = bream_length+smelt_length
weight = bream_weight+smelt_weight

fish_data = [[l,w] for l,w in zip(length,weight)]
fish_data

# target data 1:도미 0:빙어 라고 설정 하고 target data 만들어 준다 ..
fish_target = [1]*35+[0]*14

kn = KNeighborsClassifier()
kn.fit(fish_data,fish_target)
kn.score(fish_data,fish_target)

plt.scatter(bream_length,bream_weight)
plt.scatter(smelt_length,smelt_weight)
plt.scatter(30,600,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 길이가 30, 무게가 600 이라는 고기는 무엇일까 예측 : 값 array[1] 1: 도미라고 예측 함.
print(kn.predict([[30,600]]))

train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]

# 일렬로 도미 와 빙어를 나열 해서 억지로 섞지 않고 학습하면 0 이다 ..
kn.fit(train_input,train_target)
kn.score(test_input,test_target)

np.random.seed(42)
index = np.arange(49)
np.random.shuffle(index)

input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(test_input[:,0], test_input[:,1])
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn.fit(train_input,train_target)
kn.score(test_input,test_target)

print(kn.predict(test_input))
print(test_target)

fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0,
               31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0,
               35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8,
               10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0,
               500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0,
               700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7,
               7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

fish_data = np.column_stack((fish_length,fish_weight))
fish_target = np.concatenate((np.ones(35), np.zeros(14)))

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

print(train_input.shape, test_input.shape)
print(train_target.shape, test_target.shape)

# 무작위로 stratify 값을 주기 않고 지정 하면 0 이 3개 본포 ,,,
print(test_target)

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target,stratify=fish_target, random_state=42)

# finsh_target 을 설정하면 0 의 비율을 target 의 비율을 가져와서 설정 하므로
# 주지 않았을때 보다 비율이 더 정확해져서 score 가 더 좋게 나온다..
print(test_target)

kn.fit(train_input,train_target)
kn.score(test_input,test_target)

print(kn.predict([[25,150]]))

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25,150,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 추축값 의 거리와 인텍스 표시 ..
distances, indexes = kn.kneighbors([[25, 150]])
print(distances)
print(indexes)

plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25,150,marker='^')
plt.scatter(train_input[indexes,0],train_input[indexes,1],marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# x 값을 일렬로 표시 되는거 보니 x 는 거의 영향을 미치지 못한다.
# 정규화 필요 ..
plt.scatter(train_input[:,0],train_input[:,1])
plt.scatter(25,150,marker='^')
plt.scatter(train_input[indexes,0],train_input[indexes,1],marker='D')
plt.xlim((0,1000))
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

mean = np.mean(train_input,axis=0)
std = np.std(train_input,axis=0)

train_scaled = (train_input-mean)/std

# 25,150 도 전처리 해줘야 동일 선상에 비교가 가능 하다 ..
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(25,150,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

new = ([25,150] - mean)/std

# 25,150 을 전처리 하고 나서의 비율 ...
plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(new[0], new[1],marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn.fit(train_scaled,train_target)
test_scaled = (test_input - mean) / std

distances, indexes = kn.kneighbors([new])

plt.scatter(train_scaled[:,0],train_scaled[:,1])
plt.scatter(new[0],new[1],marker='^')
plt.scatter(train_scaled[indexes,0],train_scaled[indexes,1],
            marker='D')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
                         21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
                         23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
                         27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
                         39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
                         44.0])
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
                         115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
                         150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
                         218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
                         556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
                         850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
                         1000.0])

plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

train_input, test_input, train_target, test_target = train_test_split(perch_length,perch_weight,random_state=42)
print(train_input.shape)

test_array = np.array([1,2,3,4])
test_array = test_array.reshape(-1,1)

# 싸이킷런은 2차원 배열만 인식 ..
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

knr = KNeighborsRegressor()
knr.fit(train_input,train_target)
knr.score(test_input,test_target)

# 테스트 set 에 대한 예측을 만듭니다.
test_prediction = knr.predict(test_input)
mae = mean_squared_error(test_target, test_prediction)
print(mae)

knr.score(train_input,train_target)
knr.score(test_input,test_target)
# 과소적합 : train 결과값 보다 test 결과값이 높다면 과소 적합 : train 이 너무 적게 학습 ...
# 위의 결과값은 과소적합 ..

knr.n_neighbors = 3
knr.fit(train_input,train_target)
knr.score(train_input, train_target)
knr.score(test_input, test_target)
# 인근 값을 줄여 보니 위의 보다 결과가 반대로 나와 과대적합으로 변경 되었다...

x = np.arange(5, 45).reshape(-1,1)
for n in [1,5,10]:
    knr.n_neighbors = n
    knr.fit(train_input,train_target)
    prediction = knr.predict(x)
    plt.scatter(train_input,train_target)
    plt.plot(x,prediction)
    plt.title('n_neighbore = {}'.format(n))
    plt.xlabel('length')
    plt.ylabel('weight')
    plt.show()

# 길이 예측 ..
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)

knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input, train_target)
knr.predict([[50]])

distances, indexes = knr.kneighbors([[50]])
plt.scatter(train_input, train_target)
plt.scatter(train_input[indexes], train_target[indexes],marker='D')
plt.scatter(50,1033,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

lr = LinearRegression()
lr.fit(train_input, train_target)
print(lr.predict([[50]]))
print(lr.coef_, lr.intercept_)
# coef_ : 기울기, intercept_ : 절편

plt.scatter(train_input, train_target)
plt.plot([15,50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])
plt.scatter(50,1241.8,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(train_input.shape)
train_input

train_poly = np.column_stack((train_input **2, train_input))
test_poly = np.column_stack((test_input ** 2, test_input))

print(train_poly.shape)
lr.fit(train_poly, train_target)
print(lr.predict([[50**2, 50]]))

print(lr.coef_, lr.intercept_)

# 구간별 직선을 그리기 위해 15에서 49까지 정수 배열을 만듭니다.
point = np.arange(15, 50)

plt.scatter(train_input, train_target)
plt.plot(point, 1.01*point**2 - 21.6*point +116.05)
plt.scatter(50, 1574, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()