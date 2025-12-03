#Cau13
def sum_of_proper_divisors(n):
    """
    Tính tổng các ước số của số nguyên dương n, không kể chính n.
    Ví dụ: n=6 có các ước (1, 2, 3, 6). Tổng các ước không kể 6 là 1+2+3 = 6.
    """
    if n <= 0:
        return 0
    
    # Ước số nhỏ nhất luôn là 1. Khởi tạo tổng bằng 1.
    total_sum = 1 
    
    # Ước số chỉ cần kiểm tra đến căn bậc hai của n (bao gồm căn bậc hai)
    # vì nếu i là ước số, thì n/i cũng là ước số.
    limit = int(n**0.5)
    
    for i in range(2, limit + 1):
        if n % i == 0:
            # i là một ước số
            total_sum += i
            
            # n // i là ước số còn lại (trừ trường hợp n là số chính phương)
            divisor2 = n // i
            
            # Nếu divisor2 khác i (tránh đếm ước số hai lần), thì cộng thêm divisor2
            if divisor2 != i:
                total_sum += divisor2
                
    return total_sum