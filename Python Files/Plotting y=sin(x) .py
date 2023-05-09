from numpy import *
import matplotlib.pyplot as plt 
xmin=0
xmax=30
x=linspace(0,30,101)
y=sin(x)
plt.plot(x,y)
plt.show()