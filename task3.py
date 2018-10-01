# Solve the ODE for a conducting ring spinning in a magnetic field.
import numpy as np
import scipy.integrate
import argparse
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("F", dtype = float, help = "Driving force")
parser.add_argument("q", dtype = float, help = "damping")
parser.add_argument("k", dtype = float, help = "Driving frequency")
x = parser.parse_args()

# This function evaluates the derivatives for the equation
# d^2 theta/dt^2 = - * sin(theta) -q* d theta/dt + Fsin(k*t)
# We work in the transformed variables y[0] = theta, y[1] = d(theta)/dt
def derivatives(y,t,q,f,k):
    return [y[1], -np.sin(y[0]) - q*y[1] + F*np.sin(k*t)]
# Main code starts here
t=np.linspace(0.0, 20.0, 200)
y0=[0.0, 10.0]
tau=2.0
y=scipy.integrate.odeint(derivatives,y0,t,args=(q,k,F))
for i in range(len(y)):
    print("{:8.4g} {:8.4g} {:8.4g}".format(t[i],y[i,0],y[i,1]))
 
#plotting     
plt.plot(t, y[:, 0], 'b', label='theta(t)')
plt.plot(t, y[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
plt.savefig('pendulum1.pdf')
