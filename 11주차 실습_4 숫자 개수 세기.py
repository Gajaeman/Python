n=int(input('양의 정수를 입력하세요 :'))
cnt=0
while n : 
    r=n%10
    n=n//10
    if r == 3:
        cnt+=1
print(f'3의 개수는 {cnt}개 입니다.')


# while n,n!=0,n>0 모두 동일
# while n : n이 0이되면 반복문 종료


'''
a=int(input('양의 정수를 입력하세요 :'))
b,d = 10,0
while a*10>b :          
    c=a%b
    while c>10:
        c=c//10
    if c == 3 :
        d+=1
    b*=10
print(f'3의 개수는 {d}개 입니다.')
'''
