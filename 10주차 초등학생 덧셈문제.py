# 예시답안
import random

while True:
    x=random.randint(1,100)
    y=random.randint(1,100)

    answer = int(input(f'{x} + {y} = '))

    if answer == x+y:
        print('잘했어요!!')
    else:
        print('틀렸어요!!')
        break





# break 사용 X
'''
import random
flag=True

while flag:
    x=random.randint(1,100)
    y=random.randint(1,100)

    answer = int(input(f'{x} + {y} = '))

    if answer == x+y:
        print('잘했어요!!')
    else:
        print('틀렸어요!!')
        flag=False
'''




'''
import random as r

while True:
    a=r.randint(1,99)
    b=r.randint(1,99)
    c=a+b
    d=int(input(f'{a} + {b} = '))

    if c=d:
        print('맞았어요!!')
    else:
        print('틀렸어요!!')
        break

'''
