grades = list(map(int, input().split()))
av = sum(grades) / len(grades)
print(av)
if av >= 4:
    print("Допущен")
else:
    print("Недопущен")
