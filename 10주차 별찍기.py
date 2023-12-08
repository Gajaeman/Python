for y in range(5):
    for x in range(10):
        print('*', end='')
    print('')


#외부 반복문 변수 이용
#행의 번호와 별의 개수가 일치하므로 변수를 하나로 맞춰서 사용
#별의 개수는 0부터 시작하면 안되므로 y의 값을 1부터 5까지로 할당
'''
for y in range(1,6):
    for x in range(y):
        print('*',end='')
    print()
'''
