import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

F=0
q=0
N=10000
tmax=100
theta0=0.01

z0 = np.array([theta0, 0])
t = np.linspace(0, tmax, N)


def fun(z, t, q, F):
    return np.array([z[1], -np.sin(z[0]) - q*z[1] + F*np.sin(2.0*t/3.0)])



def energy(y):
    KE = 0.5 * 9.81**2 * y[:,1]**2
    PE = 9.81 **2 *(1 - np.cos(y[:,0]))
    return np.column_stack((KE + PE, KE, PE))

def period(y):
	test = True
	result = []
	for i in range(y.shape[0]):
		if y[i,2] > 0:
			test = True
		elif test:
			result.append(y[i,0])
			test = False
			res = np.array(result)
			Tcount = 0
	for i in range(len(res)-1):
		Tcount += res[i+1] - res[i]
	return Tcount/(len(res) - 1)



sol = spi.odeint(fun, z0, t, args = (q, F))
out = np.column_stack((t, sol, energy(sol)))

np.savetxt("data1.csv", out)
#data = np.empty((0,N))
for i in range(N):
    while sol[i,0] > np.pi:
        sol[i,0] -=2 *np.pi
        while sol[i,0] < -np.pi:
            sol[i,0]+= 2*np.pi
    #data=np.append(data, [energy(sol)[0]])
out = np.column_stack((t, sol, energy(sol)))
np.savetxt("data2.csv", out)

print(period(out))

#plotting     
plt.plot(out[:,0], out[:,3])
plt.ylabel('E')
plt.xlabel('t')
plt.xlim(0,100)
plt.grid()
plt.savefig('pendulumEcons.pdf')
plt.show()
