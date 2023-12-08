place=int(input('관광지 수를 입력하세요 : '))
price=[0]*place
for k in range(place):
    price[k]=int(input('입장료를 입력하세요 : '))
price.sort()
totalprice=price[0] + price[-1]
print(totalprice)
