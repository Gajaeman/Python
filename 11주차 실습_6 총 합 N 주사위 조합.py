N=int(input('3~18 사이의 정수를 입력하세요 : '))
for a in range(1,7):
    for b in range(1,7):
        for c in range(1,7):
            if a+b+c==N:
                print("%d %d %d"%(a,b,c))
