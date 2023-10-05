# empty dictionary
# stored in key : value
# dictionary is mutable (changeable)
d = {}
print(type(d))

dict1 = {"good": "something pleasant", "fetch": "to bring", "1": "The number 1"}
print(dict1["fetch"])  # prints value for provided key

marks = {"Yash": 78, "Tanvi": 90, "Aarya": 88, "Shourya": 93}
print(marks["Shourya"])

marks["Swara"] = 89  # adding key:value to dict at end
print(marks)

print(marks.get("Yash Gosavi"))  # returns none, as no key of name and value is present

print(marks.get("Yash"))  # returns value of provided key without error else none

print(marks.keys())  # return all keys
print(marks.values())  # return all values
print(marks.items())  # return each item of dictionary
print(len(marks))  # return count of items in dictionary



