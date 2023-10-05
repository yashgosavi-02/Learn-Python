# collection of well-defined objects

a = {3, 5, 5, 2}
print(a)  # returns unique elements and sorted
a.pop()  # removes random element from end, unique and sort
a.clear()  # removes all elements
a.add(4)  # adds element to set

a1 = {3, 5, 23, 5, 5, 5}
a2 = {3, 5, 23, 7, 8, 0}
print(a1.union(a2))  # elements of both sets
print(a1.intersection(a2))  # common elements of both sets

a3 = {3, 23}
print(a3.issubset(a1))  # checks if subset

# empty set
b = set()
