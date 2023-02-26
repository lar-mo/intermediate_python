'''
Find friends whose name begins with "K"
'''

friends = ['Kat','Charles','Julie','Kim']

# naive implementation
print("Naive")
friends_k = []
for friend in friends:
    if friend[0].lower() == 'k':
        friends_k.append(friend)
print(friends_k)
print()

# list comprehension
print("List comprehension")
print([friend for friend in friends if friend[0].lower() == 'k'])
print()
