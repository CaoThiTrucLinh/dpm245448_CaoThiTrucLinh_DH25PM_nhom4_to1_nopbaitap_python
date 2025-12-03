#Cau10
import time
import os
import platform

def clear_screen():
    """Hàm dọn sạch màn hình console trước khi vẽ hình mới."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        # Dùng cho Linux và macOS
        os.system('clear')

def draw_shapes_with_sleep():
    """Vẽ 4 hình, mỗi hình cách nhau 5 giây."""
    print("--- Câu 10: Vẽ hình dùng sleep ---")
    
    shapes = [
        # Hình 1
        """
        *
       * *
      * * *
     * * * *
    * * * * *
        """,
        
        # Hình 2
        """
        * * * * *
         * * * * * * *
           * *
            *
        """,
        
        # Hình 3
        """
        * * * * *
        * * * * * * *
        * *
        *
        """,
        
        # Hình 4
        """
            *
           * *
          * * *
         * * * *
        * * * * *
        """
    ]
    
    # Do các hình trong đề bài có cấu trúc khác nhau, tôi sẽ sử dụng các chuỗi 
    # ký tự trực tiếp dựa trên yêu cầu của đề:
    
    # ----------------------------------------------------
    # KHAI BÁO CÁC HÌNH THEO ĐÚNG ĐỀ BÀI (dùng * và khoảng trắng)
    # ----------------------------------------------------

    shape_1 = """
     *
    * *
   * * *
  * * * *
 * * * * *
"""
    shape_2 = """
  * * * *
   * * *
    * *
     *
    * *
   * * *
  * * * *
"""

    shape_3 = """
 * * * * *
  * * * *
   * * *
    * *
     *
      *
     * *
    * * *
   * * * *
  * * * * *
"""
    shape_4 = """
* * * *
 * * *
  * *
   *
  * *
 * * *
* * * *
"""
    
    all_shapes = [shape_1, shape_2, shape_3, shape_4]

    # Vòng lặp để vẽ từng hình
    for i, shape in enumerate(all_shapes):
        clear_screen()
        print(f"--- Đang vẽ Hình {i + 1} / {len(all_shapes)} ---")
        print(shape)
        
        if i < len(all_shapes) - 1:
            print(f"Chờ 5 giây trước khi vẽ hình tiếp theo...")
            time.sleep(5) # Dừng chương trình 5 giây
        else:
            print("Đã vẽ xong 4 hình.")

# Chạy hàm vẽ hình
# draw_shapes_with_sleep()