names = input()


sorted_nums = sorted(names.split(", "), key=lambda x: (-(len(x)), x))

print(sorted_nums)
