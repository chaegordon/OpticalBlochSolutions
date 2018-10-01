import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

#defining intial conditions and parameters (these vary between task!)

F=1.0001
q=0.0001
N=100000
tmax=100
theta0=0.0001001

z0 = np.array([theta0, 0])
t = np.linspace(0, tmax, N)

#coupled ODE

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


sol = spi.odeint(fun, z0, t, args = (q, F))
out = np.column_stack((t, sol, energy(sol)))

np.savetxt("data1.csv", out)
#res = np.empty((0,N))
for i in range(N):
    while sol[i,0] > np.pi:
        sol[i,0] -=2 *np.pi
        while sol[i,0] < -np.pi:
            sol[i,0]+= 2*np.pi
    #res=np.append(res, [energy(sol)[0]])
out = np.column_stack((t, sol, energy(sol)))
np.savetxt("data2.csv", out)

print(period(out))

#plotting     
plt.plot(out[:,1], out[:,2])
plt.title('Omega as a function of theta,q=0.0001 F=1.0001 theta0=0.0001001')
plt.ylabel('Omega')
plt.xlabel('theta')
plt.xlim(0,3.14)
plt.grid()
plt.savefig('pendulumChaos_q0.0001_1.0001_theta0.0001001.pdf')
plt.show()
