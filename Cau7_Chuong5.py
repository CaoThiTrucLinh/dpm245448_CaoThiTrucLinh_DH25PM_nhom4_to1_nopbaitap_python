#Cau7
def optimize_name_string(s):
    """
    Tối ưu hóa chuỗi danh từ theo 3 tiêu chí: 
    1. Loại bỏ khoảng trắng dư thừa ở đầu/cuối.
    2. Chỉ giữ lại 1 khoảng trắng giữa các từ.
    3. Viết hoa chữ cái đầu tiên của mỗi từ.
    """
    print("\n--- Câu 7: Tối ưu chuỗi danh từ ---")
    
    # 1. Loại bỏ khoảng trắng dư thừa ở đầu/cuối và tách chuỗi thành các từ
    # s.split() tự động xử lý nhiều khoảng trắng giữa các từ.
    words = s.split() 
    
    if not words:
        return "" # Trả về chuỗi rỗng nếu đầu vào là rỗng hoặc toàn khoảng trắng

    # 2. Xử lý từng từ: Viết hoa chữ cái đầu tiên (s.capitalize())
    # và tạo danh sách mới
    processed_words = [word.capitalize() for word in words]
    
    # 3. Nối các từ lại với nhau bằng một khoảng trắng duy nhất
    optimized_string = " ".join(processed_words)
    
    return optimized_string

# Thử nghiệm hàm:
input_str = " Trần duY   thAnH "
output_str = optimize_name_string(input_str)

print(f"Input: '{input_str}'")
print(f"Output: '{output_str}'") 
# Kết quả: 'Trần Duy Thanh'