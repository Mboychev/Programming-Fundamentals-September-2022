"""Write a program that reads the path to a file and subtracts the file name and its extension.
###################################EXAMPLES#######################################
Input: C:\Internal\training-internal\Template.pptx
Output:
File name: Template
File extension: pptx


Input: C:\Projects\Data-Structures\LinkedList.cs
Output:
File name: LinkedList
File extension: cs
"""

file_path = input().split("\\")[-1]
file_name, file_extension = file_path.split(".")
print(f"File name: {file_name}")
print(f"File extension: {file_extension}")


