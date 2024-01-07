
import numpy as np
from scipy.integrate import quad
import sympy as smp
def fx(x):
    y = 2+2*x+x**2+np.sin(2*np.pi*x) + np.cos((2*np.pi*x)/0.5 )
    return y


def it(f,a,b,n):
    h = (b-a)/n
    sum = 0 
    
    for i in range(int(n)):
        t = (f(a + i*h )  + f(a + (i + 1) *h )) 
        sum = sum+t
    return sum*h/2





print(it(fx,0,1.5, 1.0))
print(it(fx,0,1.5, 9.0))







from scipy.integrate import quad
import numpy as np
def poly(x):
    return 2+2*x+x**2+np.sin(2*np.pi*x) + np.cos((2*np.pi*x)/0.5 )
    
poly_int = quad(poly , 0 , 1.5)
print(poly_int[0])
