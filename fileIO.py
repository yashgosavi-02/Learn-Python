s = "Hello, My name is Yash & I am from Aurangabad"

# writing into a file:

with open("hello.txt", "w") as f:
    f.write(s)

# writes object of s in file hello.txt

# fp = open("hello.txt", "w")
# fp.write(s)
# fp.close()

# Reading a file
# with open("hello.txt","r") as f:
#     response = f.read()
#     print(response)
#

# fp = open("hello.txt", "r")
# response = fp.read()
# print(response)

# appending to file

with open("hello.txt", "a") as f:
    f.write("\nI like bike rides")