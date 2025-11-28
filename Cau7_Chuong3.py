#Cau7
from datetime import datetime, timedelta

def find_next_day(day_str):
    """
    Tìm ngày kế tiếp sau ngày vừa nhập.
    day_str có format 'ngày/tháng/năm' (ví dụ: '27/11/2025').
    """
    try:
        # Chuyển chuỗi nhập vào thành đối tượng datetime
        current_date = datetime.strptime(day_str, '%d/%m/%Y')
        
        # Thêm 1 ngày
        next_date = current_date + timedelta(days=1)
        
        # Trả về ngày kế tiếp dưới dạng chuỗi
        return next_date.strftime('%d/%m/%Y')
        
    except ValueError:
        return "Ngày nhập vào không hợp lệ. Vui lòng sử dụng định dạng ngày/tháng/năm."

# Ví dụ kiểm tra
print("\n--- Câu 7: Tìm ngày kế tiếp ---")
date_input_a = "31/12/2024"
date_input_b = "29/02/2024" # Năm nhuận
print(f"Ngày {date_input_a} => Ngày kế tiếp: {find_next_day(date_input_a)}")
print(f"Ngày {date_input_b} => Ngày kế tiếp: {find_next_day(date_input_b)}")