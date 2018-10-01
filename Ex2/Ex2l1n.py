import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

#defining intial conditions

F=0
q=0
N=10000
tmax=50
num=50
theta0=np.linspace(0,2,num)
theta1=np.linspace(0,2,num-1)

#function similar to one in lecture notes, coupled ODEs in an array

def fun(z, t, q, F):
    return np.array([z[1], -np.sin(z[0]) - q*z[1] + F*np.sin(2.0*t/3.0)])

#creating column stakck of all KE PE and total energy

def energy(y):
    K = 0.5 * 9.81**2 * y[:,1]**2
    P = 9.81 **2 *(1 - np.cos(y[:,0]))
    return np.column_stack((K + P, K, P))

#Function to find period by updating an empty matrix and averaging nearest
#neighbours in the matrix

def period(y):
	test = True
	data = []
	for i in range(y.shape[0]):
		if y[i,2] > 0:
			test = True
		elif test:
			data.append(y[i,0])
			test = False
			dat = np.array(data)
			Tco = 0
	for i in range(len(dat)-1):
		Tco += dat[i+1] - dat[i]
	return Tco/(len(dat) - 1)

#This or loop creates a matrix of T versus initial angular displacement

res = np.empty((0,num))
for m in range(num-1):
    z0 = np.array([theta0[m+1], 0])
    t = np.linspace(0, tmax, N)
    sol = spi.odeint(fun, z0, t, args = (q, F))
    out = np.column_stack((t, sol, energy(sol)))
    np.savetxt("data1.csv", out)
#This for loop deals with wrap around

    for i in range(N):
        while sol[i,0] > np.pi:
            sol[i,0] -=2 *np.pi
        while sol[i,0] < -np.pi:
            sol[i,0]+= 2*np.pi

    out = np.column_stack((t, sol, energy(sol)))
    np.savetxt("data2.csv", out)
#printing the period
    print(period(out))
    res=np.append(res, [period(out)])

#plotting     
plt.plot(theta1, res)
plt.title('Period as a Function of Intial Angular Displacement')
plt.ylabel('T')
plt.xlabel('theta0')
plt.xlim(0,2)
plt.grid()
plt.savefig('pendulumPeriodVAmpl.pdf')
plt.show()
