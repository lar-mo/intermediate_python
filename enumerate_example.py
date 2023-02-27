'''
Print each flower's index number and flower name
'''

flowers = ['rose','daisy','tulip','peony']

# naive implementation
count = 0
print('Naive')
for flower in flowers:
    print(count,flower)
    count+=1
print()
'''
output:
0 rose
1 daisy
2 tulip
3 peony
'''

# enumerate()
print('Enumerate')
for count,flower in enumerate(flowers):
    print(count,flower)
print()
'''
output:
0 rose
1 daisy
2 tulip
3 peony
'''

# list() variation
print('List() variation')
print(list(enumerate(flowers)))
print()
'''
output: [(0, 'rose'), (1, 'daisy'), (2, 'tulip'), (3, 'peony')]
'''

# dict() variation
print('Dict() variation')
print(dict(enumerate(flowers)))
print()
'''
output: {0: 'rose', 1: 'daisy', 2: 'tulip', 3: 'peony'}
'''
