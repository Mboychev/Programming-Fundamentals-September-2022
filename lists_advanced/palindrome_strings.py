single_string = input().split(" ")
user_palindrome = input()


palindrome_list = [x for x in single_string if x == x[::-1]]
palindrome_count = palindrome_list.count(user_palindrome)
print(palindrome_list)
print(f"Found palindrome {palindrome_count} times")