import sympy as sym
import numpy as np
import matplotlib.pyplot as plt
from math import *
from sympy.abc import x
def Simpson():
    global x
    func = input("Enter function: ")
    func = sym.sympify(func)
    f = sym.lambdify(x, func)

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
    r = np.linspace(a, b, 100)
    plt.fill_between(r, f(r), 'b', edgecolor='b', alpha=0.2)

    right = y[1:]
    left = y[:-1]
    middle = [2 * y[x] for x in range(len(y[1:-1])) if x % 2 == 0]
    dx = (b - a)/N
    T = (dx/3) * np.sum(right + left + middle)

    plt.title('Simpson Rule\n N = {}, Area = {}'.format(N, T))

    plt.show()


Simpson()
