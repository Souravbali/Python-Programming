def sayHi(n):
    for i in range(int(n)):
        print('Hi', end=' ')
inp = input("Enter a function call like sayHi(3): ")
eval(inp)
