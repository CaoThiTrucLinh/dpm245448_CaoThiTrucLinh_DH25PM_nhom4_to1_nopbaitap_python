#Cau7
# ===== Một số cách nhập dữ liệu từ bàn phím trong Python =====

# 1. Nhập chuỗi từ bàn phím
ten = input("Nhập tên của bạn: ")
print("Tên của bạn là:", ten)

# 2. Nhập số nguyên (int)
tuoi = int(input("Nhập tuổi của bạn: "))
print("Tuổi của bạn:", tuoi)

# 3. Nhập số thực (float)
diem = float(input("Nhập điểm của bạn: "))
print("Điểm của bạn:", diem)

# 4. Nhập nhiều giá trị trên cùng một dòng (split)
a, b = input("Nhập hai số, cách nhau bởi dấu cách: ").split()
print("Bạn đã nhập:", a, b)

# 5. Nhập nhiều số và chuyển thành danh sách (map + list)
ds = list(map(int, input("Nhập danh sách số (cách nhau bởi khoảng trắng): ").split()))
print("Danh sách bạn nhập:", ds)