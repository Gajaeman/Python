a=int(input('양의 정수를 입력하세요 : '))
for y in range(a):
    for x in range(a-y,0,-1):
        print(x,end=' ')
    print()
