a=[1,4,7,9,10]
b=[11,13,17,18,22]
#   c=a[::2]+b[1::2]로 표현도 가능
c=a[0:5:2]+b[1:5:2]
print(c)
