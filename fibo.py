def fib(n):
    if (n == 1):
        return 1, print(n)
    else:
        return fib(n - 1) + fib(n - 2)

def fff(n):
    f0, f1, f2 = 1, 0, None
    list = []
    for i in range(n):
        f2 = f1 + f0
        list.append(f2)

        f0 = f1
        f1 = f2

    for i in range(0, n):
        print(list[i],end=" ")
    number_list=[]
    for i in range(n):
        number_list.append(i+1)
    print(number_list)
    # for i in range(len(list)):
    #     if set(list[i]) == set(number_list[i]):
    #         print("+")
    #     else:
    #         print("-")

    # list3 = list(set(list).intersection(set(number_list)))
    # return list3
    for i in number_list:
        if i in list:
            print("+",end="")
        else:print("-",end="")
fff(7)


def fibo(n):
    for i in range(1, n):
        if i == 1:
            print("+", end="")

        else:
            return fibo(n - 1) + fibo(n - 2)
            print("-", end="")