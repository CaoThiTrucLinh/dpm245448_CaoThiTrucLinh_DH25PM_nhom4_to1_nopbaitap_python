#Cau6
import re

def NegativeNumberInStrings(s):
    """
    Trích xuất tất cả các số nguyên âm từ một chuỗi.
    Sử dụng biểu thức chính quy (regular expression).
    """
    print(f"\n--- Câu 6: Trích lọc số âm trong chuỗi ---")
    
    # Biểu thức chính quy tìm số nguyên âm:
    # -\d+ 
    #   - : khớp với dấu trừ (dấu âm)
    #   \d+ : khớp với một hoặc nhiều chữ số (0-9)
    #
    # Lưu ý: re.findall trả về danh sách các chuỗi khớp.
    negative_numbers_str = re.findall(r'-\d+', s)
    
    # Chuyển đổi các chuỗi số âm tìm được thành số nguyên (int)
    negative_numbers_int = [int(num_str) for num_str in negative_numbers_str]
    
    return negative_numbers_int

# Thử nghiệm hàm:
test_string = "abc-5xyz-12k9l-30--p-4"
result = NegativeNumberInStrings(test_string)

print(f"Chuỗi đầu vào: '{test_string}'")
print(f"Các số nguyên âm trích được: {result}") 
# Kết quả sẽ là: [-5, -12, -30, -4]