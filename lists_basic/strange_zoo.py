"""You are at the zoo, and the meerkats look strange.
You will receive 3 strings on separate lines, representing the tail, the body, and the head of an animal in that order. Your task is to re-arrange the elements in a list so that the animal looks normal again:
•	On the first position is the head;
•	On the second position is the body;
•	On the last one is the tail.
###################################EXAMPLES#######################################
Input:
my tail
my body seems on place
my head is on the wrong end!
Output: ['my head is on the wrong end!', 'my body seems on place', 'my tail']

Input:
tail
body
head
Output: ['head', 'body', 'tail']

Input:
T
B
H

Output: ['H', 'B', 'T']
"""

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