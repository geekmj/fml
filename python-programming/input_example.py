name = input("Enter your name: ")
print("Hello there, {}!".format(name.title()))

num = int(float(input("Enter a number: ")))
print(num + 1)
print(name * num)

num = 30
x = eval('num + 42')
print(x)

num = eval(input("Input an expression: "))
print(num)