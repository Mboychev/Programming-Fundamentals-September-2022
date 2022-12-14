"""Anonymous has created a hyper cyber virus, which steals data from the CIA. The virus is known for its innovative and
unbelievably clever merging and dividing data into partitions. As the lead security developer in the CIA, you have been
tasked to analyze the software of the virus and observe its actions on the data.
You will receive a single input line containing strings, separated by spaces. The strings may contain any ASCII
character except whitespace. Then you will begin receiving commands in one of the following formats:
•	merge {startIndex} {endIndex}
•	divide {index} {partitions}
Every time you receive the merge command, you must merge all elements from the startIndex to the endIndex.
In other words, you should concatenate them.
Example: {abc, def, ghi} -> merge 0 1 -> {abcdef, ghi}
If any of the given indexes is out of the array, you must take only the range that is inside the array and merge it.
Every time you receive the divide command, you must divide the element at the given index into several small substrings
with equal length. The count of the substrings should be equal to the given partitions.
Example: {abcdef, ghi, jkl} -> divide 0 3 -> {ab, cd, ef, ghi, jkl}
If the string cannot be exactly divided into the given partitions, make all partitions except the last with equal
lengths and make the last one - the longest.
Example: {abcd, efgh, ijkl} -> divide 0 3 -> {a, b, cd, efgh, ijkl}
The input ends when you receive the command "3:1". At that point, you must print the resulting elements,
joined by a space.
Input
•	The first input line will contain the array of data.
•	On the next several input lines, you will receive commands in the format specified above.
•	The input ends when you receive the command "3:1".
Output
•	As output, you must print a single line containing the elements of the array, joined by a space.
Constrains
•	The strings in the array may contain any ASCII character except whitespace.
•	The startIndex and the endIndex will be in the range [-1000…1000].
•	The endIndex will always be greater than the startIndex.
•	The index in the divide command will always be inside the array.
•	The partitions will be in the range [0…100].
•	Allowed working time/memory: 100ms / 16MB.
###################################EXAMPLES#######################################
Input:
Ivo Johny Tony Bony Mony
merge 0 3
merge 3 4
merge 0 3
3:1
Output: IvoJohnyTonyBonyMony

Input:
abcd efgh ijkl mnop qrst uvwx yz
merge 4 10
divide 4 5
3:1
Output: abcd efgh ijkl mnop qr st uv wx yz
"""


def merge_func(start_index, end_index, text):
    if start_index < 0:
        start_index = 0
    joined_string = ''
    if end_index >= len(text):
        end_index = len(text) - 1
    if start_index <= len(text):
        for index in range(start_index, end_index + 1):
            joined_string += text[index]
        text[start_index] = joined_string
        for index_a in range(end_index, start_index, -1):
            text.pop(index_a)

    return text


def divide_func(index, partitions, text):

    if partitions > 0:
        for current_index in range(len(text)):
            if current_index == index:

                current_word = text[current_index]
                partitions_length = len(current_word)//partitions
                partition_to_add = len(current_word) % partitions
                text.pop(current_index)

                for index_of_partition in range(index, index + partitions):
                    part_to_insert = current_word[0:partitions_length]
                    text.insert(index_of_partition, part_to_insert)
                    current_word = current_word[partitions_length::]

                if partition_to_add > 0:
                    text[index + partitions - 1] = text[partitions - 1] + current_word
    return text


array_of_data = input().split(" ")

while True:

    data = input()

    if data == "3:1":
        break

    command, first_num, second_num = data.split(" ")

    if command == "merge":
        result = merge_func(int(first_num), int(second_num), array_of_data)

    elif command == "divide":
        result = divide_func(int(first_num), int(second_num), array_of_data)

print(" ".join(result))
