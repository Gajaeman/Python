def getDivisiors(n):
    res=[]
    for i in range(1,n//2+1):
        if n%i==0:
            res.append(i)
    return(res)
def checkPerfect(n):
    div=getDivisiors(n)
    return sum(div)==n
num=[]
k=int(input('몇 이하의 완전수를 구하시겠습니까? : '))
for n in range(2,k+1):
    if checkPerfect(n):
        num.append(n)
print(f'{k}이하의 완전수는 = {num}')
