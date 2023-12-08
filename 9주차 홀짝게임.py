import random as r
userwin, comwin = 0, 0
for e in range(3):
    u = int(input('홀 0, 짝 1, 입력 : '))
    c=r.randint(0,1)
#   c=r.range(2)
    if u==c :
        print('사용자 승')
        userwin+=1
    else :
        print('컴퓨터 승')
        comwin+=1
print('userwin=%d, comwin=%d' %(userwin, comwin))
