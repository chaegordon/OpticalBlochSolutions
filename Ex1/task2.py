import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
from scipy import integrate

#define integrands and integrating functions of the fresnel integrals

def Cfunc(x):

	return np.cos(0.5*np.pi*(x**2))

def Sfunc(x):

	return np.sin(0.5*np.pi*(x**2))

def Cint(u):

	return sc.integrate.quad(Cfunc, 0, u)

def Sint(u):

	return sc.integrate.quad(Sfunc,0,u)

#Collecting data by creating an empty matrix and
#then populating it with a marix of values -5<u<5
    
data = []
for i in np.arange(-500, 501):
  j = i/100
  mat = [j, Cint(j)[0], Sint(j)[0]]
  data.append(mat)

#Plot data
data = np.transpose(data)
plt.plot(data[1][:],data[2][:])
plt.title('Cornu Spiral')
plt.ylabel('S(u)')
plt.xlabel('C(u)')
plt.savefig('CornuSpiral.pdf')
