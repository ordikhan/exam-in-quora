list = []
while True:
    a = eval(input('enter the number:'))
    if a == 0:
        break
    else:
        list.append(a)
# for i in reversed(len(list)):
#     print(list[i], end="")


for item in list[::-1]:
    print (item,end="")555
