def sum(N):
    sum = 0
    for digits in str(N):
        sum = sum + int(digits)
    return sum

N = int(input("enter any number:"))
print(sum(N))