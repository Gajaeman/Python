num=int(input('선수 인원 수를 입력하세요 : '))
no=[]
rec={}

for x in range(num):
    i=int(input('참가 번호를 입력하세요 : '))
    no.append(i)

for y in no:
    k=int(input('기록을 입력하세요(초단위) : '))
    rec[y]=k

lank=sorted(rec.items(),key=lambda x: x[1])

for z in range(3):
    h=(lank[z][1]//3600)
    m=(lank[z][1]%3600)//60
    sec=(lank[z][1]%3600)%60
    print(lank[z][0],h,m,sec)
