#Cau2
import tkinter as tk
from tkinter import messagebox
import math

def giai_phuong_trinh_bac_2():
    """Hàm xử lý việc giải phương trình bậc hai khi nhấn nút 'Giải'."""
    try:
        # Lấy các hệ số từ các ô nhập liệu
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
    except ValueError:
        # Xử lý trường hợp người dùng nhập không phải là số
        messagebox.showerror("Lỗi Nhập Liệu", "Vui lòng nhập các hệ số a, b, c là các số hợp lệ.")
        return

    ket_qua = ""

    # 1. Trường hợp a = 0 (Trở thành phương trình bậc nhất: bx + c = 0)
    if a == 0:
        if b == 0:
            if c == 0:
                ket_qua = "Phương trình vô số nghiệm (0 = 0)."
            else:
                ket_qua = "Phương trình vô nghiệm (c ≠ 0)."
        else:
            # Phương trình bậc nhất: x = -c/b
            x = -c / b
            ket_qua = f"a = 0. Phương trình là bậc nhất: x = {-c}/{b} = {x:.4f}"
            
    # 2. Trường hợp a ≠ 0 (Phương trình bậc hai)
    else:
        # Tính Delta (Δ)
        delta = b**2 - 4*a*c
        
        # Biểu diễn LaTeX cho công thức Delta: $\Delta = b^2 - 4ac$
        # 
        if delta < 0:
            ket_qua = f"Δ = {delta:.4f}. Phương trình vô nghiệm thực."
        elif delta == 0:
            # Nghiệm kép: x1 = x2 = -b / (2a)
            x = -b / (2 * a)
            ket_qua = f"Δ = 0. Phương trình có nghiệm kép: x1 = x2 = {-b}/({2*a}) = {x:.4f}"
        else:
            # Hai nghiệm phân biệt: x1 = (-b - sqrt(Delta)) / (2a), x2 = (-b + sqrt(Delta)) / (2a)
            x1 = (-b - math.sqrt(delta)) / (2 * a)
            x2 = (-b + math.sqrt(delta)) / (2 * a)
            
            # Biểu diễn LaTeX cho công thức nghiệm: $x = \frac{-b \pm \sqrt{\Delta}}{2a}$
            #             
            # Giống định dạng trong hình ảnh (x1=...px2=...)
            ket_qua = f"Δ = {delta:.4f}. Kết quả: x1={x1:.4f} px2={x2:.4f}"

    # Cập nhật kết quả lên nhãn hiển thị
    label_ket_qua.config(text="Kết quả: " + ket_qua)

def tiep_tuc():
    """Hàm xóa nội dung các ô nhập liệu và kết quả để giải phương trình mới."""
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_c.delete(0, tk.END)
    label_ket_qua.config(text="Kết quả:")
    entry_a.focus() # Đặt con trỏ về ô nhập a

# --- Thiết lập cửa sổ chính ---
window = tk.Tk()
window.title("PTB1 - Phương Trình Bậc 2")
window.geometry("350x300")
window.resizable(False, False) # Không cho phép thay đổi kích thước

# Tiêu đề lớn
label_title = tk.Label(window, text="Phương Trình Bậc 2", fg="blue", font=("Arial", 16, "bold"))
label_title.pack(pady=10)

# --- Các ô nhập liệu (Widgets) ---

# Khung cho Hệ số a
frame_a = tk.Frame(window)
frame_a.pack(pady=5, padx=20, fill='x')
label_a = tk.Label(frame_a, text="Hệ số a:", width=10, anchor='w')
label_a.pack(side=tk.LEFT)
entry_a = tk.Entry(frame_a, width=20)
entry_a.pack(side=tk.RIGHT, fill='x', expand=True)
entry_a.insert(0, "4") # Giá trị mặc định như trong hình

# Khung cho Hệ số b
frame_b = tk.Frame(window)
frame_b.pack(pady=5, padx=20, fill='x')
label_b = tk.Label(frame_b, text="Hệ số b:", width=10, anchor='w')
label_b.pack(side=tk.LEFT)
entry_b = tk.Entry(frame_b, width=20)
entry_b.pack(side=tk.RIGHT, fill='x', expand=True)
entry_b.insert(0, "2") # Giá trị mặc định như trong hình

# Khung cho Hệ số c
frame_c = tk.Frame(window)
frame_c.pack(pady=5, padx=20, fill='x')
label_c = tk.Label(frame_c, text="Hệ số c:", width=10, anchor='w')
label_c.pack(side=tk.LEFT)
entry_c = tk.Entry(frame_c, width=20)
entry_c.pack(side=tk.RIGHT, fill='x', expand=True)
entry_c.insert(0, "-6") # Giá trị mặc định như trong hình

# --- Các nút chức năng ---
frame_buttons = tk.Frame(window)
frame_buttons.pack(pady=15)

# Nút Giải
button_giai = tk.Button(frame_buttons, text="Giải", command=giai_phuong_trinh_bac_2, width=8)
button_giai.pack(side=tk.LEFT, padx=10)

# Nút Tiếp
button_tiep = tk.Button(frame_buttons, text="Tiếp", command=tiep_tuc, width=8)
button_tiep.pack(side=tk.LEFT, padx=10)

# Nút Thoát
button_thoat = tk.Button(frame_buttons, text="Thoát", command=window.quit, width=8)
button_thoat.pack(side=tk.LEFT, padx=10)

# --- Hiển thị kết quả ---
label_ket_qua = tk.Label(window, text="Kết quả:", fg="black", font=("Arial", 10))
label_ket_qua.pack(pady=10)

# Chạy vòng lặp sự kiện chính của Tkinter
window.mainloop()