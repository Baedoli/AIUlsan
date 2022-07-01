import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier

cancer = load_breast_cancer()

print(cancer.data.shape,cancer.target.shape)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = train_test_split(x,y,stratify=y,test_size=0.2,random_state=42)

class LogisticNeuron:

    def __int__(self):
        self.w = None
        self.b = None
        self.losses = []

    def forpass(self, x):
        z = np.sum(x * self.w) + self.b
        return z

    def backprop(self,x,err):
        w_grad = x * err
        b_grad = 1 * err

        return w_grad, b_grad

    def fit(self,x,y,epochs=100):
        self.w = np.ones(x.shape[1])
        self.b = 0

        for i in range(epochs):
            loss = 0
            indexes = np.random.permutation(np.arange(len(x)))
            #for x_i, y_i in zip(x,y):
            for i in indexes:
                z = self.forpass(x[i])
                a = self.actviation(z)
                err = -(y[i] - a)
                w_grad, b_grad = self.backprop(x[i], err)
                self.w -= w_grad
                self.b -= b_grad
                a = np.clip(a, 1e-10, 1-1e-10)
                loss += (y[i]*np.log(a)+(1-y[i])*np.log(1-a))
        self.losses.append(loss/len(y))

    def actviation(self,z):
        a = 1/(1+np.exp(-z))
        return a

    def predict(self,x):
        z = [self.forpass(x_i) for x_i in x]
        # a = self.actviation(np.array(z))

        return np.array(z)>0.5

    def score(self,x,y):
        return np.mena(self.predict(x)==y)

neuron = LogisticNeuron()
neuron.fit(x_train, y_train)

class SingleLayer:

    def __init__(self):
        self.w = None
        self.b = None

    def forpass(self, x):
        z = np.sum(x * self.w) + self.b
        return z

    def backprop(self,x,err):
        w_grad = x * err
        b_grad = 1 * err

        return w_grad, b_grad

    def fit(self,x,y,epochs=100):
        self.w = np.ones(x.shape[1])
        self.b = 0

        for i in range(epochs):
            loss = 0
            indexes = np.random.permutation(np.arange(len(x)))
            #for x_i, y_i in zip(x,y):
            for i in indexes:
                z = self.forpass(x[i])
                a = self.actviation(z)
                err = -(y[i] - a)
                w_grad, b_grad = self.backprop(x[i], err)
                self.w -= w_grad
                self.b -= b_grad
                a = np.clip(a, 1e-10, 1-1e-10)
                loss += (y[i]*np.log(a)+(1-y[i])*np.log(1-a))
            self.losses.append(loss/len(y))

    def actviation(self,z):
        a = 1/(1+np.exp(-z))
        return a

    def predict(self,x):
        z = [self.forpass(x_i) for x_i in x]
        return np.array(z)>0.5

    def score(self,x,y):
        return np.mean(self.predict(x)==y)

layer = SingleLayer()
layer.fit(x_train,y_train)
layer.score(x_test,y_test)

plt.plot(layer.losses)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()

sgd = SGDClassifier(loss='log', max_iter=100, tol=1e-3, random_state=42)
sgd.fit(x_train,y_train)
sgd.score(x_test,y_test)

print(sgd.predict(x_test[0:10]))

