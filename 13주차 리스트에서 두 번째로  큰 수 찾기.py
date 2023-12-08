#Solution (1)
import random
list1=list(random.sample(range(1,100),10))
print('정렬 전 : ',list1)
list1.sort()
print('정렬 후 : ',list1)
print('두 번째로 큰 수 = ',list1[-2])



#Solution (2)
import random
list2=list(random.sample(range(1,101),10))
print('list2 : ', list2)
list2.remove(max(list2))
print('두 번째로 큰 수 = ',max(list2))
