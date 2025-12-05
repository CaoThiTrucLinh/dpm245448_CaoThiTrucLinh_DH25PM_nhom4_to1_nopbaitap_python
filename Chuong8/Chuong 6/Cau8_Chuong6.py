#Cau8
## Câu 8: Sắp xếp dãy số theo thứ tự giảm dần
def sort_list_descending():
    """Nhập dãy số và sắp xếp theo thứ tự giảm dần."""
    user_input = input("\n[Câu 8] Nhập một dãy các số thực (cách nhau bằng dấu phẩy) để sắp xếp: ")
    
    try:
        # Chuyển chuỗi nhập vào thành list các số thực
        float_list = [float(x.strip()) for x in user_input.split(',')]
        
        # Sắp xếp giảm dần
        float_list.sort(reverse=True)
        
        print(f"[Câu 8] Dãy số sau khi sắp xếp giảm dần là: {float_list}")
        return float_list
        
    except ValueError:
        print("Nhập sai định dạng. Vui lòng nhập các số cách nhau bằng dấu phẩy.")

# Chạy câu 8
# sorted_desc_list = sort_list_descending()

