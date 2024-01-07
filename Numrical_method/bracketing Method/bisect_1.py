from math import sin, cos

a = -0.6
b = -0.5

print(cos(0.995004))


def f(x):
    z = sin(5 * x) + cos(2 * x)

    return z


while True:
    if f(a) * f(b) < 0:
        xi = (a + b) / 2

        if round(f(xi), 3) == 0:
            print("root find = ", round(xi, 3))
            break

        elif f(a) * f(xi) < 0:
            b = xi

        elif f(b) * f(xi) < 0:
            a = xi
    else:
        print("root are not found")
        break
