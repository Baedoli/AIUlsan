
from cProfile import label
from matplotlib.lines import _LineStyle
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.figure()
plt.plot([1,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2,1,0])
plt.show()

t = np.arange(0,12,0.01)
x = np.sin(t)
y = np.cos(t)
plt.figure(figsize=(10,6))
plt.plot(t,x,lw=3,label='sin')
plt.plot(t,y,c='r',label='cos')
plt.grid()
plt.legend(ncol=2,loc='best')
plt.xlabel('Time',labelpad=5)
plt.ylabel('Amplitude',labelpad=5)
plt.title('Example of sineware', loc='center', pad=10)
plt.xlim(0,np.pi)
plt.ylim(-1.2,1.2)
#plt.axis([0,np.pi,-1.2,1.2])
plt.show()

t = np.arange(0,5,0.5)
plt.figure(figsize=(10,6))
plt.plot(t,t,'r--')     # r : red 이며 -- 표시
plt.plot(t,t**2,'bX')   # b : blue 이며 s : square(네모)
#plt.plot(t,t**3,'g^')   # g : green 이며 ^ : triangle_up (삼각형)
plt.plot(t,t**3,'g8')   # g : green 이며 ^ : triangle_up (삼각형)
plt.show()

t = np.arange(0,5,0.5)
plt.figure(figsize=(10,3))
pl1 = plt.plot(t,t**2,'bs')
plt.ylim(0,60)
plt.figure(figsize=(10,3))
pl2 = plt.plot(t,t**3,'g^')
plt.ylim(0,60)
plt.show()

t = [0,1,2,3,4,5,6]
y = [1,4,5,8,9,5,3]
plt.figure(figsize=(10,6))
#plt.plot(t,y,color='coral',linestyle='-.')
#plt.plot(t,y,color='blue',linestyle='dashed',marker='o',markerfacecolor='blue')
#plt.plot(t,y,color='blue',linestyle='dashed',marker='o',mfc='blue', ms=12)
plt.plot(t,y,color='blue',linestyle='dashed',marker='o',markerfacecolor='blue',markersize=12)
#plt.plot(t,y,color='coral',ls='dashed')
#plt.plot(t,y,color='coral',linestyle='--')
plt.show()

