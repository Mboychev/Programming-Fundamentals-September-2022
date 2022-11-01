sequence = input().split(" ")
final_result = []

for current_number in sequence:
    final_result.append(abs(float(current_number)))
print(final_result)