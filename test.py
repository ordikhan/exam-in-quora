
def chess(list):
    n=list
    if n[0] == 1:
        print('number of king: ok',end=" ")
    elif n[0] > 1:
        print('number of king',1 - n[0],end="")
    else:
        print('number of king',n[0] - 1,end=" ")
    if n[1] == 1:
        print('number of Minister: ok',end=" ")
    elif n[1] > 1:
        print('number of Minister',1 - n[1],end=" ")
    else:
        print('number of Minister',n[1] - 1,end="" )
    if n[2] == 2:
        print('number of horse:ok',end=" ")
    elif n[2] > 2:
        print('number of horse',2 - n[2],end=" ")
    else:
        print('number of horse',n[2] - 2,end=" ")
    if n[3] == 2:
        print('number of bishop:ok',end=" ")
    elif n[3] > 2:
        print('number of bishop:', 2 - n[3],end=" ")
    else:
        print('number of bishop:',n[3] - 2,end=" ")
    if n[4] == 8:
        print('number of soldier:ok',end=" ")
    elif n[4] > 8:
        print('number of soldier',n[4] - 8,end=" ")
    else:
        print('number of soldier',8 - n[4],end=" ")
chess([1,2,3,4,5])