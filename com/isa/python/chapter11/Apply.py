## apply() built-in function:  Calls the function ONCE and passes optional arguments.
# Different from others:
# - Calls once
# - Accepts not sequence but also dictionary

def funcApply(*nkwargs, **kwargs):
    return (nkwargs, kwargs)


print apply(funcApply, (1, 2, 3, 4))

# Same with lambda functions
print apply(lambda *nkwargs, **kwargs: (nkwargs, kwargs), (1, 2, 3, 4))

# Direct call without apply. With the new syntax we can pass informal arguments as tuple or dict
print funcApply(*(1, 2, 3, 4))
