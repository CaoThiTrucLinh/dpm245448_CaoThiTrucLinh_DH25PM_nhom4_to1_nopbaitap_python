#Cau5
import string

def analyze_string():
    """Nhập một chuỗi và đếm số lượng các loại ký tự khác nhau."""
    print("\n--- Câu 5: Xử lý chuỗi với các hàm cơ bản ---")
    s = input("Nhập một chuỗi bất kỳ: ")
    
    # Khởi tạo bộ đếm
    count_upper = 0
    count_lower = 0
    count_digit = 0
    count_space = 0
    count_vowels = 0
    count_consonants = 0
    
    # Định nghĩa tập hợp nguyên âm (tiếng Việt thường dùng A, E, I, O, U, Y)
    VOWELS = "aeiouyáàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵAEIOUYÁÀẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴ"
    
    # Ký tự đặc biệt (tất cả những gì còn lại không phải chữ, số, hay khoảng trắng)
    count_special = 0

    for char in s:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
             # Kiểm tra chữ cái
            if char.isupper():
                count_upper += 1
            else:
                count_lower += 1
            
            # Kiểm tra Nguyên Âm / Phụ Âm
            if char in VOWELS:
                count_vowels += 1
            else:
                count_consonants += 1
                
        elif char.isdigit():
            # Kiểm tra chữ số
            count_digit += 1
        elif char.isspace():
            # Kiểm tra khoảng trắng
            count_space += 1
        else:
            # Còn lại là ký tự đặc biệt
            count_special += 1

    # Xuất kết quả
    print("\n--- Kết quả Phân tích Chuỗi ---")
    print(f"Bao nhiêu chữ IN HOA: {count_upper}")
    print(f"Bao nhiêu chữ in thường: {count_lower}")
    print(f"Bao nhiêu chữ là chữ số: {count_digit}")
    print(f"Bao nhiêu chữ là ký tự đặc biệt: {count_special}")
    print(f"Bao nhiêu chữ là khoảng trắng: {count_space}")
    print(f"Bao nhiêu chữ là Nguyên Âm: {count_vowels}")
    print(f"Bao nhiêu chữ là Phụ Âm: {count_consonants}")

# analyze_string()