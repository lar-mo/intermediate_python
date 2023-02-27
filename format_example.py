'''
insert variable in printed sentence
'''

name = 'John'

# naive implementation
print('Naive')
print('Hello', name)
print()
'''
output: Hello John
'''

# f-string
print('f-string')
print(f'Hello {name}')
print()
'''
output: Hello John
'''

# format()
print('Format')
print('Hello {}'.format(name))
print()
'''
output: Hello John
'''
