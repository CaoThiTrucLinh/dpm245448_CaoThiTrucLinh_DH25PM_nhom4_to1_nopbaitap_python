#Cau16
def count_stars_q16():
    # 1. Khởi tạo biến đếm
    star_count = 0
    
    # 2. Vòng lặp theo yêu cầu: range(start=20, stop=100, step=5)
    print("--- Câu 16: Mô phỏng vòng lặp ---")
    print("Các giá trị của 'a' trong vòng lặp:")
    
    # Chúng ta dùng một danh sách để lưu các giá trị a
    values_of_a = []
    
    for a in range(20, 100, 5):
        # Lệnh in dấu '*'
        # print('*', end='')
        
        # Tăng biến đếm lên 1 cho mỗi lần lặp
        star_count += 1
        values_of_a.append(a)
        
    # print() # Lệnh xuống dòng
    
    print(values_of_a)
    print("-" * 35)
    
    # 3. Kết quả
    print(f"Số lần lặp (số dấu '*' được in) là: {star_count}")
    
    # Xác nhận bằng cách in độ dài của dãy range
    # print(f"Xác nhận bằng len(range(20, 100, 5)): {len(range(20, 100, 5))}")

count_stars_q16()