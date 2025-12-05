#Cau7
## Câu 7: Viết chương trình nhập vào một dãy các số theo thứ tự tăng dần
def input_sorted_list():
    """Nhập dãy số cho đến khi nó là dãy tăng dần."""
    while True:
        user_input = input("\n[Câu 7] Nhập một dãy các số (cách nhau bằng dấu phẩy) theo thứ tự TĂNG DẦN: ")
        
        try:
            # Chuyển chuỗi nhập vào thành list các số nguyên
            # Xóa khoảng trắng và chia chuỗi
            num_list = [int(x.strip()) for x in user_input.split(',')]
            
            is_sorted = True
            # Kiểm tra xem list có tăng dần không (a[i] <= a[i+1])
            for i in range(len(num_list) - 1):
                if num_list[i] > num_list[i+1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                print(f"[Câu 7] Dãy số đã nhập hợp lệ: {num_list}")
                return num_list
            else:
                print("Dãy số nhập vào KHÔNG theo thứ tự tăng dần. Vui lòng nhập lại.")
                
        except ValueError:
            print("Nhập sai định dạng. Vui lòng nhập các số nguyên cách nhau bằng dấu phẩy.")

# Chạy câu 7
# sorted_list = input_sorted_list()