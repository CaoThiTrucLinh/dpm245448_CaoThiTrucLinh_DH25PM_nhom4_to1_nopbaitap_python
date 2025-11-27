#Cau8
# ===== Các loại lỗi khi lập trình và cách bắt lỗi trong Python =====

# 1. Lỗi cú pháp (Syntax Error)
# Xảy ra khi viết sai cú pháp, thiếu dấu ngoặc, dấu hai chấm,...
# Ví dụ: (dòng dưới nếu chạy sẽ báo lỗi)
# if True print("Hello")   # <-- Lỗi cú pháp


# 2. Lỗi khi chạy chương trình (Runtime Error)
# Xảy ra khi chương trình đang chạy và gặp vấn đề như chia cho 0, sai kiểu dữ liệu,...
# Ví dụ:
# x = 10 / 0   # Lỗi ZeroDivisionError


# 3. Lỗi logic (Logic Error)
# Chương trình chạy bình thường nhưng ra kết quả sai.
# Ví dụ: tính tổng nhưng lại viết nhầm thành phép nhân
def tong_sai(a, b):
    return a * b   # <-- Lỗi logic


# ===== Cách bắt lỗi trong Python: try - except =====

try:
    x = int(input("Nhập một số nguyên: "))
    y = 10 / x
    print("Kết quả:", y)

except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")

except ValueError:
    print("Lỗi: Bạn phải nhập số nguyên!")

except Exception as e:
    # Bắt mọi lỗi còn lại
    print("Lỗi khác xảy ra:", e)

finally:
    print("Khối finally luôn được chạy dù có lỗi hay không.")