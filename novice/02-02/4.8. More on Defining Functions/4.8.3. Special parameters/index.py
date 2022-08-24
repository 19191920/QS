def standard_arg(arg):
    print(arg)
def pos_only_arg(arg, /):
    print(arg)
def kwd_only_arg(*, arg):
    print(arg)
def combined_excample(pos_only, /, standrad, *, kwd_only):
    print(pos_only, standrad, kwd_only)

# standard_arg(2)

# standard_arg(arg=2)
#pos_only_arg(1)
#kwd_only_arg(arg=3)

# combined_excample(1, 2, kwd_only=3)
# combined_excample(1, standrad=2, kwd_only=3)

def foo(name, **kwds):
    return 'name' in kwds

def foo(name, /, **kwds):
    return 'name' in kwds
    foo(1, **{'name': 2})
True