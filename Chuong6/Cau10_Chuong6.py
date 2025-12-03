#Cau10
def nhap_ma_tran():
    """Hàm nhập ma trận từ người dùng."""
    while True:
        try:
            R = int(input("Nhập số hàng (rows): "))
            C = int(input("Nhập số cột (columns): "))
            if R <= 0 or C <= 0:
                print("Số hàng và số cột phải là số nguyên dương.")
                continue
            break
        except ValueError:
            print("Đầu vào không hợp lệ. Vui lòng nhập số nguyên.")

    matrix = []
    print(f"Nhập các phần tử cho ma trận {R}x{C}:")
    for i in range(R):
        row = []
        for j in range(C):
            while True:
                try:
                    val = float(input(f"Nhập phần tử [{i}][{j}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Vui lòng nhập số (nguyên hoặc thực).")
        matrix.append(row)
    return matrix, R, C

def in_ma_tran(matrix):
    """Hàm in ma trận ra màn hình."""
    for row in matrix:
        print(row)