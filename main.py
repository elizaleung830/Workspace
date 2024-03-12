from sympy import *
from sympy import lambdify
from scipy.optimize import fsolve
from IPython.display import display, Math
V, I = symbols("V I", cls=Function)
RC, t, C, Vs, L, R1, V0, I0 = symbols("RC t C Vs L R1 V0 I0")
system = [Eq(V(t).diff(t), -1/RC*V(t) + I(t)/C), Eq(I(t).diff(t), -R1/L*I(t) - 1/L*V(t) + Vs/L)]
ics = {V(0): V0, I(0): I0}
dsolve(system, [V(t), I(t)], ics=ics)

print("Second")
t, C1, C2 = symbols("t, C1, C2")
y = Function('y')
x = Function('x')
eq1 = Eq(y(t).diff(t), -3*x(t)**2 * y(t))
eq2 = Eq(x(t).diff(t), x(t)**3 - sin(y(t)))
ics = {y(0): 2, x(0): 2}
print(dsolve([eq1,eq2],[y(t),x(t)], ics = ics) )