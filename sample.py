import scipy.optimize
import numpy as np
from constfunc import fix_consts


def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c


xs = np.arange(100)
noises = (np.random.rand(100) * 10 - 5)
# let a=0.1, b=10, c=10 (actually unknown)
ys = 0.1 * xs ** 2 + 10 * xs + 10 + noises

# estimate parameters
param, _ = scipy.optimize.curve_fit(parabola, xs, ys)
print('a b c')
print(param)
# already known that b=10!
param2, _ = scipy.optimize.curve_fit(fix_consts(parabola, {'b': 10}), xs, ys)
print('a c')
print(param2)
