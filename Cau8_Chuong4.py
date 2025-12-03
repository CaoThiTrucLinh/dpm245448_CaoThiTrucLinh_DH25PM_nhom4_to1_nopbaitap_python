#Cau8
import math

def calculate_log_base_a():
    """Nhập cơ số 'a' và giá trị 'x', sau đó tính và in ra log_a(x)."""
    print("\n--- Câu 8: Tính log_a(x) ---")
    
    try:
        # Nhập x và a
        x = float(input("Nhập giá trị x (x > 0): "))
        a = float(input("Nhập cơ số a (a > 0 và a != 1): "))
        
        # Kiểm tra điều kiện (x > 0, a > 0, a != 1)
        if x <= 0:
            print("Lỗi: x phải lớn hơn 0.")
            return
        
        if a <= 0 or a == 1:
            print("Lỗi: a phải lớn hơn 0 và khác 1.")
            return

        # Tính log_a(x) bằng công thức đổi cơ số: log_a(x) = ln(x) / ln(a)
        # math.log(x) trong Python là ln(x)
        log_a_x = math.log(x) / math.log(a)
        
        # Xuất kết quả
        print(f"\nlog({x}) cơ số {a} là: {log_a_x:.6f}") # Làm tròn 6 chữ số thập phân
        
        # Ghi chú: Python cũng có hàm tính logarit với cơ số bất kỳ: math.log(x, a)
        # log_a_x_check = math.log(x, a)
        # print(f"(Kiểm tra bằng hàm tích hợp sẵn: {log_a_x_check:.6f})")

    except ValueError:
        print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số thực.")

# Chạy hàm tính logarit
# calculate_log_base_a()