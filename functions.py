def callHello():
    print("Hello")

def callHelloName(name, ending):
    print("Hello", name)
    print(ending)

def letterGenerator(name,date):
    response = f"Hello ma'am,\nI'm {name} and I will be not present on {date}"
    print(response)

def average(a,b):
    return (a + b)/2


callHello()

callHelloName("Yash", "Thankyou")
callHelloName("Sourav", "Bye")

letterGenerator("Yash", "12-03-2023")

print(average(3, 4))
