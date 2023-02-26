'''
insert variable in printed sentence
'''

name = "John"

# naive implementation
print("Naive")
print("Hello", name)
print()

# f-string
print("f-string")
print(f"Hello {name}")
print()

# format()
print("Format")
print("Hello {}".format(name))
print()
