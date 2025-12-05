#Cau5
# Dữ liệu bài 5
lst = [20, 1, -34, 40, -8, 60, 1, 3]

print("\n--- Kết quả Bài tập 5 ---")
# (a) lst
print(f"(a) lst là: {lst}")

# (b) lst[0:3]
# Lấy từ chỉ mục 0 đến (3-1)=2. Kết quả: [20, 1, -34]
print(f"(b) lst[0:3] là: {lst[0:3]}")

# (c) lst[4:8]
# Lấy từ chỉ mục 4 đến (8-1)=7. Kết quả: [-8, 60, 1, 3]
print(f"(c) lst[4:8] là: {lst[4:8]}")

# (d) lst[4:3]
# Start index lớn hơn End index. Kết quả: [] (list rỗng)
print(f"(d) lst[4:3] là: {lst[4:3]}")

# (e) lst[-5:-3]
# Chỉ mục âm: -5 là 40, -3 là -8. Lấy từ -5 đến (-3-1)=-4. Kết quả: [40, -8]
print(f"(e) lst[-5:-3] là: {lst[-5:-3]}")

# (f) lst[2: -3]
# Chỉ mục 2 là -34. Chỉ mục -3 là 60. Lấy từ 2 đến (-3-1)=-4. Kết quả: [-34, 40, -8]
print(f"(f) lst[2:-3] là: {lst[2:-3]}")

# (g) lst[4:]
# Lấy từ chỉ mục 4 đến hết. Kết quả: [-8, 60, 1, 3]
print(f"(g) lst[4:] là: {lst[4:]}")

# (h) lst[:]
# Lấy bản sao của toàn bộ list. Kết quả: [20, 1, -34, 40, -8, 60, 1, 3]
print(f"(h) lst[:] là: {lst[:]}")

# (i) lst[4]
# Phần tử tại chỉ mục 4. Kết quả: -8
print(f"(i) lst[4] là: {lst[4]}")

# (j) lst[1:5]
# Lấy từ chỉ mục 1 đến (5-1)=4. Kết quả: [1, -34, 40, -8]
print(f"(j) lst[1:5] là: {lst[1:5]}")

# (k) -34 in lst
# Kiểm tra xem -34 có tồn tại trong list không. Kết quả: True
print(f"(k) -34 in lst là: {-34 in lst}")

# (l) -34 not in lst
# Kiểm tra xem -34 có KHÔNG tồn tại trong list không. Kết quả: False
print(f"(l) -34 not in lst là: {-34 not in lst}")

# (m) len(lst)
# Độ dài của list. Kết quả: 8
print(f"(m) len(lst) là: {len(lst)}")