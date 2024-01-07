# y=4.5
# y0=2.3
# y1=2.95
# y2=3.5
# y3=5.1

# x0=1.27
# x1=2.25
# x2=2.5
# x3=3.6

x=0
n=4
y=4.5
datax = [1.27 , 2.25 , 2.5 , 3.6]
datay = [2.3 , 2.95 , 3.5 , 5.1]
cnt=0

for i in range(0,n):
    xi = datax[i]
    for j in range(0,n):
        if(i != j):
            cnt=cnt+1
            xi = (xi  * ( y - datay[j])) / ( datay[i] - datay[j] )
    x+=xi
    


print("value of x = " , x)
print("num of itration done = " , cnt)