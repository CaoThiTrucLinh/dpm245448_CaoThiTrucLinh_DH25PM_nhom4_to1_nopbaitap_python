#Cau6
def read_two_digit_number(n):
    """Đọc số nguyên n (0 <= n <= 99) ra dạng chữ tiếng Việt."""
    
    if not (0 <= n <= 99):
        return "Số nhập vào không hợp lệ (ngoài khoảng 0-99)."
    
    # Danh sách từ vựng
    ones = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    
    if 0 <= n <= 9:
        return ones[n]

    tens_digit = n // 10
    ones_digit = n % 10
    
    result = ""
    
    # Xử lý hàng chục
    if tens_digit == 1:
        result += "mười"
    else:
        result += ones[tens_digit] + " mươi"
        
    # Xử lý hàng đơn vị
    if ones_digit == 0:
        pass # Không đọc nếu là số tròn chục
    elif ones_digit == 1 and tens_digit >= 2:
        result += " mốt" # Ví dụ: hai mốt, ba mốt
    elif ones_digit == 5 and tens_digit >= 1:
        result += " lăm" # Ví dụ: mười lăm, hai lăm
    else:
        result += " " + ones[ones_digit]
        
    return result.strip()

# Ví dụ kiểm tra
print("--- Câu 6: Đọc số ra dạng chữ ---")
n_a = 35
n_b = 5
n_c = 21
n_d = 70
print(f"n={n_a} => {read_two_digit_number(n_a)}")
print(f"n={n_b} => {read_two_digit_number(n_b)}")
print(f"n={n_c} => {read_two_digit_number(n_c)}")
print(f"n={n_d} => {read_two_digit_number(n_d)}")