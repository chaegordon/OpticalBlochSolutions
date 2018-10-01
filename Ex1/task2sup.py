import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
import cmath
import numpy as np
import scipy as sc
from scipy import integrate

#define integrands and integrating functions of the fresnel integrals

d=0.1
l=0.01
D=1

def Cfunc(x):

	return np.cos(np.pi*(x**2)/(l*D))

def Sfunc(x):

	return np.sin(np.pi*(x**2)/(l*D))

def Cint(u):

	return sc.integrate.quad(Cfunc, u-d/2, u+d/2)

def Sint(u):

	return sc.integrate.quad(Sfunc,u-d/2,u+d/2)

def Intensity(u):
	
	return (Cint(u)[0]**2 + Sint(u)[0]**2)

def Amp(u):
	return np.sqrt(Intensity (u))

def faze(u):
	z= complex(Cint(u)[0],Sint(u)[0])
	return cmath.phase(z)

#Collecting data by creating an empty matrix and then populating it with a marix of values -5<u<5
data = []
plase= []
for i in np.arange(-500, 501):
  m = i/100
  mat = [m, Amp(m)]
  pat=[m, faze(m)]
  data.append(mat)
  plase.append(pat)

#Plot data
fig1=plt.figure(1)
data = np.transpose(data)
plt.plot(data[0][:],data[1][:])
plt.title('Open Slit')
plt.xlim(-1,1)
plt.ylabel('A')
plt.xlabel('u')
plt.savefig('Open slit100.pdf')

#plot phase
fig2=plt.figure(2)
phase=np.transpose(plase)
plt.plot(phase[0][:],phase[1][:])
plt.title('Open Slit Phase')
plt.xlim(-1,1)
plt.ylabel('phase')
plt.xlabel('u')
plt.savefig('Open slit phase100.pdf')

