#Cau13
import xml.etree.ElementTree as ET
import os

# Tên file dữ liệu
NHOM_FILE = "nhomthietbi.xml"
THIET_BI_FILE = "ThietBi.xml"

# --- I. CÁC HÀM XỬ LÝ FILE (Đọc XML) ---

def tao_file_xml_mau():
    """Tạo các file XML mẫu nếu chưa tồn tại."""
    
    # 1. Tạo nhomthietbi.xml
    if not os.path.exists(NHOM_FILE):
        print(f"Đang tạo file mẫu: {NHOM_FILE}")
        root_nhom = ET.Element("nhomthietbis")
        
        # Dữ liệu Nhóm mẫu
        for i in range(1, 4):
            nhom = ET.SubElement(root_nhom, "nhom")
            # Giả định Ma Nhóm là 'a1', 'a2', 'a3'
            ET.SubElement(nhom, "ma").text = f"a{i}"
            ET.SubElement(nhom, "ten").text = f"Nhóm {i}"
            
        tree_nhom = ET.ElementTree(root_nhom)
        tree_nhom.write(NHOM_FILE, encoding='utf-8', xml_declaration=True)
        
    # 2. Tạo ThietBi.xml
    if not os.path.exists(THIET_BI_FILE):
        print(f"Đang tạo file mẫu: {THIET_BI_FILE}")
        root_tb = ET.Element("thietbis")
        
        # Dữ liệu Thiết bị mẫu (manhom='n1', 'n2', 'n3' tương ứng)
        thiet_bi_data = [
            ("n1", "tb1", "Thiết bị 1"), ("n1", "tb2", "Thiết bị 2"),
            ("n2", "tb3", "Thiết bị 3"), ("n2", "tb4", "Thiết bị 4"), ("n2", "tb5", "Thiết bị 5"),
            ("n3", "tb6", "Thiết bị 6")
        ]
        
        for manhom, ma, ten in thiet_bi_data:
            thietbi = ET.SubElement(root_tb, "thietbi", manhom=manhom)
            ET.SubElement(thietbi, "ma").text = ma
            ET.SubElement(thietbi, "ten").text = ten
            
        tree_tb = ET.ElementTree(root_tb)
        tree_tb.write(THIET_BI_FILE, encoding='utf-8', xml_declaration=True)
        
    print("Khởi tạo file XML hoàn tất.")

def doc_nhom_thiet_bi(file_path):
    """Đọc dữ liệu Nhóm Thiết bị."""
    nhom_list = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for nhom in root.findall('nhom'):
            ma = nhom.find('ma').text
            ten = nhom.find('ten').text
            nhom_list.append({'Ma': ma, 'Ten': ten})
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {file_path}")
    return nhom_list

def doc_thiet_bi(file_path):
    """Đọc dữ liệu Thiết bị."""
    thiet_bi_list = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for thietbi in root.findall('thietbi'):
            manhom = thietbi.attrib.get('manhom')
            ma = thietbi.find('ma').text
            ten = thietbi.find('ten').text
            thiet_bi_list.append({'MaNhom': manhom, 'Ma': ma, 'Ten': ten})
    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {file_path}")
    return thiet_bi_list

# --- II. CÁC CHỨC NĂNG XỬ LÝ DỮ LIỆU ---

def hien_thi_nhom_thiet_bi(nhom_list):
    """Hiển thị danh sách Nhóm thiết bị."""
    print("\n--- DANH SÁCH NHÓM THIẾT BỊ ---")
    if not nhom_list:
        print("Danh sách Nhóm thiết bị trống.")
        return
    print(f"{'Mã Nhóm':<10} | {'Tên Nhóm':<20}")
    print("-" * 35)
    for nhom in nhom_list:
        print(f"{nhom['Ma']:<10} | {nhom['Ten']:<20}")

def hien_thi_toan_bo_thiet_bi(thiet_bi_list):
    """Hiển thị toàn bộ Thiết bị."""
    print("\n--- TOÀN BỘ DANH SÁCH THIẾT BỊ ---")
    if not thiet_bi_list:
        print("Danh sách Thiết bị trống.")
        return
    print(f"{'Mã Nhóm':<10} | {'Mã TB':<8} | {'Tên Thiết Bị':<25}")
    print("-" * 48)
    for tb in thiet_bi_list:
        print(f"{tb['MaNhom']:<10} | {tb['Ma']:<8} | {tb['Ten']:<25}")

def loc_thiet_bi_theo_nhom(nhom_list, thiet_bi_list):
    """Lọc Danh sách Thiết bị theo Nhóm thiết bị."""
    
    # Hiển thị các nhóm có sẵn để người dùng chọn
    print("\n--- LỌC THIẾT BỊ THEO NHÓM ---")
    hien_thi_nhom_thiet_bi(nhom_list)
    
    ma_nhom_chon = input("Nhập Mã Nhóm (ví dụ: a1) để lọc thiết bị: ").lower()
    
    # Chuyển đổi mã nhóm nếu cần (ví dụ: a1 -> n1)
    # Giả định: Mã Nhóm trong Thiết bị (n1) tương đương với mã Nhóm chính (a1)
    if ma_nhom_chon.startswith('a'):
        # Thay 'a' bằng 'n' để phù hợp với thuộc tính manhom trong ThietBi.xml
        ma_nhom_thiet_bi = 'n' + ma_nhom_chon[1:] 
    else:
        ma_nhom_thiet_bi = ma_nhom_chon
        
    ket_qua_loc = [tb for tb in thiet_bi_list if tb['MaNhom'] == ma_nhom_thiet_bi]
    
    ten_nhom = next((nhom['Ten'] for nhom in nhom_list if nhom['Ma'] == ma_nhom_chon), "Không xác định")

    print(f"\n* Thiết bị thuộc Nhóm: {ten_nhom} ({ma_nhom_chon}) *")
    hien_thi_toan_bo_thiet_bi(ket_qua_loc)


def xuat_nhom_thiet_bi_co_so_luong_nhieu_nhat(nhom_list, thiet_bi_list):
    """Xuất Nhóm thiết bị có số lượng thiết bị nhiều nhất."""
    
    # 1. Đếm số lượng thiết bị cho mỗi nhóm (sử dụng thuộc tính MaNhom)
    dem_nhom = {}
    for tb in thiet_bi_list:
        ma_nhom = tb['MaNhom']
        dem_nhom[ma_nhom] = dem_nhom.get(ma_nhom, 0) + 1
        
    if not dem_nhom:
        print("Không có thiết bị nào để thống kê.")
        return
        
    # 2. Tìm số lượng lớn nhất
    max_so_luong = max(dem_nhom.values())
    
    # 3. Tìm các nhóm có số lượng bằng số lượng lớn nhất
    nhom_nhieu_nhat = []
    
    # Lặp qua danh sách nhóm chính để lấy Tên Nhóm
    for nhom in nhom_list:
        # Chuyển đổi mã nhóm (a1 -> n1) để so sánh với kết quả đếm
        ma_doi = 'n' + nhom['Ma'][1:] if nhom['Ma'].startswith('a') else nhom['Ma']
        
        if dem_nhom.get(ma_doi) == max_so_luong:
            nhom_nhieu_nhat.append(f"{nhom['Ten']} ({nhom['Ma']})")

    print("\n--- NHÓM THIẾT BỊ CÓ SỐ LƯỢNG THIẾT BỊ NHIỀU NHẤT ---")
    print(f"Tổng số lượng thiết bị lớn nhất: {max_so_luong}")
    print("Các nhóm đạt số lượng này:")
    for ten in nhom_nhieu_nhat:
        print(f"- {ten}")

# --- III. HÀM MAIN VÀ MENU ---

def menu_thiet_bi():
    """Menu chính của phần mềm Quản Lý Thiết Bị."""
    
    # Khởi tạo file mẫu lần đầu
    tao_file_xml_mau()
    
    while True:
        # Đọc dữ liệu mới nhất mỗi lần lặp
        nhom_list = doc_nhom_thiet_bi(NHOM_FILE)
        thiet_bi_list = doc_thiet_bi(THIET_BI_FILE)
        
        print("\n===== QUẢN LÝ THIẾT BỊ (XML FILE) =====")
        print("1. Hiển thị danh sách Nhóm thiết bị")
        print("2. Hiển thị toàn bộ Thiết bị")
        print("3. Lọc danh sách Thiết bị theo Nhóm")
        print("4. Xuất Nhóm thiết bị có số lượng nhiều nhất")
        print("0. Thoát")
        
        choice = input("Chọn chức năng (0-4): ")
        
        if choice == '1':
            hien_thi_nhom_thiet_bi(nhom_list)
        elif choice == '2':
            hien_thi_toan_bo_thiet_bi(thiet_bi_list)
        elif choice == '3':
            loc_thiet_bi_theo_nhom(nhom_list, thiet_bi_list)
        elif choice == '4':
            xuat_nhom_thiet_bi_co_so_luong_nhieu_nhat(nhom_list, thiet_bi_list)
        elif choice == '0':
            print("Đã thoát chương trình Quản Lý Thiết Bị.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

# Chạy chương trình
if __name__ == "__main__":
    menu_thiet_bi()