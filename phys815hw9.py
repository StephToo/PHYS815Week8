import numpy as np
from scipy.optimize import minimize

# Define function that is being minimized
def func(x):
    return x**2 - 4*x + 3

# Define the initial guess
x0 = 0

# Find the minimum of the function
res = minimize(func, x0)

# Print the minimum and the corresponding x value
print("Minimum value: ", res.fun)
print("X value at minimum: ", res.x)
