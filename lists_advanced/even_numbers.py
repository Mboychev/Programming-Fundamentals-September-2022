numbers = list(map(int, input().split(", ")))

found_indeces_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "No", numbers)
even_indeces = list(filter(lambda a: a != "No", found_indeces_or_no))
print(even_indeces)