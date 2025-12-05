#Cau9
## Câu 9: Xử lý mảng (Phân loại số)
def is_prime(n):
    """Kiểm tra một số có phải là số nguyên tố không."""
    if n < 2:
        return False
    # Chỉ cần kiểm tra đến căn bậc hai của n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def analyze_list(M):
    """Phân tích list M theo các yêu cầu."""
    print(f"\n[Câu 9] List đầu vào M: {M}")
    
    # Khởi tạo các biến
    odd_numbers = []
    even_numbers = []
    prime_numbers = []
    non_prime_numbers = []
    
    for num in M:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
        
        if is_prime(num):
            prime_numbers.append(num)
        elif num > 0 and num == int(num): # Chỉ xét số nguyên dương khi kiểm tra không phải số nguyên tố
             # Nếu không phải là số nguyên tố VÀ là số nguyên dương
            non_prime_numbers.append(num)

    # --- Kết quả ---
    
    # Dòng 1: gồm các số lẻ, tổng cộng có bao nhiêu số lẻ.
    sum_odd = sum(odd_numbers)
    print(f"  - Dòng 1 (Số lẻ): {odd_numbers}. Tổng các số lẻ: {sum_odd}. Số lượng: {len(odd_numbers)}")

    # Dòng 2: gồm các số chẵn, tổng cộng có bao nhiêu số chẵn.
    sum_even = sum(even_numbers)
    print(f"  - Dòng 2 (Số chẵn): {even_numbers}. Tổng các số chẵn: {sum_even}. Số lượng: {len(even_numbers)}")
    
    # Dòng 3: gồm các số nguyên tố.
    print(f"  - Dòng 3 (Số nguyên tố): {prime_numbers}")
    
    # Dòng 4: gồm các số không phải là số nguyên tố (chỉ lấy các số nguyên dương không phải SNT trong list)
    print(f"  - Dòng 4 (Không phải SNT): {non_prime_numbers}")

# Chạy câu 9 với dữ liệu mẫu: M = [-3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 8]
M_test = [-3, 6, 7, 8, 11, 17, 2, 90, 2, 5, 4, 8]
analyze_list(M_test)