#Cau4
# Dữ liệu bài 4
lst = [3, 0, 1, 5, 2]
x = 2

print("--- Kết quả Bài tập 4 ---")
# (a) lst[0]
print(f"(a) lst[0] là: {lst[0]}")

# (b) lst[3]
print(f"(b) lst[3] là: {lst[3]}")

# (c) lst[x]
print(f"(c) lst[x] (lst[2]) là: {lst[x]}")

# (d) lst[-x]
# Chỉ mục âm -2
print(f"(d) lst[-x] (lst[-2]) là: {lst[-x]}")

# (e) lst[x + 1]
# Chỉ mục x+1 = 3
print(f"(e) lst[x + 1] (lst[3]) là: {lst[x + 1]}")

# (f) lst[x] + 1
# Giá trị lst[x] = lst[2] = 1. Kết quả là 1 + 1 = 2
print(f"(f) lst[x] + 1 (1 + 1) là: {lst[x] + 1}")

# (g) lst[lst[x]]
# lst[x] = lst[2] = 1. Kết quả là lst[1] = 0
print(f"(g) lst[lst[x]] (lst[1]) là: {lst[lst[x]]}")

# (h) lst[lst[lst[x]]]
# lst[x] = 1. lst[lst[x]] = 0. Kết quả là lst[0] = 3
print(f"(h) lst[lst[lst[x]]] (lst[0]) là: {lst[lst[lst[x]]]}")