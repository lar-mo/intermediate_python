'''
Print a list of tuples with team and their mascot
'''

teams = ['Rams','Seahawks','Padres','Chargers']
mascots = ['Goat','Bird','Bald guy','Bolt']

# naive implementation
print("Naive")
pairs = []
for i in range(len(teams)):
    pairs.append((teams[i],mascots[i]))
print(pairs)
print()

# zip()
print("Zip()")
print(list(zip(teams,mascots)))
print()
