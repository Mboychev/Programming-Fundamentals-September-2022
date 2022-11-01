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