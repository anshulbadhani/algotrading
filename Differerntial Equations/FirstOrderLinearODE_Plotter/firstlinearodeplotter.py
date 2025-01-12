"""
# Explaining The Math:
    This program uses the concept of isoclines to plot the direction field.
    Suppose we have a first order ODE y' = f(x, y)
    Now to plot a vector we need slope at that point and we know that slope is just y'
    which itself is equal to f(x, y). In short, we are just plotting functions for 
    different values of x and y.
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# symbols are notation for variables in math
x, y, z, t, w = symbols("x y z t w")

# Getting input and converting it to a numpy expression
print("Input the linear Ordinary differential Equation of form dy/dx = f(x, y)")
expr = str(input("dy/dx = "))
f = lambdify([x, y], expr, "numpy")

# Creating a 2D grid with 20 points on X and Y axis resp
X = np.linspace(-10, 10, 20)
Y = np.linspace(-10, 10, 20)
x, y = np.meshgrid(X, Y)

# defining the components of vectors; Remove u = 1 and normalization part and uncomment np.ones line for normalization of vector to not happen

# u = np.ones(400)
u = 1
v = f(x, y)

# Normalizing the vectors for uniform arrows
mag = np.sqrt(u**2 + v**2)
u /= mag
v /= mag

# Plotting arrows
plt.quiver(x, y, u, v, color="blue", angles="xy")
plt.title(f"Plot for dy/dx={expr}")
plt.grid()
plt.show()
