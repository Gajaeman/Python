arr=list(map(int, input('성적을 입력하시오 :').split()))
count=0

print(f'성적 평균 = {int(sum(arr)/len(arr))}')
print(f'최대점수 = {max(arr)}')
print(f'최소점수 = {min(arr)}')

for score in arr:
    if score>=80:
        count+=1
print('80점 이상=', count)
