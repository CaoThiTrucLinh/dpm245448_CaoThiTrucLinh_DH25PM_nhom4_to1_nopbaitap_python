#Cau4
import tkinter as tk

# Biến toàn cục để lưu chuỗi phép tính
expression = ""

def press(num):
    """
    Hàm xử lý khi người dùng nhấn nút số hoặc toán tử.
    Cập nhật biểu thức và hiển thị lên màn hình.
    """
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    """
    Hàm xử lý khi người dùng nhấn nút '='.
    Tính toán kết quả của biểu thức.
    """
    global expression
    try:
        # Sử dụng eval() để tính toán chuỗi biểu thức.
        total = str(eval(expression))
        equation.set(total)
        # Bắt đầu biểu thức mới bằng kết quả vừa tính.
        expression = total
    except:
        # Xử lý lỗi nếu biểu thức không hợp lệ (ví dụ: chia cho 0)
        equation.set(" Lỗi ")
        expression = ""

def clear():
    """
    Hàm xử lý khi người dùng nhấn nút 'Clr'.
    Xóa toàn bộ biểu thức.
    """
    global expression
    expression = ""
    equation.set("")

# --- Thiết lập cửa sổ chính ---
if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Máy Tính Đơn Giản")
    gui.resizable(False, False) # Cố định kích thước

    # Biến String để liên kết với màn hình hiển thị kết quả
    equation = tk.StringVar()

    # Màn hình hiển thị
    expression_field = tk.Entry(gui, textvariable=equation, font=('Arial', 14), bd=5, relief=tk.SUNKEN, justify='right')
    expression_field.grid(columnspan=4, ipadx=8, ipady=8, padx=5, pady=5)

    # --- Thiết lập các nút ---

    # Hàm tạo nút đơn giản
    def create_button(text, command, row, col, columnspan=1):
        return tk.Button(gui, text=text, fg='black', bg='light grey',
                         command=command, height=2, width=8).grid(row=row, column=col, columnspan=columnspan, padx=2, pady=2)

    # Dòng 1: 1, 2, 3, +
    create_button('1', lambda: press(1), 2, 0)
    create_button('2', lambda: press(2), 2, 1)
    create_button('3', lambda: press(3), 2, 2)
    create_button('+', lambda: press('+'), 2, 3)

    # Dòng 2: 4, 5, 6, -
    create_button('4', lambda: press(4), 3, 0)
    create_button('5', lambda: press(5), 3, 1)
    create_button('6', lambda: press(6), 3, 2)
    create_button('-', lambda: press('-'), 3, 3)

    # Dòng 3: 7, 8, 9, *
    create_button('7', lambda: press(7), 4, 0)
    create_button('8', lambda: press(8), 4, 1)
    create_button('9', lambda: press(9), 4, 2)
    create_button('*', lambda: press('*'), 4, 3)

    # Dòng 4: ., 0, /, =
    create_button('.', lambda: press('.'), 5, 0)
    create_button('0', lambda: press(0), 5, 1)
    create_button('/', lambda: press('/'), 5, 2)
    create_button('=', equalpress, 5, 3)

    # Dòng 5: Clr
    create_button('Clr', clear, 6, 0, columnspan=4)

    # Chạy vòng lặp chính
    gui.mainloop()