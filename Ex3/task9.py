import numpy as np
import matplotlib.pyplot as plt

amplitude    = 1     
slitWidth    = 2e-3   
wavelength   = 500e-9 
screenDistance = 10
N=2**16
s=100e-6

#creating the slit
x     = np.linspace(-0.1, 0.1, num = N)
field = np.zeros(x.size, dtype='complex128') # Ensure the field is complex
field[np.logical_and(x > -slitWidth / 2, x <= slitWidth / 2)] = amplitude + 0j
slit = field
#Below code which is used to view the slit is inlcuded
#plt.plot(x, np.angle(slit))
#plt.xlim(-1e-3, 1e-3)
#FFT
dx = x[1] - x[0] # Spatial sampling period, microns

result = np.fft.fft(slit)
result = np.fft.fftshift(result)
freq=np.fft.fftfreq(N,dx)
freq=np.fft.fftshift(freq)

y=wavelength*screenDistance*freq


plt.plot(y, abs(result)**2/max(abs(result)**2), label= 'diffraction pattern')
plt.xlim(-0.01, 0.01)
plt.title('Tophat Slit')
plt.ylabel('Intensity')
plt.xlabel('theta')
plt.legend()
plt.savefig('TophatSlit.pdf')
plt.show()

