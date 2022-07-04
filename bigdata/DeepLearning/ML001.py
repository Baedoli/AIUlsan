
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

diabetes = load_diabetes()

x = diabetes.data[:,2]
y = diabetes.target

print(diabetes.data.shape, diabetes.target.shape)
plt.scatter(diabetes.data[:,2],diabetes.target)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

w = 1.0
b = 1.0

y_hat = x[0]*w + b
print(y_hat)
print(y[0])

w_inc = w + 0.1
y_hat_inc = x[0]*w_inc + b
print(y_hat_inc)

w_rate = (y_hat_inc - y_hat)/(w_inc - w)
print(w_rate)
print(x[0])

for x_i, y_i in zip(x,y):
    y_hat = x_i*w + b
    err = y_i - y_hat
    w_rate = x_i
    w = w + w_rate*err
    b = b + 1 * err
print(w,b)

plt.scatter(x,y)
pt1 = (-0.1, -0.1*w+b)
pt2 = (0.15, 0.15*w+b)
plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

for i in range(1,100):
    for x_i, y_i in zip(x,y):
        y_hat = x_i * w + b
        err = y_i - y_hat
        w_rate = x_i
        w = w + w_rate * err
        b = b + 1 * err
print(w,b)

plt.scatter(x,y)
pt1 = (-0.1, -0.1*w+b)
pt2 = (-0.15,-0.15*w+b)
plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()

x_new = 0.18
y_pred = x_new * w + b
print(y_pred)

plt.scatter(x,y)
plt.scatter(x_new, y_pred)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

class Neuron:
    def __init__(self):
        self.w = 1.0
        self.b = 1.0

    def forpass(self, x):
        y_hat = x * self.w + self.b
        return y_hat

    def backprop(self,x,err):
        w_grade = x * err
        b_grade = 1 * err
        return w_grade, b_grade

    def fit(self, x, y, epochs=100):
        for i in range(epochs) :
            for x_i, y_i in zip(x,y):
                y_hat = self.forpass(x_i)
                err = -(y_i-y_hat)
                w_grade, b_grade = self.backprop(x_i, err)
                self.w -= w_grade
                self.b -= b_grade

neuron = Neuron()
neuron.fit(x,y)

plt.scatter(x,y)
pt1 = (-0.1,-0.1*neuron.w+neuron.b)
pt2 = (0.15, 0.15*neuron.w+neuron.b)
plt.plot([pt1[0],pt2[0]],[pt1[1],pt2[1]])
plt.xlabel('x')
plt.ylabel('y')
plt.show()


