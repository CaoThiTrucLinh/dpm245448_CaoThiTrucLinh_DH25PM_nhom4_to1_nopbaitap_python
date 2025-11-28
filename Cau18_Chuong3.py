#Cau18
def draw_all_shapes(n):
    print(f"\n--- Câu 18: Vẽ các hình với n = {n} ---")

    if n <= 0:
        print("Chiều cao n phải là số dương.")
        return
    
    # --- Hình 1: Tam giác vuông trái dưới (như ảnh) ---
    # Trong ảnh là tam giác vuông góc dưới bên trái,
    # với các hàng dấu sao có độ dài tương ứng.
    # VD với n=3:
    # *
    # * *
    # * * *
    # NHƯNG trong ảnh là 3 sao ở hàng đầu, 2 ở hàng 2, 1 ở hàng 3
    # nên nó là một tam giác vuông ngược (dưới trái).
    print("\n--- Hình 1: Tam giác vuông ngược (dưới trái) ---")
    for i in range(n):
        print("* " * (n - i))

    # --- Hình 2: Hình tam giác rỗng bên phải (như ảnh) ---
    # VD với n=3:
    #   *
    # * *
    # *****
    # Đây là hình tam giác cân, nhưng có 2 cạnh.
    print("\n--- Hình 2: Hình tam giác rỗng (cân) ---")
    # Vẽ phần trên (các hàng rỗng)
    for i in range(n - 1): # n-1 hàng đầu
        if i == 0: # Hàng đầu tiên (chỉ 1 sao ở giữa)
            print(" " * (n - 1) + "*")
        else: # Các hàng ở giữa
            leading_spaces = " " * (n - 1 - i)
            middle_spaces = " " * (2 * i - 1)
            print(leading_spaces + "*" + middle_spaces + "*")
    # Vẽ hàng cuối cùng (toàn sao)
    print("* " * n)


    # --- Hình 3: Hình chữ V (như ảnh) ---
    # Với n là chiều cao, tạo hình chữ V
    # VD với n=3:
    # * *
    #  * *
    #   *
    print("\n--- Hình 3: Hình chữ V ---")
    for i in range(n):
        leading_spaces = " " * i
        if i == n - 1: # Đáy của chữ V (chỉ 1 sao)
            print(leading_spaces + "*")
        else: # Các hàng phía trên (2 sao)
            middle_spaces = " " * (2 * (n - 1 - i) - 1)
            print(leading_spaces + "*" + middle_spaces + "*")


    # --- Hình 4: Hình chữ W (như ảnh) ---
    # Hình trong ảnh là một chữ W đơn giản, có vẻ là 2 chữ V cạnh nhau.
    # VD với n=5 trong ảnh
    # * *
    #  * *
    #   * *
    #    * *
    #     *
    #    * *
    #   * *
    #  * *
    # * *
    print("\n--- Hình 4: Hình chữ W ---")
    # Để vẽ chính xác hình W trong ảnh, nó có vẻ là 2 chữ V đối xứng nhau.
    # Giả định n là số hàng cho một nửa chữ W (từ trên xuống đáy)
    # Và sau đó lại tăng lên.
    
    # Phần trên của W (giảm dần xuống đáy)
    for i in range(n):
        # Khoảng cách từ lề trái
        indent1 = " " * i
        
        # Khoảng cách giữa sao thứ nhất và thứ hai (chữ V đầu tiên)
        gap1 = " " * (2 * (n - 1 - i) - 1)
        
        # Khoảng cách giữa chữ V đầu tiên và chữ V thứ hai
        gap_between_Vs = " " * (2 * i + 1) #