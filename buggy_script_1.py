# buggy_script_1.py

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Result:", divide_numbers(10, 0))
