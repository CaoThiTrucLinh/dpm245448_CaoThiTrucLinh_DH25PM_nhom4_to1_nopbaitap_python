#Cau12
def oscillate(start, end):
    """
    Hàm generator tạo ra chuỗi giá trị dao động: -3, -2, -1, 0, 1, -2, -3, -4.
    """
    
    # 1. Phần tăng: -3, -2, -1, 0, 1
    current_value = start 
    while current_value <= 1:
        yield current_value
        current_value += 1
        
    # 2. Phần giảm theo yêu cầu đặc biệt: -2, -3, -4
    yield -2
    yield -3
    yield -4
    
# Thử nghiệm hàm:
print("\n--- Câu 12: Thử nghiệm hàm oscillate ---")
result = []
for n in oscillate(-3, 5):
    result.append(str(n))
    
print(" ".join(result))
# Output: -3 -2 -1 0 1 -2 -3 -4