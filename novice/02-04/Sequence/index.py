shoplist = ['ayam', 'bebek', 'itik', 'angsa']
name = 'swaroop'

print('item 0 is', shoplist[0])
print('item 1 is', shoplist[1])
print('Item 2 is', shoplist[2])
print('Item 3 is', shoplist[3])
print('Item -1 is', shoplist[-1])
print('Item -2 is', shoplist[-2])
print('Character 0 is', name[0])

print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])

shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[::1]
['apple', 'mango', 'carrot', 'banana']
shoplist[::2]
['apple', 'carrot']
shoplist[::3]
['apple', 'banana']
shoplist[::-1]
['banana', 'carrot', 'mango', 'apple']
