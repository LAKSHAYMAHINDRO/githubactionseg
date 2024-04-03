def calculator(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    else:
        return "Invalid operation"

# Example usage
result_add = calculator('add', 5, 3)
print("5 + 3 =", result_add)

result_subtract = calculator('subtract', 10, 4)
print("10 - 4 =", result_subtract)

result_multiply = calculator('multiply', 6, 2)
print("6 * 2 =", result_multiply)

result_divide = calculator('divide', 12, 3)
print("12 / 3 =", result_divide)
