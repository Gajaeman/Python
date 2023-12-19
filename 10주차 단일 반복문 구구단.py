dan=2
for k in range(72):
    num=k%9+1
    print('%dx%d=%d '%(dan,num,dan*num),end='')
    if num==9:
        dan=dan+1
        print()