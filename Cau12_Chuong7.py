#Cau12
import random
import os

# Tên file CSV
FILE_NAME = "du_lieu_ngau_nhien.csv"
TONG_SO_DONG = 10
SO_PHAN_TU_MOI_DONG = 10
GIOI_HAN_SO = (1, 100) # Phạm vi số ngẫu nhiên từ 1 đến 100

# --- PHẦN 1: TẠO VÀ GHI FILE CSV ---

def khoi_tao_csv_so_ngau_nhien(file_path):
    """
    Tạo tệp CSV với 10 dòng, mỗi dòng 10 số ngẫu nhiên cách nhau bởi dấu ','
    """
    print(f"--- 1. Đang tạo file '{file_path}' với {TONG_SO_DONG} dòng ---")
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for _ in range(TONG_SO_DONG):
                # Tạo list 10 số ngẫu nhiên trong phạm vi [1, 100]
                numbers = [random.randint(GIOI_HAN_SO[0], GIOI_HAN_SO[1]) 
                           for _ in range(SO_PHAN_TU_MOI_DONG)]
                
                # Chuyển list số thành chuỗi, phân tách bằng dấu phẩy
                line = ",".join(map(str, numbers))
                
                # Ghi chuỗi và xuống dòng
                f.write(line + "\n")
        print(f"✅ Tạo file thành công. File '{file_path}' đã sẵn sàng.")
        
        # In ra nội dung mẫu để kiểm tra
        print("\nNội dung file (ví dụ):")
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i < 3: # Chỉ in 3 dòng đầu
                    print(line.strip())
                elif i == 3:
                    print("...")
    except Exception as e:
        print(f"Lỗi khi tạo file: {e}")

# --- PHẦN 2: ĐỌC VÀ TÍNH TỔNG GIÁ TRỊ ---

def doc_va_tinh_tong_csv(file_path):
    """
    Đọc tệp CSV, tính tổng giá trị của các phần tử trên mỗi dòng và xuất ra.
    """
    print(f"\n--- 2. Đang xử lý file '{file_path}' và tính tổng ---")
    
    if not os.path.exists(file_path):
        print("Lỗi: Không tìm thấy file để đọc.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f"{'Dòng':<8} | {'Dãy số (10 phần tử)':<40} | {'Tổng giá trị'}")
            print("-" * 70)
            
            for i, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                    
                # 1. Tách chuỗi thành list các chuỗi số
                str_numbers = line.split(',')
                
                # 2. Chuyển đổi sang số nguyên và tính tổng
                current_sum = 0
                processed_numbers = []
                
                for s in str_numbers:
                    try:
                        num = int(s)
                        current_sum += num
                        processed_numbers.append(str(num)) # Lưu lại để in ra
                    except ValueError:
                        print(f"Cảnh báo: Bỏ qua giá trị không hợp lệ '{s}' ở dòng {i+1}")
                        
                # 3. Xuất kết quả
                print(f"{i+1:<8} | {', '.join(processed_numbers):<40} | {current_sum}")
                
    except Exception as e:
        print(f"Lỗi khi đọc file: {e}")

# --- CHƯƠNG TRÌNH CHÍNH ---

def main_csv_handler():
    # 1. Khởi tạo file CSV
    khoi_tao_csv_so_ngau_nhien(FILE_NAME)
    
    # 2. Đọc file và tính tổng
    doc_va_tinh_tong_csv(FILE_NAME)

# Thực thi chương trình
main_csv_handler()