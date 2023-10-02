# Author: Dayana Gonzalez Cruz
# Runge-Kutta and ODEINT Ordinary Differential Equation Solver
# CST-305: Principles of Modeling
# WF1100 Dr. Citro
# 10-1-2023

# This program solves the ordinary differential equation (ODE) f(x,y) = -y +lnx with intial values x0 = 2, y0 = 1, and a step-size h = 0.3 using the Runge-Kutta 4th Order 
# Method (RK4) and SciPy library's ODEINT function. It uses the pyplot utilities of the matplotlib libary to plot, model, and compare the solutions. 
# The program first intializes the initial values for x and y, the step size h. The ODE is defined within the function RK4 solves which takes parameters of intial values y # and x, step size h, and the count of y values to solve for, m. The ODESolve function takes parameters of initial values x and y and count of y values to solve for, m. The # ODE is defined in a function externally called ODE with value parameters y and x. 
# Within RKSolve ->
# The algoritm solves for k 1 -4 according to the formulas:
# k1 = f(x,y) = -y + lnx
# k2 = f(x + (h/2), y + (h/2)*k1)
# k3 = f(x + (h/2), y + (h/2)*k2)
# k4 = f(x + h, y + h*k3)
# Then, solves for y at m according to the formula:
# ynext = y + (h/6)*(k1+2k2+2k3+k4)
# Algorithm prints k and y values as they are calculated, adding y values to list RKy to plot at a later time. 
# Within ODESolve -> 
# Calls odeint function with parameters of ODE function, initial y value, and a list of x values from the first, incremented by step size h for count m solutions.
# Prints y solutions. 
# Displaying Graphs
# -> Asks user which solution they want to see
# -> Plots and labels respective graph using x, RKy, and ODESolution lists- including computation times and computational steps. 

  
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import time

# Initialize variables and intial values
x0 = 2
y0 = 1
h = 0.3
# Set m number of y points to solve for
m = 1000
# Create list of values x incrementing according to step size h
# np.arrange(initial x value, limit x value (not included), step size, data type)
x = np.arange(x0,x0+(h*(m+1)),h,dtype=float)
# Delete final x from list. 
# It was created to make sure the final x point needed for calculations was included within the limit of numpy arrange
x = x[:-1]
# Create list to hold RK4 solutions
RKy = [y0]
# The computational steps or k and y formulas needed to solve for 1000 y's using the RK4Solve function
Computational_Steps = 5 * m

# Solve using RK4
def RKSolve(xm,ym,h,m):
	print("Runge-Kutta Method")
	# Solve m count of solutions
	for n in range(m):
		# Solve for k 1-4 according to RK4 algorithm	
		# Print out k's in progression with labels
		# k1 = f(x,y) = -y + lnx
		k1 = -(ym) + np.log(xm)
		print("k1 : ", end = "")
		print(k1)
		# k2 = f(x + (h/2), y + (h/2)*k1)
		k2 = -(ym + (h/2)* k1) + np.log((xm + (h/2)))
		print("k2 : ", end = "")
		print(k2)
		# k3 = f(x + (h/2), y + (h/2)*k2)
		k3 = -(ym + (h/2)* k2) + np.log(xm + (h/2))
		print("k3 : ", end = "")
		print(k3)
		# k4 = f(x + h, y + h*k3)
		k4 = -(ym + h*k3) + np.log(xm + h)
		print("k4 : ", end = "")
		print(k4) 
		# Solve for next y according to RK4 formula
		# ynext = y + (h/6)*(k1+2k2+2k3+k4)	
		yn = ym + (h/6)*(k1 + 2*k2 + 2*k3 + k4)
		print("-> y", end ="")
		print(n + 1, end = " : ")
		print (yn)
		# Add y solution to list of solutions
		RKy.append(yn)
		# Increment x according to step size h
		xm += h
		# Set last y
		ym = yn
		# Increment current solution m 
		m += 1
# Define the ODE
def ODE(y,x):
	dydx = -y + np.log(x)
	return dydx

# Solve the ODE using SciPy ODEINT function	
def ODESolve(y0,x,m):
	print("SciPy ODEint Method")
	# odeint(function definition, intial y value, intial x value)
	ODESolution = odeint(ODE, y0,x)
	# Print out solutions with labeling
	for n in range(m+1):
		print("y" , end="")
		print(n, end = " : ")
		print(*ODESolution[n])
	return ODESolution


print("This program solves the ordinary differential equation (ODE) f(x,y) = -y +lnx with intial values x0 = 2, y0 = 1, and a step-size h = 0.3 using the Runge-Kutta 4th Order Method (RK4) and SciPy library's ODEINT function.")
print("")
# Get input from user to 
View = int(input("View Solutions: RK4[1], ODEINT[2], both [3], or exit[0 or other] -> "))

# Calculate run-time and call function to solve by RK4
RK_Start = time.time()
RKSolve(x0,y0,h,m)
RK_End = time.time()
RK_Time = RK_End - RK_Start

# Calculate run-time and call function to solve by ODEINT
ODE_Start = time.time()
ODESolution = ODESolve(y0,x,m)
ODE_End = time.time()
plt.xlabel('x')
ODE_Time = ODE_End - ODE_Start
plt.ylabel('y')

# Plot and display x and y solution values alongside computation times and number of k's and y's calculated per RK4 method.
if(View == 1):
	plt.plot(x,RKy, ':r', label = 'RK4')
	plt.title('1000 Points RK4 Solution')
	plt.legend(['RK4'])
	plt.figtext(0.5, 0.59, "Computation Time: ")
	plt.figtext(0.5, 0.55, str(RK_Time))
	plt.figtext(.5, .45, "Computational Steps: ")
	plt.figtext(.5, .4, Computational_Steps)
	plt.show()
elif(View ==2):
	plt.figtext(0.5, 0.59, "Computation Time: ")
	plt.figtext(0.5, 0.55, str(ODE_Time))
	plt.plot(x,ODESolution, '-b', lw = .4, label = 'odeint')
	plt.title('1000 Points odeint Solution')
	plt.legend(['ODEINT'])
	plt.show()
elif (View == 3):
	plt.figtext(0.5, 0.59, "Computation Time: ")
	plt.figtext(0.4, 0.5, "RK4")
	plt.figtext(.5, .5, str(RK_Time))
	plt.figtext(0.4, 0.55, "ODEINT")
	plt.figtext(.5, .55, str(ODE_Time))
	plt.plot(x,RKy, ':r', label = 'RK4')
	plt.figtext(1, 1, RK_Time)
	plt.figtext(.5, .45, "Computational Steps: ")
	plt.figtext(0.4, 0.4, "RK4")
	plt.figtext(.5, .40, Computational_Steps)
	plt.plot(x,ODESolution, '-b', lw = .4, label = 'odeint')
	plt.title('1000 Points RK4 and odeint Solution')
	plt.legend(['RK4', 'ODEINT'])
	plt.show()
else:
	print("Exited")
