#Cau9
def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def xu_ly_mang_so_tu_nhien(M):
    """Phân loại các phần tử trong mảng M theo tính chất chẵn/lẻ và nguyên tố."""
    
    # 1. Chẵn/Lẻ
    so_le = [x for x in M if x % 2 != 0]
    so_chan = [x for x in M if x % 2 == 0]
    
    # 2. Nguyên tố/Không nguyên tố
    so_nguyen_to = [x for x in M if is_prime(x)]
    # Lưu ý: 0 và 1 không phải là số nguyên tố, nhưng cũng không phải là hợp số (non-prime)
    so_khong_nguyen_to = [x for x in M if not is_prime(x)]
    
    print("--- Kết quả xử lý Mảng ---")
    
    # Dòng 1: Số lẻ
    print(f"1. Các số lẻ ({len(so_le)} số): {so_le}")
    
    # Dòng 2: Số chẵn
    print(f"2. Các số chẵn ({len(so_chan)} số): {so_chan}")
    
    # Dòng 3: Số nguyên tố
    print(f"3. Các số nguyên tố: {so_nguyen_to}")
    
    # Dòng 4: Số không phải là số nguyên tố
    print(f"4. Các số không phải là số nguyên tố: {so_khong_nguyen_to}")

# Ví dụ áp dụng với mảng đã cho (lưu ý: Mảng ban đầu có cả số âm, cần làm rõ yêu cầu 'số tự nhiên' 
# nếu chương trình chỉ xử lý số >= 0. Ở đây, tôi xử lý tất cả các số như trong ví dụ).
M_example = [-7, 5, 8, 3, 1, 17, 2, 90, 2, 5, 4, 8]
xu_ly_mang_so_tu_nhien(M_example)