"""Write a function that receives a string and a counter n. The function should return a new string –
the result of repeating the old string n times. Print the result of the function. Try using lambda.
###################################EXAMPLES#######################################
Input:
abc
3
Output: abcabcabc

Input:
String
2
Output: StringString """


current_string = input()
current_number = int(input())

repeating_string = lambda a, b: a * b

result = repeating_string(current_string, current_number)
print(result)