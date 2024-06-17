num = int(input("enter any no.:"))
factorial = 1
if num <0 :
    print("the factorial of:",num,"does not exists")
elif num == 0 :
    print("the factorial of:",num,"is equal to 1")
else :
    for i in range(1,num+1):
        factorial = factorial*i
    print("the factorial of:",num,"is",factorial)
