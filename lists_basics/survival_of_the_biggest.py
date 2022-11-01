# a = [1, 5, 7, 9]
# b = min(a)
# a.remove(b)
# print(a, b)

lst_of_integers_in_str = input().split(" ")
count_numbers_to_remove = int(input())
lst_of_integers_in_int = []
final_list = []

for digits in lst_of_integers_in_str:
    lst_of_integers_in_int.append(int(digits))

for i in range(count_numbers_to_remove):
    lst_of_integers_in_int.remove(min(lst_of_integers_in_int))

for j in lst_of_integers_in_int:
    j = str(j)
    final_list.append(j)


print((", ").join(lst_of_integers_in_int))