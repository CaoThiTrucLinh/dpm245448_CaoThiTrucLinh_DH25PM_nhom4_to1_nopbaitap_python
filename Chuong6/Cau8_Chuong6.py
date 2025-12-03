#Cau8
def nhap_sap_xep_day_so():
    """Nhập dãy N số thực, sắp xếp tăng dần và xuất ra."""
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
            
    # Nhập N phần tử
    for i in range(N):
        while True:
            try:
                so = float(input(f"Nhập phần tử M[{i}]: "))
                day_so.append(so)
                break
            except ValueError:
                print("Đầu vào không hợp lệ. Vui lòng nhập số thực.")

    # Sắp xếp dãy số (mặc định là tăng dần)
    day_so.sort() 
    
    print("\nDãy số sau khi sắp xếp (tăng dần) là:")
    print(day_so)

# nhap_sap_xep_day_so()