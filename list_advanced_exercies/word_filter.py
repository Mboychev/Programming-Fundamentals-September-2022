"""Using comprehension, write a program that receives some text, separated by space, and take only those words whose
length is even. Print each word on a new line.
###################################EXAMPLES#######################################
Input: kiwi orange banana apple
Output:
kiwi
orange
banana

Input: pizza cake pasta chips
Output: cake
"""

some_text = input().split()

even_length_words = [word for word in some_text if len(word) % 2 == 0]

print("\n".join(even_length_words))
