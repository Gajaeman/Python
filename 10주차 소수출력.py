for x in range(2,11):
    isPrime=True
    for i in range(2,x//2+1):
        if x%i==0:
            isPrime=False
            break
    if isPrime:
        print(x)

#x//2+1 로 끝값을 지정하면 데이터 할당량 감소
