def single_digit(n):
    sum = 0
    while n != 0:
        sum += n % 10
        n //= 10
    if sum<9:
        print(int(sum))
    else:
        n = sum
        single_digit(n)
single_digit(914)

