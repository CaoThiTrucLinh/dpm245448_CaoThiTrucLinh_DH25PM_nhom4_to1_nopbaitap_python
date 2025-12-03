#Cau9
import os

# Đường dẫn file dữ liệu
SAN_PHAM_FILE = "sanpham.txt"
DANH_MUC_FILE = "danhmuc.txt"

# --- I. CÁC HÀM XỬ LÝ FILE ---

def doc_du_lieu_tu_file(file_path):
    """Đọc tất cả dữ liệu từ file và trả về dưới dạng list các dictionary."""
    data = []
    if not os.path.exists(file_path):
        return data
        
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                # Giả định dữ liệu được lưu dưới dạng CSV: field1,field2,field3,...
                parts = line.split(',')
                
                if file_path == DANH_MUC_FILE and len(parts) >= 2:
                    data.append({'Ma': parts[0], 'Ten': parts[1]})
                
                elif file_path == SAN_PHAM_FILE and len(parts) >= 4:
                    data.append({
                        'Ma': parts[0],
                        'Ten': parts[1],
                        'DonGia': float(parts[2]),
                        'MaDanhMuc': parts[3]
                    })
    return data

def luu_du_lieu_vao_file(file_path, data):
    """Ghi tất cả dữ liệu (list of dicts) vào file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data:
            if file_path == DANH_MUC_FILE:
                line = f"{item['Ma']},{item['Ten']}\n"
            elif file_path == SAN_PHAM_FILE:
                line = f"{item['Ma']},{item['Ten']},{item['DonGia']},{item['MaDanhMuc']}\n"
            f.write(line)

# --- II. CÁC HÀM XỬ LÝ LOGIC ---

# Khởi tạo dữ liệu mẫu (Chỉ chạy lần đầu nếu file chưa tồn tại)
def khoi_tao_du_lieu_mau():
    if not os.path.exists(DANH_MUC_FILE):
        danh_muc_mau = [
            {'Ma': 'DM01', 'Ten': 'Thức uống có gas'},
            {'Ma': 'DM02', 'Ten': 'Đồ ăn nhanh'}
        ]
        luu_du_lieu_vao_file(DANH_MUC_FILE, danh_muc_mau)

    if not os.path.exists(SAN_PHAM_FILE):
        san_pham_mau = [
            {'Ma': 'SP001', 'Ten': 'Coca Cola', 'DonGia': 15000.0, 'MaDanhMuc': 'DM01'},
            {'Ma': 'SP002', 'Ten': 'Bánh mì kẹp', 'DonGia': 25000.0, 'MaDanhMuc': 'DM02'},
            {'Ma': 'SP003', 'Ten': 'Pepsi', 'DonGia': 18000.0, 'MaDanhMuc': 'DM01'}
        ]
        luu_du_lieu_vao_file(SAN_PHAM_FILE, san_pham_mau)

# --- Các chức năng Quản Lý Sản phẩm ---

def them_san_pham():
    """Thêm mới sản phẩm."""
    san_pham = doc_du_lieu_tu_file(SAN_PHAM_FILE)
    danh_muc = doc_du_lieu_tu_file(DANH_MUC_FILE)
    
    ma_sp = input("Nhập Mã sản phẩm mới: ").upper()
    if any(sp['Ma'] == ma_sp for sp in san_pham):
        print("Lỗi: Mã sản phẩm đã tồn tại.")
        return

    ten_sp = input("Nhập Tên sản phẩm: ")
    don_gia = float(input("Nhập Đơn giá: "))
    
    # Hiển thị danh mục để chọn
    print("Các danh mục hiện có:")
    for dm in danh_muc:
        print(f" - [{dm['Ma']}]: {dm['Ten']}")
        
    ma_dm = input("Nhập Mã Danh mục (ví dụ: DM01): ").upper()
    if not any(dm['Ma'] == ma_dm for dm in danh_muc):
        print("Lỗi: Mã Danh mục không tồn tại.")
        return

    new_sp = {'Ma': ma_sp, 'Ten': ten_sp, 'DonGia': don_gia, 'MaDanhMuc': ma_dm}
    san_pham.append(new_sp)
    luu_du_lieu_vao_file(SAN_PHAM_FILE, san_pham)
    print("Thêm sản phẩm thành công.")

def hien_thi_san_pham(san_pham):
    """Hiển thị danh sách sản phẩm (có thể là kết quả tìm kiếm/sắp xếp)."""
    if not san_pham:
        print("Không có sản phẩm nào để hiển thị.")
        return
        
    print("\n--- DANH SÁCH SẢN PHẨM ---")
    print(f"{'Mã SP':<8} | {'Tên SP':<25} | {'Đơn Giá':<12} | {'Mã DM':<8}")
    print("-" * 55)
    for sp in san_pham:
        print(f"{sp['Ma']:<8} | {sp['Ten']:<25} | {sp['DonGia']:<12,.0f} | {sp['MaDanhMuc']:<8}")
    print("-" * 55)

def xoa_san_pham():
    """Xóa sản phẩm theo mã."""
    san_pham = doc_du_lieu_tu_file(SAN_PHAM_FILE)
    ma_xoa = input("Nhập Mã sản phẩm cần xóa: ").upper()
    
    # Tạo list mới không chứa sản phẩm cần xóa
    san_pham_moi = [sp for sp in san_pham if sp['Ma'] != ma_xoa]
    
    if len(san_pham_moi) < len(san_pham):
        luu_du_lieu_vao_file(SAN_PHAM_FILE, san_pham_moi)
        print(f"Đã xóa sản phẩm có Mã: {ma_xoa}")
    else:
        print(f"Lỗi: Không tìm thấy sản phẩm có Mã: {ma_xoa}")

def tim_kiem_san_pham():
    """Tìm kiếm sản phẩm theo tên hoặc mã."""
    san_pham = doc_du_lieu_tu_file(SAN_PHAM_FILE)
    keyword = input("Nhập từ khóa (Mã hoặc Tên) sản phẩm: ").lower()
    
    ket_qua = [
        sp for sp in san_pham 
        if keyword in sp['Ma'].lower() or keyword in sp['Ten'].lower()
    ]
    
    hien_thi_san_pham(ket_qua)

def sap_xep_san_pham():
    """Sắp xếp sản phẩm theo Đơn giá."""
    san_pham = doc_du_lieu_tu_file(SAN_PHAM_FILE)
    
    # Sắp xếp theo Đơn giá giảm dần
    san_pham.sort(key=lambda sp: sp['DonGia'], reverse=True)
    
    print("--- SẢN PHẨM ĐÃ SẮP XẾP THEO ĐƠN GIÁ (GIẢM DẦN) ---")
    hien_thi_san_pham(san_pham)

# --- III. HÀM MAIN VÀ MENU ---

def menu_san_pham():
    """Menu chính của phần mềm Quản Lý Sản phẩm."""
    khoi_tao_du_lieu_mau()
    
    while True:
        print("\n===== QUẢN LÝ SẢN PHẨM (TEXT FILE) =====")
        print("1. Thêm mới sản phẩm")
        print("2. Hiển thị tất cả sản phẩm")
        print("3. Xóa sản phẩm theo mã")
        print("4. Tìm kiếm sản phẩm")
        print("5. Sắp xếp sản phẩm theo đơn giá")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-5): ")
        
        if choice == '1':
            them_san_pham()
        elif choice == '2':
            hien_thi_san_pham(doc_du_lieu_tu_file(SAN_PHAM_FILE))
        elif choice == '3':
            xoa_san_pham()
        elif choice == '4':
            tim_kiem_san_pham()
        elif choice == '5':
            sap_xep_san_pham()
        elif choice == '0':
            print("Đã thoát chương trình Quản Lý Sản phẩm.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
# if __name__ == "__main__":
#     menu_san_pham()