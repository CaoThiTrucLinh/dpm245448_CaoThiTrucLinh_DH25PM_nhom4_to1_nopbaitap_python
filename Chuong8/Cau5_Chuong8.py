#Cau5
import tkinter as tk
from tkinter import messagebox

# Mật khẩu gốc để kiểm tra (mô phỏng)
CURRENT_PASSWORD = "123"

def process_change_password():
    """
    Hàm xử lý logic khi nhấn nút OK để đổi mật khẩu.
    """
    old_pass = entry_old_pass.get()
    new_pass = entry_new_pass.get()
    confirm_pass = entry_confirm_pass.get()

    if old_pass != CURRENT_PASSWORD:
        messagebox.showerror("Lỗi", "Mật khẩu cũ không đúng.")
    elif new_pass == "":
        messagebox.showerror("Lỗi", "Mật khẩu mới không được để trống.")
    elif new_pass != confirm_pass:
        messagebox.showerror("Lỗi", "Xác nhận mật khẩu mới không khớp.")
    else:
        # Giả lập việc đổi mật khẩu thành công
        global CURRENT_PASSWORD
        CURRENT_PASSWORD = new_pass
        messagebox.showinfo("Thành Công", "Mật khẩu đã được đổi thành công!")
        window.destroy() # Đóng cửa sổ sau khi đổi thành công

def cancel_operation():
    """
    Hàm xử lý khi nhấn nút Cancel.
    """
    window.destroy()

# --- Thiết lập cửa sổ chính ---
window = tk.Tk()
window.title("Enter New Password")
window.geometry("300x180")
window.resizable(False, False)

# --- Tiêu đề và Khung nhập liệu ---

label_title = tk.Label(window, text="Enter New Password", font=("Arial", 12, "bold"))
label_title.grid(row=0, column=0, columnspan=2, pady=10)

# Khung cho Old Password
tk.Label(window, text="Old Password:", anchor='w').grid(row=1, column=0, padx=5, pady=5, sticky='w')
entry_old_pass = tk.Entry(window, show="*", width=20)
entry_old_pass.grid(row=1, column=1, padx=5, pady=5)

# Khung cho New Password
tk.Label(window, text="New Password:", anchor='w').grid(row=2, column=0, padx=5, pady=5, sticky='w')
entry_new_pass = tk.Entry(window, show="*", width=20)
entry_new_pass.grid(row=2, column=1, padx=5, pady=5)

# Khung cho Enter New Password Again
tk.Label(window, text="Enter New Password Again:", anchor='w').grid(row=3, column=0, padx=5, pady=5, sticky='w')
entry_confirm_pass = tk.Entry(window, show="*", width=20)
entry_confirm_pass.grid(row=3, column=1, padx=5, pady=5)

# --- Khung nút bấm ---
frame_buttons = tk.Frame(window)
frame_buttons.grid(row=4, column=0, columnspan=2, pady=10)

# Nút OK
button_ok = tk.Button(frame_buttons, text="OK", command=process_change_password, width=10)
button_ok.pack(side=tk.LEFT, padx=10)

# Nút Cancel
button_cancel = tk.Button(frame_buttons, text="Cancel", command=cancel_operation, width=10)
button_cancel.pack(side=tk.LEFT, padx=10)

# Chạy vòng lặp chính
window.mainloop()