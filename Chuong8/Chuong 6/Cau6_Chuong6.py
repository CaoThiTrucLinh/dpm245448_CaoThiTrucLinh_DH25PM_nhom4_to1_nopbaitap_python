#Cau6
import random

## Câu 6: Nhập list N số ngẫu nhiên KHÔNG TRÙNG NHAU
def generate_unique_random_list():
    """Nhập N và tạo list N số nguyên ngẫu nhiên không trùng nhau."""
    while True:
        try:
            n = int(input("Nhập số lượng phần tử N (>0) cho list: "))
            if n > 0:
                break
            else:
                print("N phải là số nguyên dương. Vui lòng nhập lại.")
        except ValueError:
            print("Nhập sai định dạng. Vui lòng nhập một số nguyên.")

    # Giả sử phạm vi số ngẫu nhiên đủ lớn để chứa N số duy nhất, ví dụ từ 1 đến 1000
    lower_bound = 1
    upper_bound = 1000
    
    if n > upper_bound - lower_bound + 1:
        print(f"Không thể tạo {n} số duy nhất trong phạm vi từ {lower_bound} đến {upper_bound}.")
        return []

    # Dùng set để đảm bảo các số được chọn là duy nhất
    unique_numbers = set()
    while len(unique_numbers) < n:
        unique_numbers.add(random.randint(lower_bound, upper_bound))

    # Chuyển set thành list và in ra
    random_unique_list = list(unique_numbers)
    print(f"\n[Câu 6] List {n} số ngẫu nhiên KHÔNG TRÙNG NHAU là: {random_unique_list}")
    return random_unique_list

# Chạy câu 6
# unique_list = generate_unique_random_list()