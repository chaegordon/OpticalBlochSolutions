# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 14:09:17 2018

@author: chaeg
"""

#Program to calculate the Optical Bloch equation's solutions in different 
#damping regimes.

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

tau = 0
delta = 10
omega = 1


def Optical_Bloch(y,t,tau,delta,omega):
    u, v, w = y
    diff = [-1*(0.5)*tau*u + delta*v, -1*delta*u + -1*(0.5)*tau*v + omega*w, -1*omega*v -1*tau*w + tau]
    return diff



y0 = [0,0,1]
t = np.linspace(0, 10, 101)

sol = odeint(Optical_Bloch, y0, t, args = (tau,delta,omega))

plt.plot(t, sol[:, 0], 'b', label='u', color = 'green')
plt.plot(t, sol[:, 1], 'b', label='v')
plt.plot(t, sol[:, 2], 'b', label='w', color = 'red')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()