# f.read()
# f.rad()

# f.readline()
# f.readline()
# f.readline()

# for line in f:
#     print(line, end='')

# print(f.write('this is a test\n'))

# value = ('the answer', 42)
# s = str(value)
# f.write(s)

f = open('workfile', 'rb+')
print(f.write(b'0123456789abcdef'))
print(f.seek(5))

print(f.seek(-3,2))
print(f.read(1))
print(f.read(1))