from sympy import *
from sympy import lambdify
from scipy.optimize import fsolve
from IPython.display import display, Math
vo, v1, v2, c, i, v, t, l, r, n = symbols('v_o v_1 v_2 c i v t L R n', real=True)

vt = 25* 10**-3
print("start")
eq1 = Eq(i*(exp(0.7/(n*vt))-1) , 1*10**-3)
eq2 = Eq(i*(exp(0.8/(n*vt))-1) , 10*10**-3)
print(nsolve([eq1,eq2], [i, n], (1,1), verify=False))