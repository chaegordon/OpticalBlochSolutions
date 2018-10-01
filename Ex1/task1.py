#A program was developed to numerically solve the multivariate sine function in python.
#A function was found in the python documentation which generated an array of random variable,
#this made vectorising the code a lot easier. Some difficulty was found in generating the data for the integrating
#function, however with the help of a demonstrator a for loop using np.arrange was used to generate data points populating
#an empty array. If I were to rewrite the code again I might use a numpy array as althought there were no problems in 
#this instance numpy functions require numpy arrays so np.zeroes maybe a more versatile choice than '[]'.

#The value obtained for the integral was 537.16 with an error of 0.04

import matplotlib.pyplot as plt
import numpy as np


def integrandy(coordList):
  #Want an array of N by 8 with which we sum each set of coordinates
  #then sine the totals
  sumCo = coordList.sum(axis = 1)
  sinval = np.sin(sumCo)
  return sinval

def Monty(Samplenumber):
  
  #Defining the parameters of the integral
  s = np.pi / 8
  D = 8
  
  #Generate random values from 0 to s, in array size D
  randCo=s*np.random.random((Samplenumber, D))
    
  #Obtain mean value and volume
  Values = integrandy(randCo)
  meanval = np.average(Values)
  errorval = np.std(Values)
  V = s ** D
  
  #integral estimate and standard deviation
  Estimate = meanval * V * (10 ** 6)
  sigma = errorval * V * (10 ** 6)
  return [Estimate, sigma]

results = []
for i in np.arange(0,24,1):
  #pick N values spaced evenly on log log scale
  N = int(np.around(10 ** (i/4)))
  data = []
  #averaging 25 runs for each Nt value,  get error in 
  #the mean over 25 runs making an array of 25 monty calculations
  for n in np.arange(25):
    data.append(Monty(N)[0])
  mean = np.average(data)
  error = np.std(data)
  theorError = (N**-0.5)*Monty(N)[1]
  res = [N, mean, error, theorError]
  results.append(res)
results=np.asarray(results)
lnres=np.log(results)

#printing results

print( 'Integral is')
print ( Monty (10**6)[0])

print( 'with error')
print( (10**-3)*Monty(10**6)[1])

#plot actual error on a log log graph, predicted gradient = 1/2
plt.plot(lnres[:,0], lnres[:,2], label='actual')
plt.title('Logarithmic Graph of Error vs N')
plt.ylabel('ln(error)')
plt.xlabel('ln(N)')
plt.legend()
plt.savefig('error_loglog.pdf')

#plot theoretical error as well
plt.plot(lnres[:,0], lnres[:,3], label='actual')
plt.plot(lnres[:,0], lnres[:,2],label='theory')
plt.title('Logarithmic Graph of Error vs N')
plt.ylabel('ln(error)')
plt.xlabel('ln(N)')
plt.legend()
plt.savefig('theoretical_vs_actual_error.pdf')
