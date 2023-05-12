import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from math import *
from sympy.abc import x

def Midpoint():
    global x
    f = sym.sympify(input("Enter function: "))
    f = sym.lambdify(x, f)

    
    a = int(input("First interval: "))
    b = int(input("Second interval: "))
    N = int(input("Input N: "))

    n = 10

    x = np.linspace(a, b, N+1)
    y = [f(i) for i in x]

    X = np.linspace(a, b, n*N+1)
    Y = [f(i) for i in X]

    plt.figure()

    plt.plot(X, Y)
    area = 0
    for i in range(N):
        midpoint = (x[i]+x[i+1])/2
        xs = [x[i], x[i],        x[i+1],      x[i+1]]
        ys = [0,    f(midpoint), f(midpoint), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)
        area += f(midpoint)

    dx = (b - a)/N
    area *= dx 

    plt.title('Midpoint Rule\n N = {}, Area = {}'.format(N, area))

    plt.show()


Midpoint()
