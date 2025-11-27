#Cau10
# Khởi tạo các biến ban đầu
x = 10
y = 5
ncc = 3
number_of_closed_cases = 20

print(f"Giá trị ban đầu: x={x}, y={y}, number_of_closed_cases={number_of_closed_cases}")

# (a) x = x + 1
x += 1
print(f"(a) Sau x += 1: x = {x}") 
# x bây giờ là 11

# (b) x = x / 2
x /= 2
print(f"(b) Sau x /= 2: x = {x}")
# x bây giờ là 5.5 (kiểu float)

# (c) x = x - 1
x -= 1
print(f"(c) Sau x -= 1: x = {x}")
# x bây giờ là 4.5

# (d) x = x + y
x += y
print(f"(d) Sau x += y (với y=5): x = {x}")
# x bây giờ là 9.5

# (e) x = x - (y + 7)
x -= (y + 7)
print(f"(e) Sau x -= (y + 7) (tức x -= 12): x = {x}")
# x bây giờ là -2.5

# (f) x = 2 * x
x *= 2
print(f"(f) Sau x *= 2: x = {x}")
# x bây giờ là -5.0

# (g) number_of_closed_cases = number_of_closed_cases + 2 * ncc
number_of_closed_cases += 2 * ncc
print(f"(g) Sau number_of_closed_cases += 2 * ncc (tức 20 + 2*3 = 26): number_of_closed_cases = {number_of_closed_cases}")
# number_of_closed_cases bây giờ là 26