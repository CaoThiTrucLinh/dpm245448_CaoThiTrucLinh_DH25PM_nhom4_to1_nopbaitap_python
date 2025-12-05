#Cau9
import tkinter as tk
from tkinter import messagebox

# Bảng phân loại BMI (theo tiêu chuẩn quốc tế)
BMI_CATEGORIES = [
    (18.5, "Gầy"),
    (24.9, "Bình thường"),
    (29.9, "Thừa cân"),
    (float('inf'), "Béo phì") # Mọi giá trị lớn hơn 30
]

def calculate_bmi():
    """Tính toán và hiển thị BMI cùng với tình trạng cơ thể."""
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập Chiều cao và Cân nặng là các số hợp lệ.")
        return

    if height <= 0 or weight <= 0:
        messagebox.showerror("Lỗi", "Chiều cao và Cân nặng phải lớn hơn 0.")
        return

    # Chiều cao phải chuyển từ cm (như ví dụ 1.72) sang mét
    # Giả sử người dùng nhập mét (ví dụ 1.72m) theo yêu cầu công thức
    # Nếu người dùng nhập cm, phải chia 100. Ở đây giả định nhập mét.
    
    # Tính BMI
    bmi = weight / (height ** 2)
    
    # Phân loại tình trạng cơ thể
    status = "Phân loại không xác định"
    for threshold, category in BMI_CATEGORIES:
        if bmi < threshold:
            status = category
            break

    # Cập nhật kết quả
    entry_bmi.delete(0, tk.END)
    entry_bmi.insert(0, f"{bmi:.2f}")

    entry_status.delete(0, tk.END)
    entry_status.insert(0, status)

# --- Thiết lập cửa sổ chính ---
window = tk.Tk()
window.title("Phần Mềm Tính BMI")
window.geometry("350x250")
window.resizable(False, False)

# --- Khung nhập liệu ---
tk.Label(window, text="Nhập chiều cao (m):", width=20, anchor='w').grid(row=0, column=0, padx=5, pady=5)
entry_height = tk.Entry(window, width=15)
entry_height.grid(row=0, column=1, padx=5, pady=5)
entry_height.insert(0, "1.72") 

tk.Label(window, text="Nhập cân nặng (kg):", width=20, anchor='w').grid(row=1, column=0, padx=5, pady=5)
entry_weight = tk.Entry(window, width=15)
entry_weight.grid(row=1, column=1, padx=5, pady=5)
entry_weight.insert(0, "65") 

# --- Nút Tính BMI ---
tk.Button(window, text="Tính BMI", command=calculate_bmi, width=10).grid(row=2, column=1, pady=10)

# --- Khung kết quả ---
tk.Label(window, text="BMI của bạn:", width=20, anchor='w').grid(row=3, column=0, padx=5, pady=5)
entry_bmi = tk.Entry(window, width=15, state='readonly')
entry_bmi.grid(row=3, column=1, padx=5, pady=5)

tk.Label(window, text="Tình trạng của bạn:", width=20, anchor='w').grid(row=4, column=0, padx=5, pady=5)
entry_status = tk.Entry(window, width=15, state='readonly')
entry_status.grid(row=4, column=1, padx=5, pady=5)

# --- Nút Thoát ---
tk.Button(window, text="Thoát", command=window.quit, width=10).grid(row=5, column=1, pady=10)

window.mainloop()