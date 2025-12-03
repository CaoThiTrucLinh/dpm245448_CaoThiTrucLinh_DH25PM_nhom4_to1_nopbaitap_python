#Cau6
import random

# Hàm randrange(0, 100) sẽ trả về một số nguyên N, với 0 <= N < 100
# Tức là các số nguyên từ 0, 1, 2, ..., 99.

print("--- Câu 6: randrange(0, 100) ---")
print(f"Giá trị nhỏ nhất có thể: {0}")
print(f"Giá trị lớn nhất có thể: {99}")
print(f"Một ví dụ ngẫu nhiên: {random.randrange(0, 100)}")

# Kiểm tra các giá trị được hỏi:
print(f"\n4.5, 34., -1, 100 là những giá trị KHÔNG thể xuất hiện.")
print(f"0 và 99 là những giá trị CÓ thể xuất hiện.")