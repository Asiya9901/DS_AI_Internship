n=int(input("enter the number"))
def table(n):
    print("multiplication of ",n)
    for i in range(1,11):
        print(n, "x",i,"=",n*i)
table(n)