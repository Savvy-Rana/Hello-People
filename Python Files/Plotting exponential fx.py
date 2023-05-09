import numpy as np 
import matplotlib.pyplot as plt 
n=100
x=np.linspace(0,4,n+1)
y=np.exp(-x)*np.sin(2*np.pi*x)
plt.plot(x,y)
plt.show()