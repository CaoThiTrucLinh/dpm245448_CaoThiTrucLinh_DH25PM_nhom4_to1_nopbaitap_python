#Cau2
# XulyFile.py

def LuuFile(path, data):
    """
    Ghi dữ liệu 'data' vào file tại 'path'.
    Sử dụng chế độ 'a' (append) để thêm vào cuối file.
    """
    # Bước 1: Mở file ở chế độ 'a' (append) với encoding 'utf-8'
    file = open(path, 'a', encoding='utf-8') 
    
    # Bước 2: Ghi dữ liệu vào file
    file.writelines(data)
    
    # Bước 3: Ghi thêm ký tự xuống dòng '\n' để phân tách các dòng dữ liệu
    file.writelines("\n")
    
    # Bước 4: Đóng file
    file.close()

def DocFile(path):
    """
    Đọc dữ liệu từ file tại 'path' và chuyển thành list lồng nhau (ma trận số).
    """
    arrSo = [] # List chính để lưu ma trận số
    
    # Bước 1: Mở file ở chế độ 'r' (read) với encoding 'utf-8'
    file = open(path, 'r', encoding='utf-8')
    
    # Bước 2: Lặp qua từng dòng trong file
    for line in file:
        # Xóa các ký tự trắng thừa ở đầu/cuối dòng (bao gồm '\n')
        data = line.strip() 
        
        # Bỏ qua dòng trống nếu có
        if not data:
            continue
            
        # Tách dòng thành list các chuỗi số (dựa trên dấu phẩy)
        arr = data.split(',')
        
        # Khởi tạo list tạm để lưu các số nguyên của dòng hiện tại
        arrSoDong = []
        
        # Chuyển từng chuỗi số thành số nguyên (integer)
        for element in arr:
            try:
                # Chuyển đổi sang số nguyên
                number = int(element)
                arrSoDong.append(number)
            except ValueError:
                # Bỏ qua các phần tử không phải là số hợp lệ
                print(f"Cảnh báo: Bỏ qua phần tử '{element}' không phải là số nguyên.")

        # Thêm list số nguyên của dòng hiện tại vào list chính
        if arrSoDong:
            arrSo.append(arrSoDong)

    # Bước 3: Đóng file
    file.close()
    
    # Bước 4: Trả về ma trận số
    return arrSo

def XuatSoAmTrenMoiDong(arrSo):
    """
    Xuất ra các số âm trên màn hình, mỗi dòng in ra các số âm của dòng tương ứng.
    """
    for row in arrSo:
        so_am_trong_dong = []
        for number in row:
            if number < 0:
                so_am_trong_dong.append(str(number))
        
        # In các số âm của dòng, cách nhau bằng dấu tab
        if so_am_trong_dong:
            print('\t'.join(so_am_trong_dong))
            # TestDocFile.py

# --- Bước 3: Ghi dữ liệu vào file ---
file_path = "csdl_so.txt"

# Xóa nội dung file cũ (mở chế độ 'w' ghi đè) để đảm bảo không bị trùng lặp dữ liệu
try:
    with open(file_path, 'w', encoding='utf-8') as f:
        pass
except FileNotFoundError:
    pass # Nếu file chưa tồn tại thì không cần làm gì
    
# Ghi các dòng dữ liệu theo yêu cầu
LuuFile(file_path, "5,4,7,9,3,20")
LuuFile(file_path, "-5,-4,37,-19,24,-21")
LuuFile(file_path, "15,10,3,-3,-15")
LuuFile(file_path, "-4,77,-9,3,-7")
LuuFile(file_path, "55,44,27")
LuuFile(file_path, "-58,26")

print("Đã ghi xong dữ liệu vào file 'csdl_so.txt'.")


# --- Bước 4: Đọc, xử lý và xuất kết quả ---

print("\n--- KẾT QUẢ XỬ LÝ DỮ LIỆU TỪ FILE ---")

# 1. Đọc file và chuyển thành ma trận arrSo
arrSo = DocFile(file_path)

# 2. Xuất ma trận arrSo (Kiểm tra xem dữ liệu đọc có đúng không)
print("Ma trận số arrSo (Sau khi đọc và chuyển đổi):")
for row in arrSo:
    print(row)

print("\n3. Các số âm trên mỗi dòng:")

# 3. Xuất các số âm trên mỗi dòng
XuatSoAmTrenMoiDong(arrSo)