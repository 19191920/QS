year = 2016
event = 'referendum'
print(f'results of the {year} {event}')

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes {:2.2%}'.format(yes_votes, percentage))

s = 'hello, world.'
print(str(s))
print(repr(s))
print(str(1/7))
x = 10 * 3.25
y = 200 * 200
s = 'The value og x is ' + repr(x) + ', and my is' + repr(y) + '...'
print(s)
hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print(repr((x, y, ('spam', 'eggs'))))
