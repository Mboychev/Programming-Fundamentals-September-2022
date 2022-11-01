# version = [int(x) for x in input().split(".")]
#
# version[-1] += 1
#
# if version[-1] > 9:
#     version[-1] = 0
#     version[1] += 1
#
#     if version[1] > 9:
#         version[1] = 0
#         version[0] += 1
#
#
# version = [str(x) for x in version]
#
#
# print(".".join(version))

version = [int(x) for x in input().split(".")]

version[-1] += 1

for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1

print(".".join(str(y) for y in version))
