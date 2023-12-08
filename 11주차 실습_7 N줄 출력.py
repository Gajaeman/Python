s=1;
n=int(input('몇 줄을 출력하시겠습니까? :'))
for i in range(n):
    for j in range(n):
        print(f'{s%10}', end='')
        s+=1
    print()
