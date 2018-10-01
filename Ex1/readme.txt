#Excercise 1 read me

#Task 1 - source code named task1.py
#A program was developed to numerically solve the multivariate sine function in python.
#A function was found in the python documentation which generated an array of random variable,
#this made vectorising the code a lot easier. Some difficulty was found in generating the data for the integrating
#function, however with the help of a demonstrator a for loop using np.arrange was used to generate data points populating
#an empty array. If I were to rewrite the code again I might use a numpy array as althought there were no problems in 
#this instance numpy functions require numpy arrays so np.zeroes maybe a more versatile choice than '[]'.

#The value obtained for the integral was 537.16 with an error of 0.04

#Supplementary Task 1 - source code included in task1.py

#The theory suggested a N^-1/2 error and so a gradient of -1/2 was expected in the log graphs. This was observed.
#There is a potential anomaly in the actual error graph near the ln(N) = 2 point but the agreement seemed pretty good.
#For this reason I don't think the code is incorrect.

#Task 2 - source code named task2.py

#It was noted that there do exist explicit python functions for the cornu integrals, however, bespoke functions were 
#created. Because the integrals have only 2 variable a monty carlo approach is unnecesary and instead scipy integration
#functions were used. A similar for loop to the one in task1 was used to generate data and the plot of the cornu spiral
#looked as expected.

#Supplementary Task 2 - source code named task2sup.py

The code of task 2 was developed to calculate a diffraction pattern. The variables in the cornu integrals
#were scaled by pi/lambda*D. The intensity was calculated as C^2 + S^2 with rescaled variables and the amplitude
#the square root of this. The limits of the integral had to be shifted so as to scan the whole space whilst maintaining
#their relative seperation of 'd' this was done via a for loop in 'u' with the limits of the integral being [u-d/2, u+d/2].
#The plot of amplitude for the open slit looked as expected like a mixture between a gaussian and a sinc function.

 

