list1 = (23, 4, 35, 4, 345)
set1 = set()
set2 = {}
for i in list1:
    set2[i] = set2.get(i, 0) + 1
    set1.add(i if set2[i] < 2 else str(i) * set2[i])
print(*set1)