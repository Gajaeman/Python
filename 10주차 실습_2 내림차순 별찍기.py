a=int(input('양의 정수를 입력하세요 : '))
for y in range(1,a+1):
    for x in range(a-y+1):
        print('*',end='')
    print()
