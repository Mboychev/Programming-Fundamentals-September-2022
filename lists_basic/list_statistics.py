"""On the first line, you will receive a number n. On the following n lines, you will receive integers. You should create and print two lists:
•	One with all the positives (including 0) numbers
•	One with all the negatives numbers
Finally, print the following message:
"Count of positives: {count_positives}
Sum of negatives: {sum_of_negatives}"
###################################EXAMPLES#######################################
Input:
5
10
3
2
-15
-4
Output:
[10, 3, 2]
[-15, -4]
Count of positives: 3
Sum of negatives: -19

Input:
6
11
2
35
599
31
20

Output:
6
11
2
35
599
31
20
"""

number_of_lines = int(input())
positive_num = []
negative_num = []

for i in range(number_of_lines):

    current_num = int(input())

    if current_num >= 0:
        positive_num.append(current_num)
    else:
        negative_num.append(current_num)
print(positive_num)
print(negative_num)
print(f"Count of positives: {len(positive_num)}")
print(f"Sum of negatives: {sum(negative_num)}")