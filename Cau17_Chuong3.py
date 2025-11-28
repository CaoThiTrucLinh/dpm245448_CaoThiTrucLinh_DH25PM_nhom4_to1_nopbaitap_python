#Cau17
def rewrite_loop_with_break():
    print("--- Câu 17: Viết lại vòng lặp với 'break' ---")
    n, m = 0, 100  # Khởi tạo n và m như trong đề
    
    # Sử dụng while True để tạo vòng lặp vô hạn
    while True:
        try:
            # Nhập giá trị n
            n = int(input("Nhập một số nguyên (nhập số âm để thoát, hoặc 100 để dừng nếu n = m ban đầu): "))
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
            continue # Bỏ qua lần lặp này và tiếp tục vòng lặp

        # Điều kiện dừng 1: n < 0 (thay thế done = True)
        if n < 0:
            print("Bạn đã nhập số âm. Thoát vòng lặp.")
            break # Thoát khỏi vòng lặp while

        # Điều kiện dừng 2: n == m (thay thế n != m)
        # Lưu ý: Trong code gốc, n và m được khởi tạo nhưng n thay đổi ngay lập tức.
        # Nếu n == m là điều kiện dừng, ta cần kiểm tra sau khi n được nhập.
        # Giả sử m là một hằng số mục tiêu.
        if n == m:
            print(f"n đã đạt giá trị {m}. Thoát vòng lặp.")
            break # Thoát khỏi vòng lặp while
            
        print("n =", n) # In n sau khi kiểm tra điều kiện thoát
        
    print("Vòng lặp đã kết thúc.")

# Chạy hàm để kiểm tra
# rewrite_loop_with_break()