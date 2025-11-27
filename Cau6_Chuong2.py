#Cau6
# Ví dụ về các toán tử số học
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print(f"10 % 3 = {10 % 3}")
print(f"2 ** 4 = {2 ** 4}")

# Ví dụ về toán tử logic
print(f"True and False is {True and False}")
print(f"5 > 3 or 1 > 10 is {5 > 3 or 1 > 10}")

# Ví dụ về toán tử is
list_a = [10]
list_b = list_a  # Cả hai tham chiếu cùng một đối tượng
list_c = [10]    # Đối tượng mới, có giá trị giống hệt

print(f"list_a is list_b: {list_a is list_b}")  # True
print(f"list_a is list_c: {list_a is list_c}")  # False