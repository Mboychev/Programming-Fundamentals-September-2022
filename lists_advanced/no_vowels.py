text = input()

vowels = ['a', 'o', 'u', 'e', 'i']

result = "".join([x for x in text if x.lower() not in vowels])
print(result)