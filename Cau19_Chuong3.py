#Cau19
def rewrite_loop_with_break(m=100):
    print("--- Câu 17: Vòng lặp sử dụng 'break' ---")
    n = 0
    
    # 1. Thay thế 'while not done and n != m' bằng 'while True' (vòng lặp vô hạn)
    while True:
        try:
            # Nhập giá trị n
            user_input = input("Nhập một số nguyên (nhập số âm để thoát): ")
            n = int(user_input)
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")
            continue # Quay lại đầu vòng lặp

        # 2. Điều kiện dừng 1: Thay thế 'if n < 0: done = True' bằng 'if n < 0: break'
        if n < 0:
            print("Đã nhập số âm. Thoát vòng lặp (break).")
            break

        # 3. Điều kiện dừng 2: Thêm kiểm tra n == m (tương đương với n != m bị sai)
        # Nếu đã đạt mục tiêu m thì dừng (tùy vào ý định của đề bài)
        if n == m:
            print(f"n đã đạt {m}. Thoát vòng lặp.")
            break
            
        print("n =", n)
        
    print("Vòng lặp đã kết thúc.")

# Gọi hàm để chạy thử
# rewrite_loop_with_break()