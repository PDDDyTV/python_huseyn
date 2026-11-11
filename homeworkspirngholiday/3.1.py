lst = list(map(int, input().split()))
lst[lst.index(max(lst))] = 0
print(lst)