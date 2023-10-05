l1 = [3, 5, 2, 'Harry', True]
print(type(l1))
print(l1)
# lists are mutable (changeable)

l1.remove('Harry')  # remove from list
print(l1)

l1.append(12)  # appends at end
print(l1)

l1.insert(0, 'Yash')  # insert at given index
print(l1)
l1.pop()  # removes from end
print(l1)
l1.extend([7, 8, 9, 10])  # add another list
print(l1)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.extend(list2)  # merges two list
print(list1)

l1.clear()  # remove all elements
print(l1)

list3 = list1.copy()  # copies elements of list1 to list3
print(list3)

print(list3.index(5))  # returns index of element
