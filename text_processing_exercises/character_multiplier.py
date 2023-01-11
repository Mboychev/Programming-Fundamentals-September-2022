"""Create a program that receives two strings on a single line separated by a single space.
Then, it prints the sum of their multiplied character codes as follows: multiply str1[0] with str2[0]
and add the result to the total sum, then continue with the next two characters.
If one of the strings is longer than the other,
add the remaining character codes to the total sum without multiplication.
###################################EXAMPLES#######################################
Input: George Peter
Output: 52114

Input: 123 522
Output: 7647

Input: a aaaa
Output: 9700
"""


string_one, string_two = input().split()

total_sum = 0

if len(string_one) > len(string_two):

    for index in range(len(string_two)):
        total_sum += ord(string_one[index]) * ord(string_two[index])

    for index in range(len(string_two), len(string_one)):
        total_sum += ord(string_one[index])

elif len(string_one) < len(string_two):

    for index in range(len(string_one)):
        total_sum += ord(string_two[index]) * ord(string_one[index])

    for index in range(len(string_one), len(string_two)):
        total_sum += ord(string_two[index])
else:
    
    for index in range(len(string_one)):
        total_sum += ord(string_one[index]) * ord(string_two[index])

print(total_sum)