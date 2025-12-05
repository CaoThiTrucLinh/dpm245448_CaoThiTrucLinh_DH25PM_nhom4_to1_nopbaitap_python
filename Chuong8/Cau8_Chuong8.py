#Cau8
import tkinter as tk
from tkinter import messagebox

def fahrenheit_to_celsius():
    """Chuyển đổi nhiệt độ từ F sang C."""
    try:
        f_temp = float(entry_f.get())
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập nhiệt độ F là một số.")
        return

    # Công thức chuyển đổi: C = (F - 32) * 5/9
    c_temp = (f_temp - 32) * 5/9
    
    # Cập nhật kết quả
    entry_c.delete(0, tk.END)
    entry_c.insert(0, f"{c_temp:.2f}") # Hiển thị 2 chữ số thập phân

# --- Thiết lập cửa sổ chính ---
window = tk.Tk()
window.title("Chuyển Độ F sang Độ C")
window.geometry("350x150")
window.resizable(False, False)

# --- Khung nhập liệu F ---
tk.Label(window, text="Nhập độ F:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=10, sticky='w')
entry_f = tk.Entry(window, width=15)
entry_f.grid(row=0, column=1, padx=5, pady=10)
tk.Label(window, text="Độ F", font=("Arial", 10)).grid(row=0, column=2, padx=5, pady=10, sticky='w')
entry_f.insert(0, "300") # Giá trị mặc định

# --- Nút Chuyển Đổi ---
tk.Button(window, text="Độ C -> Độ F", command=fahrenheit_to_celsius, width=15).grid(row=1, column=1, pady=10)

# --- Khung kết quả C ---
tk.Label(window, text="Độ C:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=10, sticky='w')
entry_c = tk.Entry(window, width=15, state='readonly') # Kết quả là readonly
entry_c.grid(row=2, column=1, padx=5, pady=10)
tk.Label(window, text="Độ C", font=("Arial", 10)).grid(row=2, column=2, padx=5, pady=10, sticky='w')

window.mainloop()