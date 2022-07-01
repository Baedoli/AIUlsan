
from sklearn.datasets import load_diabetes
import matplotlib.pyplot as plt
diabetes = load_diabetes()

diabetes.data.shape
diabetes.target.shape

print(diabetes.data[0:3])
print(diabetes.target[:3])

plt.scatter(diabetes.data[:,2],diabetes.target)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
