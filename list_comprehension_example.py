'''
Print list of numbers that were doubled
'''

numbers = [1,3,6,10]

# naive implementation
print('Naive')
doubled_l = []
for num in numbers:
    doubled_l.append(num * 2)
print(doubled_l)
print()
'''
output: [2, 6, 12, 20]
'''

# list comprehension
print('List comprehension')
print([num * 2 for num in numbers])
print()
'''
output: [2, 6, 12, 20]
'''
