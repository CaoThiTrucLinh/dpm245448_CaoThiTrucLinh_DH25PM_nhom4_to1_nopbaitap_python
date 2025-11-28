#Cau9
def find_quarter(month):
    """Xác định tháng (1-12) thuộc quý nào trong năm."""
    
    if not (1 <= month <= 12):
        return "Tháng nhập vào không hợp lệ (phải từ 1 đến 12)."
        
    # Tính quý dựa trên công thức: (tháng - 1) // 3 + 1
    quarter = (month - 1) // 3 + 1
    
    return quarter

# Ví dụ kiểm tra
print("\n--- Câu 9: Xác định Quý trong năm ---")
month_a = 2
month_b = 6
month_c = 11
print(f"Tháng {month_a} thuộc Quý {find_quarter(month_a)}")
print(f"Tháng {month_b} thuộc Quý {find_quarter(month_b)}")
print(f"Tháng {month_c} thuộc Quý {find_quarter(month_c)}")