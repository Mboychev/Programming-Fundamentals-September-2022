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