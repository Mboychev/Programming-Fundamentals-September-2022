"""You are fed up with changing the version of your software manually. Instead, you will create a little script that
will make it for you.
You will be given a string representing the version of your software in the format: "{n1}.{n2}.{n3}". Your task is to
print the next version. For example, if the current version is "1.3.4", the next version will be "1.3.5".
The only rule is that the numbers cannot be greater than 9. If it happens, set the current number to 0 and increase the
previous number. For more clarification, see the examples below.
Note: there will be no case in which the first number will become greater than 9.
###################################EXAMPLES#######################################
Input: 1.2.3
Output: 1.2.4

Input: 1.3.9
Output: 1.4.0

Input: 3.9.9
Output: 4.0.0
"""
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
# version = [str(x) for x in version]
# print(".".join(version))

version = [int(x) for x in input().split(".")]

version[-1] += 1

for index in range(len(version) - 1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        if index - 1 >= 0:
            version[index - 1] += 1

print(".".join(str(y) for y in version))
