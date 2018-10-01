# Solve the ODE for a conducting ring spinning in a magnetic field.
import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt


# This function evaluates the derivatives for the equation
# d^2 theta/dt^2 = - * sin(theta) -q* d theta/dt + Fsin(k*t)
# We work in the transformed variables y[0] = theta, y[1] = d(theta)/dt
k=0
F=0
q=0

def derivatives(y,t,q,f,k):
    return [y[1], -np.sin(y[0]) - q*y[1] + F*np.sin(k*t)]
# Main code starts here
t=np.linspace(0.0, 100.0, 10000)
y0=[0.01, 0.0]

y=scipy.integrate.odeint(derivatives,y0,t,args=(q,k,F))
for i in range(len(y)):
    print("{:8.4g} {:8.4g} {:8.4g}".format(t[i],y[i,0],y[i,1]))
 
#plotting     
plt.plot(t, 0.5*y[:, 1]**2 + (1-np.cos(y[:, 0])), 'b', label='energy(t)')
plt.plot(t, 0.5*(0.01*np.sin(t))**2  + (1-np.cos(0.01*np.cos(t))), 'g', label='theoretical solution(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.xlim(0,100)
plt.grid()
plt.show()
plt.savefig('pendulum1.pdf')
