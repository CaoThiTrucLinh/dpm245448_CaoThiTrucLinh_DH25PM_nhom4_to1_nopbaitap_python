#Cau7
import tkinter as tk
from tkinter import messagebox

# Mảng Can và Chi
CAN = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
CHI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
TUOI = ["Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi", "Thân", "Dậu", "Tuất", "Hợi"]
# Hoặc: TUOI = ["Chuột", "Trâu", "Hổ", "Mèo", "Rồng", "Rắn", "Ngựa", "Dê", "Khỉ", "Gà", "Chó", "Heo"]

def convert_solar_to_lunar():
    """Chuyển năm dương lịch thành năm âm lịch (Can Chi)."""
    try:
        year = int(entry_year.get())
        if year <= 0:
             messagebox.showerror("Lỗi", "Năm dương lịch phải là số nguyên dương.")
             return
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập năm dương lịch là số nguyên.")
        return

    # Tính Can (Can = Năm % 10. Do năm 0 là Canh (CAN[0]), ta dùng (year + 6) % 10)
    can_index = (year + 6) % 10
    can = CAN[can_index]
    
    # Tính Chi (Chi = Năm % 12. Do năm 0 là Thân (CHI[8]), ta dùng (year + 8) % 12)
    chi_index = (year + 8) % 12
    chi = CHI[chi_index]
    
    # Năm Tuổi (Giống Chi)
    tuoi = TUOI[chi_index]

    lunar_year = f"{can} {chi}"
    
    # Cập nhật kết quả lên các Entry
    entry_lunar_year.delete(0, tk.END)
    entry_lunar_year.insert(0, lunar_year)
    
    entry_tuoi.delete(0, tk.END)
    entry_tuoi.insert(0, tuoi)

# --- Thiết lập cửa sổ chính ---
window = tk.Tk()
window.title("Chuyển Dương Lịch sang Âm Lịch")
window.geometry("300x200")
window.resizable(False, False)

# --- Khung nhập liệu (Input) ---
tk.Label(window, text="Nhập năm dương lịch:", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=10, sticky='w')
entry_year = tk.Entry(window, width=15)
entry_year.grid(row=0, column=1, padx=5, pady=10)
entry_year.insert(0, "1982") # Giá trị mặc định

# --- Nút Chuyển Đổi ---
tk.Button(window, text="Chuyển", command=convert_solar_to_lunar, width=10).grid(row=1, column=0, columnspan=2, pady=10)

# --- Khung kết quả (Output) ---
tk.Label(window, text="Năm âm:", font=("Arial", 10)).grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_lunar_year = tk.Entry(window, width=15, state='readonly') # Kết quả là readonly
entry_lunar_year.grid(row=2, column=1, padx=5, pady=5)

tk.Label(window, text="Năm Tuổi:", font=("Arial", 10)).grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_tuoi = tk.Entry(window, width=15, state='readonly') # Kết quả là readonly
entry_tuoi.grid(row=3, column=1, padx=5, pady=5)

window.mainloop()