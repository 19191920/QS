# try:
#     raise keyboardInterrupt
# finally:
#      print('Goodbye, world!')

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# bool_retrun()

def divide(x, y):
    try:
      result = x / y
    except ZerodivisionError:
        print("division by zero!")
    else:
       print("result is is", result)
    finally:
        print("executing finallly clause")

print(divide(2, 1))
print(divide(2, 0)) 
print(divide("2", "1"))