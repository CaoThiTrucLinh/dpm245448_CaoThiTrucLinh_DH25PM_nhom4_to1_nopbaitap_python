#Cau10
import json
import os

# Đường dẫn file dữ liệu
SINH_VIEN_FILE = "sinhvien.json"

# --- I. CÁC HÀM XỬ LÝ FILE ---

def doc_du_lieu_tu_json(file_path):
    """Đọc dữ liệu từ file JSON và trả về dưới dạng list các dictionary (Lớp)."""
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        return []
        
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # Xử lý trường hợp file JSON bị lỗi định dạng
            return []

def luu_du_lieu_vao_json(file_path, data):
    """Ghi dữ liệu (list of dicts) vào file JSON."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# --- II. CÁC HÀM XỬ LÝ LOGIC ---

def khoi_tao_du_lieu_mau_sv():
    """Khởi tạo dữ liệu mẫu Lớp và Sinh viên nếu file chưa tồn tại."""
    if not os.path.exists(SINH_VIEN_FILE):
        lop_mau = [
            {
                'MaLop': 'CNTT01', 
                'TenLop': 'Kỹ thuật Phần mềm 01',
                'SinhVien': [
                    {'Ma': 'SV001', 'Ten': 'Nguyễn Văn A', 'NamSinh': 2004},
                    {'Ma': 'SV002', 'Ten': 'Trần Thị B', 'NamSinh': 2003}
                ]
            },
            {
                'MaLop': 'CNTT02', 
                'TenLop': 'Hệ thống Thông tin 02',
                'SinhVien': [
                    {'Ma': 'SV003', 'Ten': 'Lê Văn C', 'NamSinh': 2004}
                ]
            }
        ]
        luu_du_lieu_vao_json(SINH_VIEN_FILE, lop_mau)

def hien_thi_sv_cua_lop(lop):
    """Hàm hiển thị danh sách sinh viên của một lớp."""
    print(f"\n[Lớp {lop['MaLop']}]: {lop['TenLop']}")
    if not lop['SinhVien']:
        print("   (Chưa có sinh viên nào)")
        return

    print(f"   {'Mã SV':<8} | {'Tên Sinh Viên':<25} | {'Năm Sinh':<10}")
    print("   " + "-" * 45)
    for sv in lop['SinhVien']:
        print(f"   {sv['Ma']:<8} | {sv['Ten']:<25} | {sv['NamSinh']:<10}")

def them_sinh_vien():
    """Thêm một sinh viên mới vào lớp đã chọn."""
    data = doc_du_lieu_tu_json(SINH_VIEN_FILE)
    
    # Yêu cầu nhập Mã Lớp
    ma_lop = input("Nhập Mã Lớp cần thêm sinh viên: ").upper()
    lop_tim_thay = next((lop for lop in data if lop['MaLop'] == ma_lop), None)
    
    if not lop_tim_thay:
        print("Lỗi: Không tìm thấy Mã Lớp này.")
        return

    # Nhập thông tin Sinh viên
    ma_sv = input("Nhập Mã Sinh viên mới: ").upper()
    # Kiểm tra trùng Mã SV trong toàn bộ hệ thống
    if any(sv['Ma'] == ma_sv for lop in data for sv in lop['SinhVien']):
        print("Lỗi: Mã Sinh viên đã tồn tại trong hệ thống.")
        return
        
    ten_sv = input("Nhập Tên Sinh viên: ")
    nam_sinh = int(input("Nhập Năm sinh: "))
    
    new_sv = {'Ma': ma_sv, 'Ten': ten_sv, 'NamSinh': nam_sinh}
    lop_tim_thay['SinhVien'].append(new_sv)
    
    luu_du_lieu_vao_json(SINH_VIEN_FILE, data)
    print(f"Thêm sinh viên {ma_sv} vào lớp {ma_lop} thành công.")

def hien_thi_tat_ca_lop():
    """Hiển thị tất cả các lớp và sinh viên trong lớp đó."""
    data = doc_du_lieu_tu_json(SINH_VIEN_FILE)
    if not data:
        print("Chưa có dữ liệu Lớp/Sinh viên.")
        return
        
    for lop in data:
        hien_thi_sv_cua_lop(lop)

def tim_kiem_sinh_vien():
    """Tìm kiếm sinh viên theo tên hoặc mã trong toàn bộ hệ thống."""
    data = doc_du_lieu_tu_json(SINH_VIEN_FILE)
    keyword = input("Nhập từ khóa (Mã hoặc Tên) Sinh viên: ").lower()
    
    ket_qua = []
    for lop in data:
        for sv in lop['SinhVien']:
            if keyword in sv['Ma'].lower() or keyword in sv['Ten'].lower():
                ket_qua.append((lop['MaLop'], sv)) # Lưu kèm Mã Lớp để dễ quản lý
                
    if not ket_qua:
        print(f"Không tìm thấy sinh viên nào với từ khóa '{keyword}'.")
        return

    print("\n--- KẾT QUẢ TÌM KIẾM SINH VIÊN ---")
    print(f"{'Mã SV':<8} | {'Tên Sinh Viên':<25} | {'Năm Sinh':<10} | {'Mã Lớp':<8}")
    print("-" * 55)
    for ma_lop, sv in ket_qua:
        print(f"{sv['Ma']:<8} | {sv['Ten']:<25} | {sv['NamSinh']:<10} | {ma_lop:<8}")

def sap_xep_sinh_vien_theo_nam_sinh():
    """Sắp xếp tất cả sinh viên trong từng lớp theo Năm sinh."""
    data = doc_du_lieu_tu_json(SINH_VIEN_FILE)
    
    for lop in data:
        # Sắp xếp theo Năm sinh tăng dần
        lop['SinhVien'].sort(key=lambda sv: sv['NamSinh'], reverse=False)
        
    luu_du_lieu_vao_json(SINH_VIEN_FILE, data)
    print("Đã sắp xếp sinh viên trong tất cả các lớp theo Năm sinh (tăng dần) và lưu lại.")
    hien_thi_tat_ca_lop()

# --- III. HÀM MAIN VÀ MENU ---

def menu_sinh_vien():
    """Menu chính của phần mềm Quản Lý Sinh Viên."""
    khoi_tao_du_lieu_mau_sv()
    
    while True:
        print("\n===== QUẢN LÝ SINH VIÊN (JSON FILE) =====")
        print("1. Thêm sinh viên mới")
        print("2. Hiển thị tất cả lớp và sinh viên")
        print("3. Tìm kiếm sinh viên")
        print("4. Sắp xếp sinh viên theo năm sinh")
        # Yêu cầu Sửa/Xóa cần thêm logic phức tạp hơn, có thể bổ sung sau
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-4): ")
        
        if choice == '1':
            them_sinh_vien()
        elif choice == '2':
            hien_thi_tat_ca_lop()
        elif choice == '3':
            tim_kiem_sinh_vien()
        elif choice == '4':
            sap_xep_sinh_vien_theo_nam_sinh()
        elif choice == '0':
            print("Đã thoát chương trình Quản Lý Sinh Viên.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
# if __name__ == "__main__":
#     menu_sinh_vien()