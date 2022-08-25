ab = {
    'swaroop': 'swarrop@swaroopch.com',
    'larry': 'larry@wall.org',
    'matsumoto': 'matz@ruby-lang.org',
    'spammer': 'spammer@hotmail.com'
    }

print("swaroop's address is", ab['swaroop'])
del ab['spammer']

print('\nThere are {} contacts in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('contact {}'.format(name, address))

ab['guido'] = 'guido@python.org'

if 'guido' in ab:
    print("\nGuido's addres is", ab['guido'])