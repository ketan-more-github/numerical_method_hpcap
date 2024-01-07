import numpy as np




def it(f, a, b, n):
    h = (b - a) / (n / 2)
    sum = 0
    for i in range(int(n)):
        t = f(a + (2 * i) * h) + 4 * f(a + (2 * i + 1) * h) + f(a + (2 * i + 2) * h)
        sum = sum + t
    return h/3*sum


def fx(x):
    y = 2 + 2 * x + x**2 + np.sin(2 * np.pi * x) + np.cos((2 * np.pi * x) / 0.5)
    return y

print(it(fx, 0, 1.5, 1.0))
print(it(fx, 0, 1.5, 3.0))
print(it(fx, 0, 1.5, 18.0))


from scipy.integrate import quad
import numpy as np
def poly(x):
    return 2+2*x+x**2+np.sin(2*np.pi*x) + np.cos((2*np.pi*x)/0.5 )
    
poly_int = quad(poly , 0 , 1.5)
print(poly_int[0])
