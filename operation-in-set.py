# len()
# add()
# clear()
# copy()
# discart()

set1 = {1,5,8,13,19}
set2 = {3,6,8,12,1,10,5}

# union
print(set1|set2)
print(set1.union(set2))

# Intersection
print(set1&set2)
print(set1.intersection(set2))


# Difference

print(set1-set2)

# symerric_difference == union - intersection
print(set1^set2)
print(set1.symmetric_difference(set2))