#Cau3
import math

def giai_phuong_trinh_bac_hai(a, b, c):
    """
    Giải phương trình bậc hai: ax^2 + bx + c = 0
    """
    print(f"\nGiải phương trình: {a}x^2 + {b}x + {c} = 0")

    # 1. Trường hợp a = 0
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình có vô số nghiệm (0 = 0).")
            else:
                print("Phương trình vô nghiệm.") # c != 0
        else:
            # Phương trình bậc nhất: bx + c = 0
            x = -c / b
            print(f"Đây là phương trình bậc nhất. Nghiệm duy nhất: x = {-c}/{b} ≈ {x}")
        return

    # 2. Trường hợp a != 0 (Phương trình bậc hai thực sự)

    # Tính Delta (Δ)
    delta = b**2 - 4*a*c
    print(f"Delta (Δ) = b^2 - 4ac = ({b})^2 - 4*({a})*({c}) = {delta}")

    if delta < 0:
        # Trường hợp Δ < 0
        print("Phương trình vô nghiệm thực (có hai nghiệm phức).")
    elif delta == 0:
        # Trường hợp Δ = 0
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x1 = x2 = -b/(2a) = {-b}/({2*a}) ≈ {x}")
    else:
        # Trường hợp Δ > 0
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt:")
        print(f"  x1 = (-b + √Δ) / (2a) ≈ {x1}")
        print(f"  x2 = (-b - √Δ) / (2a) ≈ {x2}")

# --- Ví dụ minh họa ---

## 🛠️ Hàm nhập dữ liệu
def nhap_he_so():
    print("Vui lòng nhập các hệ số a, b, c:")
    try:
        a = float(input("Nhập hệ số a: "))
        b = float(input("Nhập hệ số b: "))
        c = float(input("Nhập hệ số c: "))
        return a, b, c
    except ValueError:
        print("Lỗi: Đầu vào không hợp lệ. Vui lòng nhập số.")
        return None, None, None

## 🚀 Thực thi chương trình
if __name__ == "__main__":
    a, b, c = nhap_he_so()
    if a is not None:
        giai_phuong_trinh_bac_hai(a, b, c)

    # Thêm một vài ví dụ cố định để dễ kiểm tra:
    print("\n--- Kiểm tra nhanh các trường hợp đặc biệt ---")
    giai_phuong_trinh_bac_hai(1, -3, 2) # Δ > 0, x1=2, x2=1
    giai_phuong_trinh_bac_hai(1, 2, 1)  # Δ = 0, x1=x2=-1
    giai_phuong_trinh_bac_hai(1, 1, 1)  # Δ < 0, vô nghiệm
    giai_phuong_trinh_bac_hai(0, 2, 4)  # a = 0, bậc nhất, x = -2
    giai_phuong_trinh_bac_hai(0, 0, 5)  # a = 0