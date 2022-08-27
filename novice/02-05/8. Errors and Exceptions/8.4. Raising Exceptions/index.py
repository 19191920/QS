#     raise NameError('HiThere') 
# traceback (most recent call last):
#     file "<stdin>", line 1, in <module>

try:
    raise NameError('HiThere')
except NameError:
    print('An exceptioon flew by!')
    raise