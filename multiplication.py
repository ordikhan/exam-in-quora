def  multiplication (n):
    i = 1
    j = 1

    while i <= n:
        while j <= n:
            print(i * j, end="\t")
            j += 1
        j = 1
        i += 1
        print()
multiplication(5)
