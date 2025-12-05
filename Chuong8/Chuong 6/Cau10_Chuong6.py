#Cau10
import numpy as np

## Câu 10: Xử lý Ma Trận
def matrix_operations():
    """Nhập 2 ma trận A, B và thực hiện các phép toán."""
    
    def get_matrix(name):
        """Hàm helper để nhập ma trận."""
        while True:
            try:
                rows = int(input(f"Nhập số hàng của ma trận {name}: "))
                cols = int(input(f"Nhập số cột của ma trận {name}: "))
                print(f"Nhập các phần tử của ma trận {name} (cách nhau bằng dấu cách cho mỗi hàng, Enter để xuống hàng):")
                
                elements = []
                for i in range(rows):
                    row_input = input(f"Hàng {i+1}: ").split()
                    if len(row_input) != cols:
                        raise ValueError("Số lượng phần tử không khớp với số cột.")
                    elements.append([float(x) for x in row_input])
                
                return np.array(elements)
            except ValueError as e:
                print(f"Lỗi nhập liệu: {e}. Vui lòng nhập lại ma trận {name}.")

    # 1. Nhập 2 ma trận A, B
    print("\n[Câu 10] --- Nhập Ma Trận A ---")
    A = get_matrix("A")
    print("\n[Câu 10] --- Nhập Ma Trận B ---")
    B = get_matrix("B")
    
    print("\nMa trận A:\n", A)
    print("Ma trận B:\n", B)

    # 2. Cộng 2 matrix
    if A.shape == B.shape:
        C = A + B
        print("\nTổng A + B:\n", C)
    else:
        print("\nKhông thể cộng A và B vì kích thước không khớp.")

    # 3. Viết hàm tìm matrix hoán vị (Transpose) áp dụng để tìm cho A, B
    # Trong NumPy, dùng thuộc tính .T hoặc hàm np.transpose()
    
    def transpose_matrix(M):
        """Tìm ma trận hoán vị (chuyển vị) của ma trận M."""
        return M.T
        
    A_T = transpose_matrix(A)
    B_T = transpose_matrix(B)
    
    print("\nMa trận hoán vị (chuyển vị) của A (A^T):\n", A_T)
    print("Ma trận hoán vị (chuyển vị) của B (B^T):\n", B_T)

# Chạy câu 10
# matrix_operations()