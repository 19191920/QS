name = 'swaroop'
if name.startswith('swa'):
    print('yes, the string starts with "swa"')

if 'a' in name:
    print('yes, it contains the string "war"')

if name.find('war') != -1:
    print('yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'india', 'china']
print(delimiter.join(mylist))
