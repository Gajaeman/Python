A=[1,2,3,2,4,3.5]
# A=list(set(A)) 중복제거 방법 1 : 결과만 필요하면 간단하게 이용 가능
for i in A :
    if i not in B :
        B.append(i)
