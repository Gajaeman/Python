result=0
n=int(input('10 이상의 양의 정수를 입력하세요 : '))
while n>0:
    r=n%10
    n=n//10
    result+=r
print(result)
