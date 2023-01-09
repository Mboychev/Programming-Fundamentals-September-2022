"""On the first line, you will receive words separated by a single space. On the second line, you will receive a
palindrome. First, you should print a list containing all the found palindromes in the sequence. Then, you should print
the number of occurrences of the given palindrome in the format: "Found palindrome {number} times".
###################################EXAMPLES#######################################
Input:
wow father mom wow shirt stats
wow
Output:
['wow', 'mom', 'wow', 'stats']
Found palindrome 2 times

Input:
hey how you doin? lol
mom
Output:
['lol']
Found palindrome 0 times
"""

single_string = input().split(" ")
user_palindrome = input()


palindrome_list = [x for x in single_string if x == x[::-1]]
palindrome_count = palindrome_list.count(user_palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")