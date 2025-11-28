#Cau8
def calculate(a, b, operator):
    """Thực hiện phép toán cơ bản giữa a và b."""
    
    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
        if b == 0:
            return "Lỗi: Không thể chia cho 0!"
        result = a / b
    else:
        return f"Lỗi: Phép toán '{operator}' không được hỗ trợ."
    
    return result

# Ví dụ kiểm tra
print("\n--- Câu 8: Thực hiện phép toán ---")
a_val = 10
b_val = 3

print(f"{a_val} + {b_val} = {calculate(a_val, b_val, '+')}")
print(f"{a_val} - {b_val} = {calculate(a_val, b_val, '-')}")
print(f"{a_val} * {b_val} = {calculate(a_val, b_val, '*')}")
print(f"{a_val} / {b_val} = {calculate(a_val, b_val, '/')}")
print(f"{a_val} / 0 = {calculate(a_val, 0, '/')}")