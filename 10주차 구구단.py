for dan in range(2,10):
    print('\n%d단:' % dan, end = '')
    for num in range(1,10):
        print(f'{dan}*{num}={dan*num}',end='  ')
    print()


''''
\n을 쓰고싶지 않다면
for dan in range(2,10):
    print('%d단:' % dan, end = '')
    for num in range(1,10):
        print(f'{dan}*{num}={dan*num}  ',end='')
    print()
와 같이 외부 반복문에 print()를 넣어주면 된다


띄어쓰기 출력은
print(f'{dan}*{num}={dan*num}',end='  ')
와 같이 end에 공백을 할당하거나
print(f'{dan}*{num}={dan*num} ',end='')
와 같이 print문에 공백을 할당할 수 있다
'''
