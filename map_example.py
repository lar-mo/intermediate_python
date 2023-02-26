'''
Print list of numbers that were doubled
'''

numbers = [2,4,8,16]

# naive implementation
print("Naive")
doubled_n = []
for num in numbers:
    doubled_n.append(num*2)
print(doubled_n)
print()

# function
print("Function")
def double(num):
    return num*2

doubled_n2 = []
for num in numbers:
    doubled_n2.append(double(num))
print(doubled_n2)
print()

# map()
print("Map()")
print(list(map(double,numbers)))
print()
