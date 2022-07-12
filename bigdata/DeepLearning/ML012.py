import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import os
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_validate

path = os.getcwd()
path = path+'/data/'

fruits = np.load(path+'fruits_300.npy')
fruits_2d = fruits.reshape(-1,100*100)

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_2d)

print(np.unique(km.labels_, return_counts=True))

def draw_fruits(arr, ratio=1):
    n = len(arr)  # n은 샘플 개수입니다.
    rows = int(np.ceil(n/10))
    cols = n if rows<2 else 10
    fig, axs = plt.subplots(rows, cols,
                            figsize=(cols*ratio, rows*ratio),
                            squeeze=False)
    for i in range(rows):
        for j in range(cols):
            if i*10 + j < n:
                axs[i, j].imshow(arr[i*10 + j], cmap='gray_r')
            axs[i, j].axis('off')
    plt.show()

draw_fruits(fruits[km.labels_==0])
draw_fruits(fruits[km.labels_==1])
draw_fruits(fruits[km.labels_==2])

draw_fruits(km.cluster_centers_.reshape(-1,100,100),ratio=3)

print(km.transform(fruits_2d[100:101]))
print(km.predict(fruits_2d[100:101]))
draw_fruits(fruits[100:101])
print(km.n_iter_)

inertia = []
for k in range(2,7):
    km = KMeans(n_clusters=k,random_state=42)
    km.fit(fruits_2d)
    inertia.append(km.inertia_)
plt.plot(range(2,7),inertia)
plt.xlabel('k')
plt.ylabel('inertia')
plt.show()

# n_components 가 1 이상의 값이 들오오면 개수로 1 보다 작으면 % 0.5 = 50%
pca = PCA(n_components=50)
pca.fit(fruits_2d)

print(pca.components_.shape)
draw_fruits(pca.components_.reshape(-1,100,100))
print(fruits_2d.shape)
fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)
fruits_inverse = pca.inverse_transform(fruits_pca)
print(fruits_inverse.shape)
fruits_reconstruct = fruits_inverse.reshape(-1,100,100)
for start in [0,100,200]:
    draw_fruits(fruits_reconstruct[start:start+100])
    print('\n')

print(np.sum(pca.explained_variance_ratio_))

plt.plot(pca.explained_variance_ratio_)
plt.show()

# 지도학습으로 처리 해봄 ..
lr = LogisticRegression()
# 지도 학습의 경우 라벨 지정이 필요 하므로 ...
target = np.array([0]*100+[1]*100+[2]*100)
scores = cross_validate(lr, fruits_2d, target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

scores = cross_validate(lr,fruits_pca,target)
print(np.mean(scores['test_score']))
print(np.mean(scores['fit_time']))

pca = PCA(n_components=0.5)
pca.fit(fruits_2d)

print(pca.n_components_)

fruits_pca = pca.transform(fruits_2d)
print(fruits_pca.shape)

score = cross_validate(lr,fruits_pca,target)
print(np.mean(score['test_score']))
print(np.mean(score['fit_time']))

km = KMeans(n_clusters=3, random_state=42)
km.fit(fruits_pca)
print(np.unique(km.labels_, return_counts=True))

for label in range(0,3):
    draw_fruits(fruits[km.labels_==label])
    print('\n')

for label in range(0,3):
    data = fruits_pca[km.labels_==label]
    plt.scatter(data[:,0], data[:,1])
plt.legend(['pineapple', 'banana', 'apple'])
plt.show()