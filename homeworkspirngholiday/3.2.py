lst = [1, 2, 2, 3, 4, 4, 5]
res = []

for x in lst:
    if x not in res:
        res.append(x)

print(res)
