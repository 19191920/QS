print('we are the {} who say "{}!"'.format('knights', 'ni'))
print('{0} and {1}'.format('spam', 'eggs'))
print('{1} and {0}'.format('spam', 'eggs'))

print('this {food} is {adjective}.'.format(
    food='spam', adjective='absolutely horrible'))
print('the story of {0}, {1}, and {other}.'.format('bill', 'manfred',
                                                    other='georg'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
