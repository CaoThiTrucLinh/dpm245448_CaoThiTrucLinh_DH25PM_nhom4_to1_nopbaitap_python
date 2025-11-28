#Cau11
import math

def kiem_tra_so_nguyen_to(n):
    """
    Kiểm tra xem một số nguyên dương n có phải là số nguyên tố hay không.
    """
    if n <= 1:
        # Số nguyên tố là số nguyên lớn hơn 1
        return False
    if n == 2:
        # Số 2 là số nguyên tố chẵn duy nhất
        return True
    if n % 2 == 0:
        # Các số chẵn khác 2 không phải là số nguyên tố
        return False
    
    # Chỉ cần kiểm tra các ước số lẻ từ 3 đến căn bậc hai của n
    # Nếu n có một ước lớn hơn sqrt(n), thì nó cũng phải có một ước nhỏ hơn sqrt(n).
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            # Tìm thấy một ước, n không phải là số nguyên tố
            return False
            
    # Không tìm thấy ước nào, n là số nguyên tố
    return True

def chuong_trinh_chinh():
    """
    Hàm chính thực hiện vòng lặp kiểm tra và hỏi người dùng tiếp tục/thoát.
    """
    tiep_tuc = True
    while tiep_tuc:
        print("\n--- 🔎 KIỂM TRA SỐ NGUYÊN TỐ ---")
        
        try:
            so_nhap = input("Vui lòng nhập một số nguyên dương: ")
            
            # Kiểm tra nếu người dùng nhập rỗng hoặc ký tự không phải số
            if not so_nhap.isdigit():
                 print("⚠️ Lỗi: Vui lòng nhập một số nguyên hợp lệ.")
                 continue

            n = int(so_nhap)
            
            if kiem_tra_so_nguyen_to(n):
                print(f"✅ Số {n} là **số nguyên tố**.")
            else:
                print(f"❌ Số {n} **KHÔNG** phải là số nguyên tố.")

        except Exception as e:
            # Xử lý các lỗi ngoại lệ khác (rất hiếm trong trường hợp này)
            print(f"⚠️ Đã xảy ra lỗi: {e}")
            
        # Hỏi người dùng có muốn tiếp tục hay không
        while True:
            lua_chon = input("\nBạn có muốn tiếp tục kiểm tra? (Y/N): ").upper()
            if lua_chon == 'N':
                tiep_tuc = False
                print("👋 Cảm ơn bạn đã sử dụng phần mềm! Tạm biệt.")
                break
            elif lua_chon == 'Y':
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng nhập 'Y' hoặc 'N'.")

# 🚀 Thực thi chương trình
if __name__ == "__main__":
    chuong_trinh_chinh()