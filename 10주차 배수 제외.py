nums=[]
for x in range(1,21):
    if x%3==0 or x%7==0:
        continue
    nums.append(x)
print(nums)
