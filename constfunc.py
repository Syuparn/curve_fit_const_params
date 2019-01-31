def fix_consts(func, const_dict):
    """
    func: function
    const_dict: args of func you want to treat as const ({name: const value})

    This returns lambda expr in which the names contained in the key of
    const_dict in argments of func are replaced by the constant value
    corresponding to that key.

    i.e.)
    def parabola(x, a, b, c):
        return a * x ** 2 + b * x + c
    fix_consts(parabola, {'b': 10})
    => lambda x, a, c: parabola(x, a, 10, c)
    """
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    # arg names for NEW function
    var_names = [n for n in arg_names if n not in const_dict.keys()]
    # args new function passes to func
    # if name in const_dict, use const, otherwise use name itself
    args = [str(const_dict.get(name, name)) for name in arg_names]
    # generate new lambda expr, which gets args without ones to be const
    # NOTE: use list comprehension to bind object referred as func to name f
    # (otherwise, name 'func' is evaluated when this lambda expr is called) 
    fixed_const_func = eval(
        f'[lambda {",".join(var_names)}: f({",".join(args)})'
        f' for f in [func]][0]', {},
        {'var_names': var_names, 'args': args, 'func': func})
    return fixed_const_func
