#Cau6
import tkinter as tk

def create_styled_buttons():
    """Tạo và hiển thị các nút với các style relief khác nhau."""
    window = tk.Tk()
    window.title("Các Style Relief Cho Button")
    
    # Định nghĩa các giá trị relief (style)
    relief_styles = [tk.FLAT, tk.SUNKEN, tk.RAISED, tk.GROOVE, tk.RIDGE, tk.SOLID]
    
    # Định nghĩa các giá trị borderwidth (độ dày đường viền)
    border_widths = [1, 2, 5]
    
    # Tiêu đề
    tk.Label(window, text="Kiểu Relief", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
    for col, relief_style in enumerate(relief_styles):
        tk.Label(window, text=relief_style.capitalize(), font=("Arial", 10)).grid(row=0, column=col + 1, padx=5, pady=5)
        
    # Tạo các nút
    row_index = 1
    for bw in border_widths:
        # Nhãn cho Borderwidth
        tk.Label(window, text=f"Borderwidth={bw}", font=("Arial", 10, "bold")).grid(row=row_index, column=0, padx=5, pady=5, sticky='w')
        
        for col, relief_style in enumerate(relief_styles):
            button_text = f"bw={bw}\n{relief_style}"
            
            tk.Button(window, 
                      text=relief_style.capitalize(), 
                      relief=relief_style, 
                      borderwidth=bw,
                      width=10,
                      height=2).grid(row=row_index, column=col + 1, padx=5, pady=5)
            
        row_index += 1

    window.mainloop()

if __name__ == "__main__":
    create_styled_buttons()