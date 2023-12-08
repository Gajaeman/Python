a='korea'
a=list(a)
buff=[]
for e in a[:4]:
    buff.append(e)
for _ in range(3): #'_'도 변수로 사용 가능
    b=buff.pop()   # pop()의 괄호 디폴트 값은 -1, pop메소드는 한 번 반환 후 삭제
    print(b)
