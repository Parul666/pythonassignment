N = int(input("enter a number:"))
fib = [0,1]

for i in range(N-1):
    fib.append(fib[-1] + fib[-2])

for i in fib:
    print(i," ",end = "")
