#Cau7
def nhap_day_so_tang_dan():
    """Nhập một dãy số, đảm bảo số sau lớn hơn hoặc bằng số trước."""
    day_so = []
    
    # Nhập số lượng phần tử N
    while True:
        try:
            N = int(input("Nhập số lượng phần tử N: "))
            if N > 0:
                break
            print("N phải là số nguyên dương.")
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

    # Nhập phần tử đầu tiên
    if N > 0:
        while True:
            try:
                so_moi = float(input(f"Nhập phần tử thứ 1: "))
                day_so.append(so_moi)
                break
            except ValueError:
                print("Đầu vào không hợp lệ. Vui lòng nhập số (nguyên hoặc thực).")

    # Nhập các phần tử còn lại, kiểm tra điều kiện tăng dần
    for i in range(1, N):
        while True:
            try:
                so_moi = float(input(f"Nhập phần tử thứ {i+1} (phải >= {day_so[-1]}): "))
                if so_moi >= day_so[-1]:
                    day_so.append(so_moi)
                    break
                else:
                    print(f"Lỗi: Số mới phải lớn hơn hoặc bằng số trước đó ({day_so[-1]}). Vui lòng nhập lại.")
            except ValueError:
                print("Đầu vào không hợp lệ. Vui lòng nhập số (nguyên hoặc thực).")
    
    print("\nDãy số đã nhập theo thứ tự tăng dần là:")
    print(day_so)

# nhap_day_so_tang_dan()