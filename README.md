# curve_fit_const_params
set some parameters in a function to constant for scipy.optimize.curve_fit

## about
scipy.optimize.curve_fit does not allow keyword args with default values.
If you want to make some parameters constant, you should write another function...

```python
def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c

# let b=10
def parabora_fixed(x, a, c):
    return a * x ** 2 + 10 * x + c

param, _ = scipy.optimize.curve_fit(parabola, xs, ys)
param_fixed, _ = scipy.optimize.curve_fit(parabola_fixed, xs, ys)
```

This tool relieves re-defining many of similar functions!

```python
def parabola(x, a, b, c):
    return a * x ** 2 + b * x + c

param, _ = scipy.optimize.curve_fit(parabola, xs, ys)
param_fixed, _ = scipy.optimize.curve_fit(fix_consts(parabola, {'b': 10}), xs, ys)
```

## usage
import fix_consts from constfunc.py

## envs
python 3.6+
