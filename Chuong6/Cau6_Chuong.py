#Cau6
import random

def tao_list_ngau_nhien_khong_trung():
    """Tạo list N số nguyên ngẫu nhiên không trùng nhau."""
    while True:
        try:
            N = int(input("Nhập số lượng phần tử N: "))
            if N <= 0:
                print("Vui lòng nhập N là số nguyên dương.")
                continue
            # Đặt giới hạn phạm vi, ví dụ từ 1 đến 100
            # Giả sử N <= phạm vi (ví dụ: N <= 100)
            if N > 100:
                print("N quá lớn so với phạm vi giới hạn. Vui lòng nhập N <= 100.")
                continue
            
            # Tạo list N phần tử ngẫu nhiên, không trùng lặp, trong phạm vi (1, 100)
            list_ngau_nhien = random.sample(range(1, 101), N)
            
            print(f"List {N} số ngẫu nhiên không trùng nhau là:")
            print(list_ngau_nhien)
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

# tao_list_ngau_nhien_khong_trung()