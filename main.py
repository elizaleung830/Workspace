from sympy import *
from sympy import lambdify

print("Second")
t, C1, C2, x = symbols("t, C1, C2 x")

eq1 = diff(exp(-5*x)*(cos(4*x)-C1*sin(4*x)), x)
eq1 = Eq(eq1, 1)
print(solve(eq1.subs({x:0}), C1))