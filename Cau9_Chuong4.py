#Cau9
import math

def calculate_nested_square_roots():
    """Nhập n và tính giá trị của căn bậc 2 lồng nhau S(n)."""
    print("\n--- Câu 9: Tính căn bậc 2 lồng nhau S(n) ---")
    
    try:
        # Nhập số lần lồng nhau n (phải là số nguyên dương)
        n = int(input("Nhập số lần lồng nhau n (n > 0): "))
        
        if n <= 0:
            print("Lỗi: n phải là số nguyên dương.")
            return

        # Khởi tạo giá trị ban đầu.
        # Giá trị bắt đầu là 0, vì phép tính đầu tiên là sqrt(2 + 0) nếu ta coi
        # số 2 cuối cùng là 2 + 0. Tuy nhiên, cách đơn giản hơn là
        # bắt đầu từ căn trong cùng (sqrt(2)) và thực hiện (n-1) lần lặp tiếp theo
        # hoặc gán giá trị khởi tạo là 0 và chạy đủ n lần.
        
        # Cách 1: Bắt đầu từ 0 và chạy n lần lặp
        current_sum = 0.0
        
        for i in range(n):
            # Tại mỗi bước, ta tính căn bậc hai của (2 + giá trị tổng trước đó)
            current_sum = math.sqrt(2 + current_sum)
        
        # Xuất kết quả
        print(f"\nGiá trị của S({n}) là: {current_sum:.10f}") # Làm tròn 10 chữ số thập phân
        
        # Ghi chú: Khi n tiến ra vô cùng (n -> inf), S(n) sẽ tiến về 2.

    except ValueError:
        print("Lỗi: Đầu vào n không hợp lệ. Vui lòng nhập số nguyên.")

# Chạy hàm tính căn lồng nhau
# calculate_nested_square_roots()