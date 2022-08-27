# while true:
#     try:
#         x = int(input("please enter a number: "))
#         break
#     except valueError:
#         print("Oops! that was no valid number. try again...")

# except (runtimeerror, typeerror, nameerror):
#     pass

# class B(exception):
#     pass
# class C(B):
#     pass

# class D(C):
#     pass
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# import sys

# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError:
#     print("OS error: {0}".format(err))
# except valueerror:
#     print("could not convert data to an integer.")
# except BaseException as err:
#     print(f"unexpected {err=}, {type(err)=}")
#     raise

# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))
#     print(inst.args)
#     print(inst) 

#     x, y = inst.args
#     print('x =', x)
#     print('y =, y') 

def this_fails():
    x = 1/0
try:
    this_fails()
except ZeroDevisionError as err:
    print('Handling run-time error:', err)