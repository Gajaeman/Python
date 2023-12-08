a=[-3.2,5.5,4.1,1.1,-1.3,2.7,0.5]
temp=a.copy()
temp.sort(reverse=True)
print(f'sorted={temp}')
for x in temp[:3]:
    while x in a:
        a.remove(x)
print(f'removed={a}')
