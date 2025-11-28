#Cau14
# --- Code theo chính xác hình ảnh cung cấp ---
a = 0
while a < 100:
    b = 0
    while b < 40:
        if (a + b) % 2 == 0:
            # print('*', end='')
            # Để đếm, ta sử dụng một biến đếm thay vì in ra màn hình
            # Nếu muốn in ra màn hình, bỏ dấu # ở dòng trên
            pass 
        b += 1
    
    # print() # Lệnh xuống dòng sau khi vòng lặp b kết thúc (chỉ chạy 1 lần)
    a += 1

# --- Code giả định đúng ý đồ (b = 0 được đặt lại bên trong vòng lặp a) ---
def count_stars_correct_logic():
    count = 0
    a = 0
    while a < 100:
        b = 0 # Đúng vị trí
        while b < 40:
            if (a + b) % 2 == 0:
                count += 1
            b += 1
        a += 1
    return count

# --- Code mô phỏng chính xác lỗi trong hình (chỉ đếm * cho lần lặp a=0) ---
def count_stars_image_logic():
    count = 0
    a = 0
    b = 0
    
    # Vòng lặp ngoài (a chạy từ 0 đến 99)
    while a < 100:
        # Vòng lặp trong (b chỉ chạy 1 lần khi a=0)
        while b < 40:
            if (a + b) % 2 == 0:
                count += 1
            b += 1
            
        a += 1 # a tăng, nhưng b đã là 40, nên vòng lặp b không chạy nữa
        
    return count

print("--- Câu 14: Số lượng dấu '*' ---")
print(f"Số lượng dấu '*' theo LOGIC CỦA CODE TRONG HÌNH: {count_stars_image_logic()}")
print(f"Số lượng dấu '*' nếu b được RESET VỀ 0: {count_stars_correct_logic()}")