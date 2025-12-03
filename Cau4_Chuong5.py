#Cau4
# -----------------------------------------------
# Câu 4: Các hàm quan trọng trong xử lý chuỗi Python
# -----------------------------------------------

s = "  Xin Chào Python 123  "

print("Chuỗi gốc:", repr(s))

# 1. Thay đổi chữ hoa – chữ thường
print("\n--- Thay đổi chữ hoa – chữ thường ---")
print("upper():", s.upper())
print("lower():", s.lower())
print("title():", s.title())
print("capitalize():", s.capitalize())
print("swapcase():", s.swapcase())

# 2. Tách – Ghép chuỗi
print("\n--- Tách – Ghép chuỗi ---")
words = s.split()     # Tách theo khoảng trắng
print("split():", words)
print("join():", "-".join(words))

# 3. Tìm kiếm – Thay thế
print("\n--- Tìm kiếm – Thay thế ---")
print("find('Python'):", s.find("Python"))
print("replace('Python', 'AI'):", s.replace("Python", "AI"))

# 4. Kiểm tra thuộc tính chuỗi
print("\n--- Kiểm tra thuộc tính chuỗi ---")
print("isalpha():", "ABC".isalpha())
print("isdigit():", "123".isdigit())
print("isalnum():", "A1B2".isalnum())
print("isspace():", "   ".isspace())
print("isupper():", "HELLO".isupper())
print("islower():", "hello".islower())

# 5. Loại bỏ khoảng trắng
print("\n--- Loại bỏ khoảng trắng ---")
print("strip():", repr(s.strip()))
print("lstrip():", repr(s.lstrip()))
print("rstrip():", repr(s.rstrip()))

# 6. Cắt chuỗi (slicing)
print("\n--- Cắt chuỗi (slicing) ---")
print("s[0:5]:", s[0:5])
print("s[::-1] (đảo chuỗi):", s[::-1])

# 7. startswith() & endswith()
print("\n--- Kiểm tra bắt đầu / kết thúc ---")
print("startswith('Xin'):", s.strip().startswith("Xin"))
print("endswith('123'):", s.strip().endswith("123"))

# 8. Độ dài chuỗi
print("\n--- Độ dài chuỗi ---")
print("len(s):", len(s))

