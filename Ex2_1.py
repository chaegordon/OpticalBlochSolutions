import numpy as np
import scipy.integrate as spi
import argparse

#argparser allows you to adjust the values of q,F,tmax,N,theta0 with every run. These values are entered
#by subsituting for their respective symbols in the following cmd command py ex3.py q F tmax N theta0. Ensure N is much larer #than tmax when running.

parser = argparse.ArgumentParser()
parser.add_argument("q", type = float, help = "Damping")
parser.add_argument("F", type = float, help = "Force")
parser.add_argument("tmax", type = float, help = "Max time")
parser.add_argument("N", type = int, help = "Number of steps")
parser.add_argument("theta0", type = float, help = "initial angular displacement")
x = parser.parse_args()

#Create an array of the two coupled ODE's in our new variables z[0] (theta) and z[1] (omega)

def function(z, t, q, F):
	return np.array([z[1], -np.sin(z[0]) - q*z[1] + F*np.sin(2.0*t/3.0)])

#Array containing various Energy values

def energy(y):
	KE = 0.5 * 9.81**2 * y[:,1]**2
	PE = 9.81 **2 *(1 - np.cos(y[:,0]))
	return np.column_stack((KE + PE, KE, PE))

#calculate period by ammending an array with the time at which the pendulum crosses the 0 on the way down only.

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

#arrays of initial conditions populated with argparsers

z0 = np.array([x.theta0, 0])
t = np.linspace(0, x.tmax, x.N)

#integrating the two ODES using the ode int function from scipy

solution = spi.odeint(function, z0, t, args = (x.q, x.F))

out = np.column_stack((t, solution, energy(solution)))

np.savetxt("data1.csv", out)

#keeping theta0 within limit -pi and pi so as to plot period versus theta0 in this range

for i in range(x.N):
	while solution[i,0] > np.pi:
		solution[i,0] -=2 *np.pi
	while solution[i,0] < -np.pi:
		solution[i,0]+= 2*np.pi

out = np.column_stack((t, solution, energy(solution)))
np.savetxt("data2.csv", out)

print(period(out))


