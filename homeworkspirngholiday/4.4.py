lst = [1, "hello", 2, "world", True]

new_lst = [x for x in lst if type(x) == str]

print(new_lst)



for x in lst:
    if type(x) == str:
        append.append(x)

