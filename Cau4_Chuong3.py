#Cau4
x = 3
y = 5
z = 7

print("--- Câu 4 ---")
print(f"Giá trị ban đầu: x = {x}, y = {y}, z = {z}\n")

# a) x == 3
result_a = x == 3
print(f"(a) x == 3: {result_a}")

# b) x < y
result_b = x < y
print(f"(b) x < y: {result_b}")

# c) x < y - y
# Thay thế: 3 < 5 - 5  => 3 < 0
result_c = x < y - y
print(f"(c) x < y - y: {result_c}")

# d) x <= y
result_d = x <= y
print(f"(d) x <= y: {result_d}")

# e) x != y - 2
# Thay thế: 3 != 5 - 2  => 3 != 3
result_e = x != y - 2
print(f"(e) x != y - 2: {result_e}")

# f) x < 10
result_f = x < 10
print(f"(f) x < 10: {result_f}")

# g) x >= 0 and x < 10
# Thay thế: 3 >= 0 and 3 < 10  => True and True
result_g = x >= 0 and x < 10
print(f"(g) x >= 0 and x < 10: {result_g}")

# h) x < 0 and x < 10
# Thay thế: 3 < 0 and 3 < 10  => False and True
result_h = x < 0 and x < 10
print(f"(h) x < 0 and x < 10: {result_h}")

# i) x >= 0 and x < 2
# Thay thế: 3 >= 0 and 3 < 2  => True and False
result_i = x >= 0 and x < 2
print(f"(i) x >= 0 and x < 2: {result_i}")

# j) x < 0 or x < 10
# Thay thế: 3 < 0 or 3 < 10  => False or True
result_j = x < 0 or x < 10
print(f"(j) x < 0 or x < 10: {result_j}")

# k) x >= 0 or x < 10
# Thay thế: 3 >= 0 or 3 < 10  => True or True
result_k = x >= 0 or x < 10
print(f"(k) x >= 0 or x < 10: {result_k}")

# l) x < 0 or x > 10
# Thay thế: 3 < 0 or 3 > 10  => False or False
result_l = x < 0 or x > 10
print(f"(l) x < 0 or x > 10: {result_l}")