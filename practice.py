a = [200, 250, 300, 280, 500]
#b = [i * 1.3 for i in a]
b = list(map(lambda x : x*1.3, a))
print(b)