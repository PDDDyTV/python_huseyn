lst = list(map(int, input().split()))
res = []
for i in lst:
    res = [i] + res
print(res)
