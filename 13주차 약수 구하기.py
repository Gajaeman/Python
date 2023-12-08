def getDivisiors(n):
    res=[1]
    for i in range(2,n//2+1):
        if n%i==0:
            res.append(i)
    return(res+[num])

num=int(input('자연수를 입력하세요 : '))
print(getDivisiors(num))





'''
a=int(input('자연수를 입력하세요 : '))
c=[]
for b in range(1,a+1):
    if a%b==0:
        b.append(c)
print(c)
'''
