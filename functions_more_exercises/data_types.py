"""Write a function that, depending on the first line of the input, reads one of the following strings: "int", "real",
or "string".
•	If the data type is an int, multiply the number by 2.
•	If the data type is real, multiply the number by 1.5 and format the result to the second decimal point.
•	If the data type is a string, surround the input with "$".
Print the result on the console.
###################################EXAMPLES#######################################
Input:
int
5
Output: 10

Input:
real
2
Output: 3.00

Input:
string
hello
Output: $hello$
"""


def data_types(data_type, user_data):
    if data_type == "int":
        result = int(user_data) * 2
        return result

    elif data_type == "string":
        result = f"${user_data}$"
        return result

    elif data_type == "real":
        result = float(user_data) * 1.5
        return f"{result:.2f}"


user_data_type = input()
data = input()

print(data_types(user_data_type, data))