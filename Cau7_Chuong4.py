#Cau7
import math

def calculate_distance_ab():
    """Nhập tọa độ 2 điểm A và B, sau đó tính và in ra độ dài đoạn AB."""
    print("\n--- Câu 7: Tính độ dài đoạn AB ---")
    
    # Nhập tọa độ điểm A
    try:
        x_A = float(input("Nhập tọa độ x của điểm A (xA): "))
        y_A = float(input("Nhập tọa độ y của điểm A (yA): "))
        
        # Nhập tọa độ điểm B
        x_B = float(input("Nhập tọa độ x của điểm B (xB): "))
        y_B = float(input("Nhập tọa độ y của điểm B (yB): "))
        
        # Tính bình phương các hiệu
        delta_x_squared = (x_B - x_A)**2
        delta_y_squared = (y_B - y_A)**2
        
        # Tính độ dài đoạn AB (sử dụng math.sqrt hoặc phép lũy thừa 0.5)
        distance_ab = math.sqrt(delta_x_squared + delta_y_squared)
        
        # Xuất kết quả
        print(f"\nTọa độ A: ({x_A}, {y_A})")
        print(f"Tọa độ B: ({x_B}, {y_B})")
        print(f"Độ dài đoạn AB là: {distance_ab:.4f}") # Làm tròn 4 chữ số thập phân
        
    except ValueError:
        print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số thực.")

# Chạy hàm tính khoảng cách
# calculate_distance_ab()