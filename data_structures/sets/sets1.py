print("\n-----Creating Sets-----")
# Creating an empty set
emptySet = set()

# Creating a set with elements
mySet = {1, 2, 3, 4, 5}

# Converting a list to a set
myList = [1,2,3,4,5]
convertedSet = set(myList)

print(type(emptySet), type(mySet), type(convertedSet)) # <class 'set'> <class 'set'> <class 'set'>


print("\n-----Basic Set Operations-----")
mySet = set()

# Adding elements to a set
mySet.add(6)
mySet.update([7,8,9])
print(mySet) # {8, 9, 6, 7}

# Removing elements from a set
mySet.remove(6)
mySet.discard(1) # Removes 1 if it exists, does nothing if it doesn't
print(mySet.pop()) # Removes and returns an arbitrary element

# Clearing all elements form a set
mySet.clear()
print(mySet) # set()


print("\n-----Set Operations-----")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union of 2 sets
unionSet = set1.union(set2)

# Intersection of 2 sets
intersectionSet = set1.intersection(set2)

# Difference between 2 sets
differenceSet = set1.difference(set2)

# Symmetric Difference (elements present in either of the sets, but not both)
symmetricDiffSet = set1.symmetric_difference(set2)

print("Union Set:", unionSet)
print("Intersection Set:", intersectionSet)
print("Difference Set:", differenceSet)
print("Symmetric Difference:", symmetricDiffSet)


print("\n-----Set Methods-----")
set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5, 6, 7, 8}  # Modified set2 to include all elements of set1 and more

# Copying a set
copySet = set1.copy()

# Checking if a set is a subset or superset of another set
isSubset = set1.issubset(set2)
isSuperset = set2.issuperset(set1)

# Checking if set have no elements in common
isDisjoint = set1.isdisjoint(set2)

print("isSubset:", isSubset)
print("isSuperset:", isSuperset)
print("isDisjoint:", isDisjoint)


print("\n-----Frozen Sets-----")
frozenSet = frozenset([1,2,3,4,5])

# Frozen sets are immutable
# frozen_set.add(6)  # This will raise an error


print("\n-----Set Comprehension-----")
squaredSet = {x ** 2 for x in range(1,6)}
evenSquares = {x ** 2 for x in range(1,6) if x % 2 == 0}

print("Squared Set:", squaredSet)
print("Even Squares:", evenSquares)