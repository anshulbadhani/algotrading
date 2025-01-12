# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import symbols, Eq, Function, dsolve, solve, lambdify

# def direction_field_and_solution():
#     # Step 1: Taking inout
#     print("Enter first order differential equation of form dy/dx = f(x, y)")
#     eq_input = input("dy/dx = ")

#     # Step 2: Parsing the eqn using sympy
#     x, y = symbols('x y')
#     dydx_expr = eval(eq_input)

#     # Step 3: Generate direction field
#     x_vals = np.linspace(-5, 5, 20)
#     y_vals = np.linspace(-5, 5, 20)
#     X, Y = np.meshgrid(x_vals, y_vals)

#     # Eval slopes
#     dydx_func = lambdify(symbols, dydx_expr, "numpy")
#     dx = 1
#     dy = dydx_func(X, Y)

#     # Normalizing Vectors
#     magnitude = np.sqrt(dx**2 + V**2)
#     dx /= magnitude
#     dy /= magnitude

#     # Solving Differential Equations
#     y_func = Function('y')
#     eq = Eq(y_func(x).diff(x), dydx_expr)
#     solution = dsolve(eq, y_func(x))
#     print(f"Solution: {solution}")

# direction_field_and_solution()

# import numpy as np
# import matplotlib.pyplot as plt
# from sympy import symbols, Eq, Function, dsolve, lambdify
# from sympy.parsing.sympy_parser import parse_expr

# def direction_field_and_solution():
#     # Step 1: Taking input
#     print("Enter first order differential equation of form dy/dx = f(x, y)")
#     eq_input = input("dy/dx = ")

#     # Step 2: Parsing the equation using sympy
#     x, y = symbols('x y')
#     dydx_expr = parse_expr(eq_input, local_dict={'x': x, 'y': y})

#     # Step 3: Generate direction field
#     x_vals = np.linspace(-5, 5, 20)
#     y_vals = np.linspace(-5, 5, 20)
#     X, Y = np.meshgrid(x_vals, y_vals)

#     # Eval slopes
#     dydx_func = lambdify((x, y), dydx_expr, "numpy")
#     U = np.ones_like(X)  # Step size in x-direction
#     V = dydx_func(X, Y)  # Slopes in y-direction

#     # Normalizing vectors
#     magnitude = np.sqrt(U**2 + V**2)
#     U /= magnitude
#     V /= magnitude

#     # Plotting direction field
#     plt.quiver(X, Y, U, V, color="blue")
#     plt.xlabel("x")
#     plt.ylabel("y")
#     plt.title("Direction Field")
#     plt.grid()

#     # Solving Differential Equation
#     y_func = Function('y')
#     eq = Eq(y_func(x).diff(x), dydx_expr)
#     solution = dsolve(eq, y_func(x))
#     print(f"Solution: {solution}")

#     # Plotting the solution (Optional)
#     sol_func = lambdify(x, solution.rhs, "numpy")
#     x_sol = np.linspace(-5, 5, 400)
#     y_sol = sol_func(x_sol)
#     plt.plot(x_sol, y_sol, color="red", label="Solution Curve")
#     plt.legend()
#     plt.show()

# # Run the program
# direction_field_and_solution()

# 
from sympy import *
import numpy as np
import matplotlib.pyplot as plt

# init_session()

x, y, z, t, w = symbols("x y z t w")
# f, g, h, u, v = symbols("f, g, h, u, v", cls=Function)
# a, b, c, d, e, i, j, l, l, m, n, o, p, q, r, s = symbols("a, b, c, d, e, i, j, l, l, m, n, o, p, q, r, s", isReal=True)

print("Input the linear Ordinary differential Equation of form dy/dx = f(x, y)")
expr = str(input("dy/dx = "))
exprf = lambdify([x, y], expr, "numpy")

X = np.linspace(-10, 10, 20)
Y = np.linspace(-10, 10, 20)
x, y = np.meshgrid(X, Y)

# u = np.ones(400)
u = 1
v = exprf(x, y)

mag = np.sqrt(u**2 + v**2)
u /= mag
v /= mag

plt.quiver(x, y, u, v, color="blue", angles="xy")
plt.title(f"Plot for dy/dx={expr}")
plt.grid()
plt.show()

# help(evalf)