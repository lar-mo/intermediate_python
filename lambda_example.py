'''
multiply two numbers and print result
'''

# naive implementation
print('Naive')
x,y = 2,3
print(x*y)
print()
'''
output: 6
'''

# function
print('Function')
def multiply_f(x,y):
    return x*y
print(multiply_f(2,3))
print()
'''
output: 6
'''

# lambda function
print('Lambda')
multiply = lambda x,y: x*y
print(multiply(2,3))
print()
'''
output: 6
'''

# another variation
print('Lambda, v2')
print((lambda x,y: x*y)(2,3))
print()
'''
output: 6
'''
