# tail = input()
# body = input()
# head = input()
#
# lst = [tail, body, head]
#
# lst[0], lst[2] = lst[2], lst[0]
# print(lst)

lst = list()
for _ in range(3):
    a = input()
    lst.append(a)
lst[0], lst[2] = lst[2], lst[0]

print(lst)