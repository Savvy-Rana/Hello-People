import matplotlib.pyplot as plt 
import numpy as np 
def f(x):
    return np.exp(-x)*np.sin(2*np.pi*x)
n=10 
x=np.linspace(0,4,n+1)
y=f(x)
plt.plot (x,y, label='exp(-x)*sin(2*pi*x')
plt.xlabel('x')                     #label on x axis
plt.ylabel('y')                     #label on y axis 
plt.legend()                        #marks the curve 
plt.axis([0,4,-0.5,0.8])            #[xmin, xmax, ymin, ymax]
plt.title('Matplotlib-Demo/practice')
plt.savefig('fig.pdf')      #makes pdf image for report
plt.savefig('fig.png')      #makes PNG image for report 
plt.show()