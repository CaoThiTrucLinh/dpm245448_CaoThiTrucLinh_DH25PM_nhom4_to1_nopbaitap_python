#Cau5
# Tạm dịch đoạn mã logic sang hàm Python để dễ kiểm tra
def evaluate_condition(i, j, k):
    # if i < j:
    if i < j:
        # if j < k:
        if j < k:
            i = j
            j = k
        # else: (tức là j >= k)
        else:
            j = k
    # else: (tức là i >= j)
    else:
        # if i > k:
        if i > k:
            j = i
            i = k
        # else: (tức là i <= k)
        else:
            j = k
    
    # print("i = ", i, ", j = ", j, ", k = ", k)
    print(f"i = {i}, j = {j}, k = {k}")

print("\n--- Câu 5 ---")

# a) i = 3, j = 5, and k = 7
print("(a) i = 3, j = 5, k = 7. Kết quả:")
evaluate_condition(3, 5, 7)

# b) i = 3, j = 7, and k = 5
print("\n(b) i = 3, j = 7, k = 5. Kết quả:")
evaluate_condition(3, 7, 5)

# c) i = 5, j = 3, and k = 7
print("\n(c) i = 5, j = 3, k = 7. Kết quả:")
evaluate_condition(5, 3, 7)

# d) i = 5, j = 7, and k = 3
print("\n(d) i = 5, j = 7, k = 3. Kết quả:")
evaluate_condition(5, 7, 3)

# e) i = 7, j = 3, and k = 5
print("\n(e) i = 7, j = 3, k = 5. Kết quả:")
evaluate_condition(7, 3, 5)

# f) i = 7, j = 5, and k = 3
print("\n(f) i = 7, j = 5, k = 3. Kết quả:")
evaluate_condition(7, 5, 3)