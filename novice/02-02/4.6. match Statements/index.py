# def http_status(status):
#     match status:
#         case 400:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's Wrong with the internet"

# print(http_status(400))
# print(http_status(404))
# print(http_status(418))

class point:
    x: int
    y: int

def where_is(point):
    match point:
        case point(x=0, y=0):
            print("origin")
        case point(x=0, y=y):
            print(f"Y={y}")
        case point(x=x, y=0):
            print(f"x={x}")
        case point():
            print("somewehere else")
        case _:
            print("not a point")

