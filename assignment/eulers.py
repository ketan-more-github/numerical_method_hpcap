import numpy as np;
x0=0
y0=1
n=6
h=0.02
y=0

for x in np.arange(0 , 0.12 , 0.02):
        f = x**3+y0
        y1=y0+h*(f)
        print(y1)
        y0=y1
        
        
    
     
print(y)
