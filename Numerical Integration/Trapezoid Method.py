
import numpy as np
import matplotlib.pyplot as plt
from math import *

def Trapezoid():

    func = input("Enter function: ")

    def f(x):
        return eval(func)

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

    for i in range(N):
        xs = [x[i], x[i], x[i+1], x[i+1]]
        ys = [0, f(x[i]), f(x[i+1]), 0]
        plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)

    
    right = y[1:]
    left = y[:-1]
    dx = (b - a)/N
    T = (dx/2) * np.sum(right + left)

    plt.title('Trapezoid Rule\n N = {}, Area = {}'.format(N, T))

    plt.show()


Trapezoid()
